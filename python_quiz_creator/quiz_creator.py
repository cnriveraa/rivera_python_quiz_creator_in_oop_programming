from python_quiz import Quiz

class QuizCreator:
    def __init__(self):
        super().__init__() # initialize the QuizCreator class
        self.questions = [] # list to hold questions (not used in this class)
        self.answers = {} # dictionary to hold answers (not used in this class)
        self.quiz = Quiz() # create an instance of the Quiz class

    def create_quiz(self):
        while True:
            question = input("Enter the question (type 'exit' to finish): ")
            if question.lower() == 'exit':
                break

            answers = {}

            for option in ['a', 'b', 'c', 'd']:
                answer = input(f"Enter answer option {option}: ")
                answers[option] = answer

            correct_answer = input("Enter the correct answer (a/b/c/d: ").lower()

            if correct_answer not in answers:
                print("Invalid correct answer. Plese enter a valid option (a/b/c/d).")
                continue
            
            self.quiz.add_question(question, answers, correct_answer)
            another_question = input("Do you want to add another question? (yes/no): ").lower()

            if another_question != 'yes':
                print("Thank you for using the quiz creator!")
                break