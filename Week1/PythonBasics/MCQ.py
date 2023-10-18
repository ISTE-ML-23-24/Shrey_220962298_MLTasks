from Question import Question
que_prompts=[
    "What color are apples?\n(A)Red/Green\n(B)Purple\n(C)Orange\n\n",
    "What color are Bananas?\n(A)Red/Green\n(B)Yellow\n(C)Orange\n\n",
    "What color are oranges?\n(A)Red/Green\n(B)Purple\n(C)Orange\n\n"
]
questions=[
    Question(que_prompts[0],"A"),
    Question(que_prompts[1],"B"),
    Question(que_prompts[2],"C")
]

def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1
    print("You got "+str(score)+"!")

run_test(questions)