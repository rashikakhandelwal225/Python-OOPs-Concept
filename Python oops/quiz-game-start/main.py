from question_model import Question
from data import  question_data
from quiz_brain import  QuizBrain


# question_bank= [
#     Question(q1, a1),
#     Question(q2, a2),
# ]

question_bank = []
for i in range(len(question_data)):
    new_question= Question(question_data[i]["text"] , question_data[i]["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.current_score}/{quiz.question_number}")