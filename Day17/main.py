from data import question_data
from question_model import Question

question_bank = []

for i in question_data:
    question_bank.append(Question(i['text'], i['answer']))

print(question_bank[0].text)
