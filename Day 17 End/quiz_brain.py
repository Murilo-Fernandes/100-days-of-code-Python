import os 

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list 

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1  
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")

        self.check_answer(user_answer, question.answer)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            print(f"Your current score is: {self.score}/{self.question_number}")
            print(os.linesep)
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}")
            print(f"Your current score is: {self.score}/{self.question_number}")
            print(os.linesep)
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def quiz_finished(self):
        print("You've completed the quiz!")
        print(f"Your final score was: {self.score}/{self.question_number}")
        print("Thanks for playing!")

    def play_quiz(self):
        while self.still_has_questions():
            self.next_question()
        self.quiz_finished()
