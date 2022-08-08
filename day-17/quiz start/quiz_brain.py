class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_q(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.({self.question_number}: {current_q.text} (True/False): ")
        self.check_ans(user_ans, current_q.answer)

    def check_ans(self, user_ans, correct_answer):
        if user_ans.lower() == correct_answer.lower():
            self.score += 1
            print("You are right")

        else:
            print("You are wrong")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is:{self.score}/{self.question_number}")
        print("\n")
