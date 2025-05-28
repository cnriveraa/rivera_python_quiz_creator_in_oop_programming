from python_quiz import Quiz

class QuizCreator:
    def __init__(self):
        super().__init__() # initialize the QuizCreator class
        self.questions = [] # list to hold questions (not used in this class)
        self.answers = {} # dictionary to hold answers (not used in this class)
        self.quiz = Quiz() # create an instance of the Quiz class