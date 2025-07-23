import sys
import os
import json
from datetime import datetime
from Excel import run_excel_exam, excel_questions
from Python import run_python_exam, python_questions
from General import run_general_exam, general_questions
from Sql import run_sql_exam, sql_questions

def display_welcome():
    print("""
============================================================
        WELCOME TO THE TERMINAL-BASED EXAM SYSTEM
============================================================
Available subjects: Python, SQL, Microsoft Excel, General Knowledge
Each test contains 20 multiple choice questions.
============================================================
""")

def display_rules():
    print("""
================= EXAM RULES =================
1. This is a multiple-choice exam. Read each question carefully.
2. For questions with multiple correct answers, select all that apply (e.g., 'ac').
3. No negative marking for wrong answers.
4. Do not close the terminal during the exam.
5. Your score will be shown after each subject and at the end of the exam.
==============================================
""")

def get_user_info():
    while True:
        name = input("Please enter your name: ").strip()
        if name:
            break
        print("Name cannot be empty. Please try again.")
    user_id = input("Enter your ID: ").strip()
    print(f"\nHello {name}! Let's begin your test.\n")
    return name, user_id

def select_subject(available_subjects):
    print("""
========================================
         SELECT YOUR SUBJECT
========================================
""")
    for key, (subject, _, _) in available_subjects.items():
        print(f"{key}. {subject}")
    while True:
        choice = input("Enter the number of your choice: ").strip()
        if choice in available_subjects:
            return choice
        print("Invalid subject selection. Please enter a number between 1 and 4.")

def grade_and_remark(percentage):
    if percentage >= 90:
        return "A+", "Excellent"
    elif percentage >= 80:
        return "A", "Very Good"
    elif percentage >= 70:
        return "B", "Good"
    elif percentage >= 60:
        return "C", "Satisfactory"
    elif percentage >= 50:
        return "D", "Pass"
    else:
        return "F", "Fail"

def ask_questions(questions):
    score = 0
    total = len(questions)
    for idx, q in enumerate(questions, 1):
        print(f"\nQuestion {idx}/{total}")
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        valid = False
        while not valid:
            user_ans = input("Your answer: ").strip().lower()
            if isinstance(q["answer"], list):
                if all(a in ['a','b','c','d'] for a in user_ans) and user_ans:
                    valid = True
                else:
                    print("Invalid input. Please enter the correct option letters (e.g., ac).")
            else:
                if user_ans in ['a','b','c','d']:
                    valid = True
                else:
                    print("Invalid input. Please enter A, B, C, or D.")
        correct = False
        if isinstance(q["answer"], list):
            if set(user_ans) == set(q["answer"]):
                correct = True
        else:
            if user_ans == q["answer"]:
                correct = True
        if correct:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! Correct answer: {q['answer'] if isinstance(q['answer'], str) else ''.join(q['answer']).upper()}")
        print(f"Current Score: {score}/{idx}")
    return score

def save_results(name, user_id, scores, total_score, average, grade, remark):
    results = {
        "name": name,
        "id": user_id,
        "scores": scores,
        "total_score": total_score,
        "average": average,
        "grade": grade,
        "remark": remark,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    os.makedirs("results", exist_ok=True)
    filename = f"results/{name.replace(' ', '_')}_{user_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    try:
        with open(filename, "w") as f:
            json.dump(results, f, indent=4)
        print(f"\nResults saved to {filename}\n")
    except Exception as e:
        print(f"Error saving results: {e}")

def main():
    try:
        display_welcome()
        display_rules()
        name, user_id = get_user_info()
        scores = {}
        available_subjects = {
            "1": ("Excel", run_excel_exam, excel_questions),
            "2": ("General Knowledge", run_general_exam, general_questions),
            "3": ("Python", run_python_exam, python_questions),
            "4": ("SQL", run_sql_exam, sql_questions)
        }
        taken_subjects = []
        while True:
            choice = select_subject(available_subjects)
            subject_name, exam_func, questions = available_subjects[choice]
            if subject_name in taken_subjects:
                print("You have already taken this subject. Choose another.\n")
                continue
            print(f"\n--- {subject_name} Exam ---\n")
            score = ask_questions(questions)
            print(f"Your {subject_name} score: {score}/{len(questions)}\n")
            scores[subject_name] = score
            taken_subjects.append(subject_name)
            if len(taken_subjects) == len(available_subjects):
                break
            cont = input("Do you want to take another subject? (y/n): ").strip().lower()
            if cont != 'y':
                break
        print(f"\n===== Exam Summary for {name} (ID: {user_id}) =====")
        total_score = sum(scores.values())
        average = total_score / len(available_subjects) if available_subjects else 0
        percentage = (average / 10) * 100  # Each subject is out of 10
        grade, remark = grade_and_remark(percentage)
        for subject, score in scores.items():
            print(f"{subject}: {score}")
        print(f"Total Score: {total_score}")
        print(f"Average: {average:.2f}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")
        print(f"Remark: {remark}")
        print("========================================\n")
        save_results(name, user_id, scores, total_score, average, grade, remark)
    except KeyboardInterrupt:
        print("\n\nExam interrupted by user. Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
