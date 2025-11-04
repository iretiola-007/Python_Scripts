# List of questions and answers 
questions = [
    ["What is the capital of France? "  "Paris"], 
    ["What is 2 + 2? ", "4"],
    ["Which programming language is this quiz written in? ", "Python"],
    ["Is the sky blue? ", "Yes"],
    ["Who is the current president of Nigeria? (full name in this order-> B. A. T.) ", "Bola Ahmed Tinubu"],
    ["In what year did Nigerua gain her independence? ", "1960"],
    ["When is democracy day in Nigeria(former)? (month date) ", "May 29"]
]

score = 0

# Loop through questions
for q in questions:
    answer = input(q[0] + "")
    if answer.strip().lower() == q[1].lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q[1]}\n")
print("Quiz completed! You scored {score}/{len(questions)}")