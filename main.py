from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

#question bank comres from data
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#creates a quiz object from the QuizBrain class
quiz = QuizBrain(question_bank)

#takes in the quiz object to create a quiz ui object
quiz_ui = QuizInterface(quiz)

#while quiz.still_has_questions():
#   quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


