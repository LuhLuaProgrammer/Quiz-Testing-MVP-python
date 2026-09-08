Options = [
    "Quit",
    "SelectDifficulty",
    "ViewQuestions"
]

def MainMenu():
    print("Welcome to the quiz I made this to test how an MVP version of this would work what would you like to do")
    for Choice in Options:
        print(Choice)

    UserChoice = input()
    for Selection in Options:
        if str.lower(UserChoice) == str.lower(Selection):
            print(Selection)
        else:
            print("Try again you need to select an option provided by typing it in")
            MainMenu()
            return


MainMenu()