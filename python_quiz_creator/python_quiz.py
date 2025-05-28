class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question, answers, correct_answer):
        self.questions.append({
            'question': question,
            'answers': answers,
            'correct_answer': correct_answer
        })