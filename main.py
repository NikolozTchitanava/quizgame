from data import get_questions
from question_model import Question
from quiz_brain import QuizBrain

question_data = get_questions()

questions = []
for item in question_data:
    question_text = item['question']
    question_answer = item['correct_answer']
    new_question = Question(question_text, question_answer)
    questions.append(new_question)

quiz = QuizBrain(questions)

while quiz.still_has_questions():
    quiz.next_question()

quiz.game_over()
