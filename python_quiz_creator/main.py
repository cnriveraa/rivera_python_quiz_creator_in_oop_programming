# main execution

from quiz_creator import QuizCreator

if __name__ == "__main__":
    quiz_creator = QuizCreator()  # create an instance of QuizCreator
    quiz_creator.create_quiz()  # start creating the quiz
    quiz_creator.save_quiz()  # save the created quiz to a file