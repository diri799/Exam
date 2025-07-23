excel_questions = [
    {
        "question": "Which Excel feature allows you to find duplicates?",
        "options": ["a. Conditional Duplicate", "b. Remove Duplicate", "c. Flash Fill", "d. Sort"],
        "answer": "b"
    },
    {
        "question": "What does the “Freeze Panes” option do?",
        "options": ["a. Makes formulas visible", "b. Hides rows", "c. Splits the worksheet", "d. Locks rows/columns in view"],
        "answer": "d"
    },
    {
        "question": "Which shortcut key is used to copy in Excel?",
        "options": ["a. Ctrl + X", "b. Ctrl + V", "c. Ctrl + C", "d. Ctrl + A"],
        "answer": "c"
    },
    {
        "question": "Which function removes extra spaces from text?",
        "options": ["a. =TEXT()", "b. =CLEAN()", "c. =REMOVE()", "d. =TRIM()"],
        "answer": "d"
    },
    {
        "question": "What does conditional formatting allow you to do? (Select all that apply)",
        "options": ["a. Highlight values above or below average", "b. Change font", "c. Change cell color based on values", "d. Automatically format dates"],
        "answer": ["a", "c"]
    },
    {
        "question": "Which function is used to find the average of a range in Excel?",
        "options": ["a. =AVERAGE()", "b. =MEAN()", "c. =SUM()", "d. =MEDIAN()"],
        "answer": "a"
    },
    {
        "question": "What happens if you enter =A1+A2 in cell A3?",
        "options": ["a. Adds values of A1 and A2", "b. Concatenates A1 and A2", "c. Displays an error", "d. Merges A1 and A2"],
        "answer": "a"
    },
    {
        "question": "Which function counts only numeric values?",
        "options": ["a. =COUNTA()", "b. =COUNTIF()", "c. =COUNTBLANK()", "d. =COUNT()"],
        "answer": "d"
    },
    {
        "question": "Which Excel function is used to look up a value in a table?",
        "options": ["a. =SEARCH()", "b. =VLOOKUP()", "c. =FIND()", "d. =MATCH()"],
        "answer": "b"
    },
    {
        "question": "How can you filter data in Excel?",
        "options": ["a. View > Filter", "b. Insert > Filter", "c. Home > Format > Filter", "d. Data > Filter"],
        "answer": "d"
    }
]

def run_excel_exam():
    score = 0
    print("\n--- Excel Exam ---\n")
    for q in excel_questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        if isinstance(q["answer"], list):
            user_ans = input("Your answer (select all that apply, e.g. ac): ").strip().lower()
            user_ans_set = set(user_ans)
            correct_set = set(q["answer"])
            if user_ans_set == correct_set:
                score += 1
        else:
            user_ans = input("Your answer: ").strip().lower()
            if user_ans == q["answer"]:
                score += 1
        print()
    print(f"Your Excel score: {score}/{len(excel_questions)}\n")
    return score
