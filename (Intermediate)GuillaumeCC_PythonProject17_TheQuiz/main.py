# Project 17: The Quiz
# Guillaume CC, aka TheFirewallDragon

from questionModel import Question
from data import questionData
from quizBrain import QuizBrain

question_bank = []
for question in questionData:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Thanks for completing that!\nYour final score is: {quiz.score}/{quiz.question_number}")