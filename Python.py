python_questions = [
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": ["a. ^", "b. //", "c. **", "d. %"],
        "answer": "c"
    },
    {
        "question": "Which of these is a valid variable name in Python?",
        "options": ["a. _value2", "b. 2value", "c. my-variable", "d. value@1"],
        "answer": "a"
    },
    {
        "question": "what will print(\"hello\". upper()) output?",
        "options": ["a. Hello", "b. HELLO", "c. H E L L O", "d. hello"],
        "answer": "b"
    },
    {
        "question": "what is the output of print(type(10))?",
        "options": ["a. <class 'bool'>", "b. <class 'str'>", "c. <class 'int'>", "d. <class 'float'>"],
        "answer": "c"
    },
    {
        "question": "What will len(\"python\") return?",
        "options": ["a. Error", "b. 7", "c. 5", "d. 6"],
        "answer": "d"
    },
    {
        "question": "What is the output of: print(\"2\"+ \"2\")?",
        "options": ["a. 2+2", "b. Error", "c. 22", "d. 4"],
        "answer": "c"
    },
    {
        "question": "Which of the following is a loop in python? (select all that apply)",
        "options": ["a. Loop", "b. Do", "c. For", "d. while"],
        "answer": ["c", "d"]
    },
    {
        "question": "What happens if you divide by zero in python?",
        "options": ["a. Error", "b. Returns None", "c. Returns 0", "d. Infinity"],
        "answer": "a"
    },
    {
        "question": "Which operator is used for exponentiation in python?",
        "options": ["a. ^", "b. //", "c. **", "d. %"],
        "answer": "c"
    },
    {
        "question": "Which of these is a valid variable name in python?",
        "options": ["a. _value2", "b. 2value", "c. My-variable", "d. value@1"],
        "answer": "a"
    }
]

def run_python_exam():
    score = 0
    print("\n--- Python Exam ---\n")
    for q in python_questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        if isinstance(q["answer"], list):
            user_ans = input("Your answer (select all that apply, e.g. cd): ").strip().lower()
            user_ans_set = set(user_ans)
            correct_set = set(q["answer"])
            if user_ans_set == correct_set:
                score += 1
        else:
            user_ans = input("Your answer: ").strip().lower()
            if user_ans == q["answer"]:
                score += 1
        print()
    print(f"Your Python score: {score}/{len(python_questions)}\n")
    return score
