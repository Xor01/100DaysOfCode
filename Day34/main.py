# Trivial Quiz Game OOP GUI data from API
from question_model import Question
from data import question_data
from ui import *

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
window = QuizInterface(quiz)
