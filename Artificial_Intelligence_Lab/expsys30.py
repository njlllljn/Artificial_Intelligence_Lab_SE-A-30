from experta import *

class StudentFacts(Fact):
    """Fact class to store student interests."""
    pass

class CareerExpertSystem(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.matched = False  # Track if any rule has fired

    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")
        self.matched = True

    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")
        self.matched = True

    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Chemistry'))
    def biotech(self):
        print("Suggested Career Path: Biotechnology")
        self.matched = True

    @Rule(StudentFacts(likes='Circuits'), StudentFacts(likes='Maths'))
    def electronics(self):
        print("Suggested Career Path: Electronics Engineering")
        self.matched = True

    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Statistics'))
    def ai_datascience(self):
        print("Suggested Career Path: Artificial Intelligence and Data Science")
        self.matched = True

    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='AI Concepts'))
    def ai_ml(self):
        print("Suggested Career Path: Artificial Intelligence and Machine Learning Engineering")
        self.matched = True

def main():
    engine = CareerExpertSystem()
    engine.reset()

    print('''Welcome to the Career Path Expert System!

This expert system is designed to help students discover potential career paths in engineering and science fields based on their academic interests.
By analyzing your areas of interest, the system will suggest career paths that align with your strengths and preferences.

Please enter your interests when prompted, using keywords such as:
            Maths
            Physics
            Chemistry
            Biology
            Programming
            Circuits
            Statistics
            AI Concepts
''')

    interests = input("Enter your interests separated by commas:  ").split(',')
    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))
    engine.run()
    
    if not engine.matched:
        print('''
No specific career suggestion found based on your current interests.

You can try again with a different combination.''')

if __name__ == "__main__":
    main()

