class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question, answers, correct_answer):
        self.questions.append({
            'question': question,
            'answers': answers,
            'correct_answer': correct_answer
        })

    def save_to_file(self, file_name):
        with open(file_name, 'w') as file:
            for question in self.questions:
                file.write(f"Q: {question['question']}\n")
                for key, answer in question['answers'].items():
                    file.write(f"{key}: {answer}\n")
                file.write(f"Correct Answer: {question['correct_answer']}\n")
                file.write("\n")