class Quiz:
    def __init__(self):
        self.questions = []  # list to hold questions

    def add_question(self, question, answers, correct_answer):
        # add a new question with its answers and correct answer to the quiz
        self.questions.append({
            'question': question,
            'answers': answers,
            'correct_answer': correct_answer
        })

    def save_to_file(self, file_name):
        # save the questions and answers to a text file
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                for question in self.questions:
                    file.write(f"Q: {question['question']}\n")  # write the question
                    for key, answer in question['answers'].items():
                        file.write(f"{key}: {answer}\n")  # write the answers
                    file.write(f"Correct Answer: {question['correct_answer']}\n")  # write the correct answer
                    file.write("\n")  # add a new line for separation between questions
        except:
            print(f"An error occurred while saving the file.")