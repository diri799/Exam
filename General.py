general_questions = [
    {
        "question": "Capital of Nigeria?",
        "options": ["a. LAGOS", "b. RIVERS", "c. ABUJA", "d. CHEVRON"],
        "answer": "c"
    },
    {
        "question": "President of Nigeria?",
        "options": ["a. BUHARI", "b. WIKE", "c. TINUBU", "d. ATIKU"],
        "answer": "c"
    },
    {
        "question": "Governor of Lagos?",
        "options": ["a. FASHOLA", "b. AMBODE", "c. OBASANJO", "d. SANWO-OLU"],
        "answer": "d"
    },
    {
        "question": "Largest Ocean in the world?",
        "options": ["a. ATLANTIC", "b. PACIFIC", "c. ARCTIC", "d. INDIAN"],
        "answer": "c"
    },
    {
        "question": "Fastest land animal?",
        "options": ["a. LION", "b. TIGER", "c. CHEETAH", "d. HORSE"],
        "answer": "c"
    },
    {
        "question": "Currency of Nigeria?",
        "options": ["a. DOLLARS", "b. POUNDS", "c. CEDI", "d. NAIRA"],
        "answer": "d"
    },
    {
        "question": "How many States do you have in Nigeria?",
        "options": ["a. 30", "b. 35", "c. 36", "d. 37"],
        "answer": "c"
    },
    {
        "question": "What is the tallest mountain in the world??",
        "options": ["a. MOUNT EVEREST", "b. OLUMO ROCK", "c. KILIMANJARO", "d. MOUNT SINAI"],
        "answer": "a"
    },
    {
        "question": "Which river is the longest in the world?",
        "options": ["a. AMAZON RIVER", "b. RIVER BENUE", "c. RIVER NIGER", "d. RIVER NILE"],
        "answer": "c"
    },
    {
        "question": "Which of the below is not a state in Nigeria?",
        "options": ["a. LAGOS", "b. PORT-HARCOURT", "c. ZAMFARA", "d. ENUGU"],
        "answer": "b"
    }
]

def run_general_exam():
    score = 0
    print("\n--- General Knowledge Exam ---\n")
    for q in general_questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        user_ans = input("Your answer: ").strip().lower()
        if user_ans == q["answer"]:
            score += 1
        print()
    print(f"Your General Knowledge score: {score}/{len(general_questions)}\n")
    return score
