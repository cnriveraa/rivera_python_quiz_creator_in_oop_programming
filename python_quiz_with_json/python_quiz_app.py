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