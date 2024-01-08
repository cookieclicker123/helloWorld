def newGame():
    
    guesses = []
    correctGuesses = 0
    questionNum = 1

    for key in questions:
        print("---------------------------")
        print(key)
        for i in options[questionNum - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)

        correctGuesses += checkAnswer(questions.get(key), guess)
        questionNum += 1
    
    displayScore(correctGuesses, guesses)


def checkAnswer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def displayScore(correctGuesses, guesses):
    print("---------------------------")
    print("RESULTS")
    print("---------------------------")
    
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correctGuesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")




def playAgain():
    response = input("Do you want to play again? (Yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


questions = {
    "Who created python?: ":"A",
    "What year was python created?: ":"B",
    "Python is tributed to which comedy group?: ":"C",
    "Is the Earth round?: ":"A"
}

options =   [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
            ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
            ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
            ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]

newGame()

while playAgain():
    newGame()

print("Goodbye")

