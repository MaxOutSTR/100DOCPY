# class User:
#   def __init__(self, email):
#     self.email = email
#     self.active = True
#     print("New user being created...")
  
#   def report_email(self):
#     print(self.email)

# adam = User("sample@sampleinc.com")

# adam.report_email()

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
  question_bank.append(Question(item["text"], item["answer"]))

quiz_brain = QuizBrain(question_bank)

quiz_brain.next_question()
