import json
import random
import os

class BaseQuiz:
    def __init__(self, quiz_output):
        self.quiz_output = quiz_output
        self.questions = self.load_questions()