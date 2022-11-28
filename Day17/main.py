from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

for i in question_data:
    question_bank.append(Question(i['text'], i['answer']))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
