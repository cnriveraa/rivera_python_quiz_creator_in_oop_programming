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