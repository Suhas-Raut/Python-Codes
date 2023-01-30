from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain
# Created Empty List
question_bank = []

# Assign The Text and Question to a list by using class.
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Questions(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've Completed The Quiz.")
print(f"Your Final Score Is: {quiz.score}/{quiz.question_number}")