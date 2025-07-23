sql_questions = [
    {
        "question": "What SQL keyword retrieves data?",
        "options": ["a. GET", "b. SELECT", "c. EXTRACT", "d. FETCH"],
        "answer": "b"
    },
    {
        "question": "How do you prevent duplicates?",
        "options": ["a. UNIQUE", "b. DISTINCT", "c. GROUP BY", "d. FILTER"],
        "answer": "b"
    },
    {
        "question": "Which clause filters rows?",
        "options": ["a. WHERE", "b. HAVING", "c. ORDER BY", "d. LIMIT"],
        "answer": "a"
    },
    {
        "question": "What joins tables?",
        "options": ["a. JOIN", "b. CONNECT", "c. LINK", "d. MERGE"],
        "answer": "a"
    },
    {
        "question": "SQL stands for?",
        "options": ["a. Simple Query Language", "b. Sequential Query Language", "c. Structured Quick Language", "d. Structured Query Language"],
        "answer": "d"
    },
    {
        "question": "Which function is used to find number of rows in a table?",
        "options": ["a. SUM()", "b. COUNT()", "c. AVG()", "d. MAX()"],
        "answer": "b"
    },
    {
        "question": "What type of JOIN returns all rows from the left table and matching rows from the right table?",
        "options": ["a. INNER JOIN", "b. RIGHT JOIN", "c. LEFT JOIN", "d. FULL JOIN"],
        "answer": "c"
    },
    {
        "question": "Which SQL function returns the current date and time?",
        "options": ["a. TODAY()", "b. NOW()", "c. DATE()", "d. CURRENT()"],
        "answer": "b"
    },
    {
        "question": "What keyword is used to group rows in SQL?",
        "options": ["a. GROUP BY", "b. JOIN", "c. MERGE", "d. CONNECT"],
        "answer": "a"
    },
    {
        "question": "What SQL keyword is used to sort results",
        "options": ["a. GROUP BY", "b. ORDER BY", "c. SORT BY", "d. FILTER BY"],
        "answer": "b"
    }
]

def run_sql_exam():
    score = 0
    print("\n--- SQL Exam ---\n")
    for q in sql_questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        user_ans = input("Your answer: ").strip().lower()
        if user_ans == q["answer"]:
            score += 1
        print()
    print(f"Your SQL score: {score}/{len(sql_questions)}\n")
    return score
