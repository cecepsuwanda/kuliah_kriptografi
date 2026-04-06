import pandas as pd
import re
import os

def parse_uts_data(file_path):
    """
    Parses soal_uts.tex into a list of dictionaries for Excel export.
    Assumes standard format with 'Soal Pilihan Ganda' and 'Kunci Jawaban'.
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into Questions and Answers sections
    # Rough split based on section headers
    parts = content.split(r'\section*{Kunci Jawaban}')
    if len(parts) < 2:
        print("Could not find 'Kunci Jawaban' section.")
        return []
    
    questions_part = parts[0]
    answers_part = parts[1]

    # --- Parse Answers first to build a map: {question_number: 'A'/'B'/'C'/'D'} ---
    # Look for \item A, \item B, etc. inside the enumerate block in answers_part
    # The enumerate uses [label=\textbf{Soal \arabic*.}]
    
    # We can just look for \item\s*([A-D]) since the structure is simple list of items
    # But better to be guided by the enumerate structure if possible, 
    # or just simple regex if the format is strict.
    # The file shows: \item D \item A ...
    
    # Let's find all items in the answer section
    answer_items = re.findall(r'\\item\s+([A-D])', answers_part)
    answer_map = {i+1: ans for i, ans in enumerate(answer_items)}
    
    # --- Parse Questions ---
    # Questions are in \begin{enumerate}[label=\textbf{Soal \arabic*.}, ...]
    # We can try to split by \item but we have nested enumerate for options.
    
    # Strategy: Find the main enumerate block for questions
    # It starts after \section*{Soal Pilihan Ganda}
    
    # Regex to find each question block: \item ... (text) ... \begin{enumerate} ... \end{enumerate}
    # This might be tricky with regex. 
    # Let's split by "\item " but identifying which \item is a question and which is an option.
    # Question items are at depth 0 of the list, options at depth 1.
    
    # Simpler approach:
    # 1. Extract the text between \begin{enumerate}[label=\textbf{Soal \arabic*.}...] and the corresponding \end{enumerate}
    # 2. Inside that, split by `\item ` that are NOT inside the nested enumerate? 
    #    Actually, the nested enumerate is for options. 
    
    # Let's use a regex that captures the question text and the options block.
    # Pattern: \item (Question Text) \begin{enumerate} (Options) \end{enumerate}
    
    question_matches = re.findall(r'\\item\s+(.*?)\\begin\{enumerate\}\[label=\\Alph\*\.\].*?\s*(.*?)\s*\\end\{enumerate\}', questions_part, re.DOTALL)
    
    parsed_questions = []
    
    for idx, (q_text, opts_block) in enumerate(question_matches):
        q_num = idx + 1
        q_text = q_text.strip()
        
        # Parse options from opts_block
        # Options are list items: \item OptionText
        options = re.findall(r'\\item\s+(.*?)(?=\\item|\Z)', opts_block, re.DOTALL)
        options = [o.strip() for o in options]
        
        # We expect 4 options usually, but code should handle variable count
        correct_letter = answer_map.get(q_num)
        
        correct_answer = ""
        incorrect_answers = []
        
        if correct_letter:
            # Map 'A'->0, 'B'->1, ...
            # letter_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
            # correct_idx = letter_map.get(correct_letter)
             
            # Robust mapping
            idx_map = {char: i for i, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
            correct_idx = idx_map.get(correct_letter)
            
            if correct_idx is not None and correct_idx < len(options):
                correct_answer = options[correct_idx]
                incorrect_answers = [opt for i, opt in enumerate(options) if i != correct_idx]
            else:
                # Fallback if answer key layout doesn't match options
                incorrect_answers = options[:]
        else:
             incorrect_answers = options[:]

        # Pad incorrect answers to at least 3 for the template logic (usually 3 distractors)
        # The template expects "Incorrect Answer 01" ... "03"
        while len(incorrect_answers) < 3:
            incorrect_answers.append("")
            
        q_data = {
            "Question": q_text,
            "Correct Answer": correct_answer,
            "Incorrect Answer 01": incorrect_answers[0] if len(incorrect_answers) > 0 else "",
            "Incorrect Answer 02": incorrect_answers[1] if len(incorrect_answers) > 1 else "",
            "Incorrect Answer 03": incorrect_answers[2] if len(incorrect_answers) > 2 else "",
            # Add 4th if exists
            "Incorrect Answer 04": incorrect_answers[3] if len(incorrect_answers) > 3 else ""
        }
        parsed_questions.append(q_data)
        
    return parsed_questions

if __name__ == "__main__":
    # Original logic
    q_file = os.path.join('sections', 'bab-18_sec01.tex')
    a_file = os.path.join('sections', 'bab-18_sec02.tex')
    
    if os.path.exists(q_file) and os.path.exists(a_file):
        ans_map = parse_answers(a_file)
        chap_data = parse_questions_by_chapter(q_file, ans_map)
        if chap_data:
            export_chapters_to_excel(chap_data)
    
    # New logic for soal_uts.tex
    uts_file = 'soal_uas.tex'
    if os.path.exists(uts_file):
        print(f"Processing {uts_file}...")
        uts_data = parse_uts_data(uts_file)
        if uts_data:
            df = pd.DataFrame(uts_data)
            output_file = "quiz_uas.xlsx"
            try:
                df.to_excel(output_file, index=False, engine='openpyxl')
                print(f"Successfully created: {output_file} with {len(df)} questions.")
            except Exception as e:
                print(f"Error writing to {output_file}: {e}")
        else:
            print("No questions found in soal_uts.tex or parsing failed.")
    else:
        print(f"{uts_file} not found locally.")
