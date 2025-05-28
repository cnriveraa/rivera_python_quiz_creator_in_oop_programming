import json
import random
import os

class BaseQuiz:
    def __init__(self, quiz_output):
        self.quiz_output = quiz_output
        self.questions = self.load_questions()

    def load_questions(self):
        if not os.path.exists(self.quiz_output):
            print(f"Error: File '{self.quiz_output}' does not exist.")
            return []
        
        try:
            with open(self.quiz_output, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('questions', [])
        except json.JSONDecodeError:
            print(f"Error: File '{self.quiz_output}' is not a valid JSON file.")
        return []
    
    def start_quiz(self):
        print("Welcome to the Quiz!")
        
        if not self.questions:
            print("No questions found in the quiz file.")
            return
        
class Question:
    def __init__(self, question_text, answer_text):
        self.question_text = question_text
        self.answer_text = answer_text

    def ask_question(self, question):
        print("Question:")
        print(question.question_text)
        
        user_answer = input("Type your answer: ")

        if question.is_correct(user_answer):
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is: {question.answer_text}")

class Quiz(BaseQuiz):
    def load_questions(self):
        questions_data = super().load_questions()
        return [Question(question['question'], question['answer']) for question in questions_data]
    
    def ask_question(self, question):
        print("Question:")
        print(question.question_text)

        user_answer = input("Type your answer: ").strip()

        if question.answer_text == user_answer:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is: {question.answer_text}")

    def start_quiz(self):
        super().start_quiz()

        while self.questions:
            selected_question = random.choice(self.questions)
            self.ask_question(selected_question)
            self.questions.remove(selected_question)
            continue_quiz = input("Do you want to continue? (yes/no): ").strip().lower()

            if continue_quiz != 'yes':
                print("Thank you for playing!")
                break

        print("Quiz finished!")

class QuizApp:
    def __init__(self, quiz_file_path):
        self.quiz = Quiz(quiz_file_path)

    def run(self):
        self.quiz.start_quiz()

# entry point for the application
if __name__ == "__main__":
    quiz_file_path = r'C:\Users\Chloie Nicole Rivera\OneDrive - Polytechnic University of the Philippines\Desktop\BSCPE 1-6\2ND SEM\[CMPE 103] OOP\python\rivera_python_quiz_creator_in_oop_programming\python_quiz_with_json\quiz_questions.json'
    app = QuizApp(quiz_file_path)
    app.run()