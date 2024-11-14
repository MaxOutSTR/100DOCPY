class QuizBrain:
  def __init__(self, q_list):
    self.question_number = 0
    self.questions_list = q_list

  def still_have_questions(self):
    total_questions = len(self.questions_list)
    return self.question_number < total_questions

  def check_answer(self, u_answer, c_answer):
    return u_answer.lower() == str(c_answer).lower()

  def next_question(self):
    result = self.questions_list[self.question_number]
    answer = input(f"Q. {result.text} (True/False): ")
    if self.check_answer(answer, result.answer):
      self.question_number += 1
      if not self.still_have_questions():
        print(f"You answered all {len(self.questions_list)} questions. You WIN!")
      else:
        self.next_question()
    else:
      print(f"Game Over, you got {self.question_number} questions right.")
