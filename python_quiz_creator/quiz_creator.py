from python_quiz import Quiz

class QuizCreator:
    def __init__(self):
        super().__init__() # initialize the QuizCreator class
        self.questions = [] # list to hold questions (not used in this class)
        self.answers = {} # dictionary to hold answers (not used in this class)
        self.quiz = Quiz() # create an instance of the Quiz class

    def create_quiz(self):
        while True:
            question = input("Enter the question (type 'exit' to finish): ") # ask the user for a question
            if question.lower() == 'exit': # check if the user wants to exit
                print("Exiting quiz creator.")
                break

            answers = {}

            for option in ['a', 'b', 'c', 'd']:
                answer = input(f"Enter answer option {option}: ") # ask for answer options
                answers[option] = answer

            correct_answer = input("Enter the correct answer (a/b/c/d): ").lower()

            # validate the correct answer
            if correct_answer not in answers:
                print("Invalid correct answer. Plese enter a valid option (a/b/c/d).")
                continue # restart the loop to ask question again
            
            self.quiz.add_question(question, answers, correct_answer) # add the question and answers to the quiz
            another_question = input("Do you want to add another question? (yes/no): ").lower() # ask if the user wants to add another question

            # check if the user does not want to add another question
            if another_question != 'yes':
                print("Thank you for using the quiz creator!")
                break # end the loop

    # save the quiz to a file
    def save_quiz(self):
        file_name = "quiz_questions.txt" # name of the file to save the quiz
        self.quiz.save_to_file(file_name)
        print(f"Quiz saved to {file_name}") # confirmation message