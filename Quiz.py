Options = [
    "Quit",
    "SelectDifficulty",
    "ViewQuestions"
]

def SelectDifficultyFunction():
    print("Select the difficulty")

def ViewQuestionsFunction():
    print("Display all the questions here later")

#remember indexing starts at 0 in python

def MainMenu():
    print("Welcome to the quiz I made this to test how an MVP version of this would work what would you like to do")
    for Choice in Options:
        print(Choice)

    print(Options[1])
    UserChoice = input()
    for Selection in Options:
        if str.lower(UserChoice) == str.lower(Selection):
            print(Selection)
            print("test does this work")
            if str.lower(UserChoice) == str.lower(Options[0]):
                print("Goodbye!")
                return
            elif str.lower(UserChoice) == str.lower(Options[1]):
                SelectDifficultyFunction()
                return
            elif str.lower(UserChoice) == str.lower(Options[2]):
                ViewQuestionsFunction()
                return
    print("Try again you need to select an option provided by typing it in")
    MainMenu()
    return  


MainMenu()