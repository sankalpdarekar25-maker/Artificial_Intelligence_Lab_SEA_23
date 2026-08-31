from experta import *
class StudentFacts(Fact):
    pass
class CareerExpertSystem(KnowledgeEngine):
    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")
    @Rule(StudentFacts(likes='Artificial Intelligence'), StudentFacts(likes='Data Science'))
    def aids(self):
        print("Suggested Career Path: Artificial Intelligence & Data Science Engineering")
    @Rule(StudentFacts(likes='Graphics'), StudentFacts(likes='Maths'))
    def civil(self):
        print("Suggested Career Path: Civil Engineering")
    Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Mechanical'))
    def mechatronix(self):
        print("Suggested Career Path: Mechatronix Engineering")
    Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Circuits'))
    def roai(self):
        print("Suggested Career Path: Robotics & Artificial Engineering")

def main():
    engine = CareerExpertSystem()
    engine.reset()
    print("Welcome to the Career Path Expert System!")
    print("Enter any 2 Subject from the list:\nMaths\nPhysics\nProgramming\nArtificial Intelligence\nData Science\nGraphics\nMechanical\nCircuits")
    interests = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ").split(',')
    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))
    engine.run()
if __name__ == "__main__":
    main()


