class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, correct, user_ans):
        return correct.lower() == user_ans.lower()

    def next_question(self):
        current_question_text = self.question_list[self.question_number]
        correct_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        choice = input(f"Q.{self.question_number} {current_question_text.text} (True/False): ")

        if self.check_answer(correct_answer, choice):
            print("You are corrct.")
            self.score += 1
        else:
            print("Sorry, wrong answer")
        print(f"The correct answer is '{correct_answer}'")
        print(f"Your currant score {self.score}/{self.question_number}\n")
