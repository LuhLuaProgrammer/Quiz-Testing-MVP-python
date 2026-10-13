def SelectDifficultyFunction():
    print("Welcome to the difficulty Selection")

def ViewQuestionsFunction():
    print("Display all the questions here later")

def QuitFunction():
    print("Goodbye!")

Options = { "quit": QuitFunction,
           "selectdifficulty": SelectDifficultyFunction,
            "viewquestions": ViewQuestionsFunction,
}

#remember indexing starts at 0 in python


# rewrite this whole thing I fucking hate the way I coded this, it's dogshit
def MainMenu():
    print("Welcome to the quiz here are your options")
    for Choice in Options:
        print(Choice) 

    UserChoice = input("> ").lower()

    if UserChoice in Options:
        Options[UserChoice]()
    else:
        print("Try again select an option provided")
        print("\n")
        MainMenu()
        return


MainMenu()