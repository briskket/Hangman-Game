import random
import sys
import time
import os
#Hangman Game Try again with a new word?:
#Variable for obfuscateWord() will be called hidden
#Lives: 5, 
wordList = "character make confront office dump aisle bike garage understanding makeup guideline tooth native commission request cheque society physical econobox voucher buffet nightmare groan widen freshman elite lick security secretion uncertainty rotate dictate ghostwriter constellation cheat belly serious fund angle variable inflation meal subway ostracize trip grain variant"
finWordList = wordList.split()

def clearScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def userChoice():
    while True:
        try:
            userChoice = int(input(""))
        except ValueError:
            print("Please enter a valid choice")
        else:
            if userChoice in range(1, 3):
                return userChoice
                break
            else:
                print("Please enter a valid choice")

def getWord():
    global theWord
    theWord = random.choice(finWordList)

def obfuscateWord(theWord):
    amountOfChars = len(theWord)
    replaced = "_" * amountOfChars
    replaced = list(replaced)
    return replaced

def userInput():
    while True:
        userAnswer = input("Enter your guess: ")
        if len(userAnswer) == 1:
            return userAnswer
            break
        else:
            print("Please answer with 1 character")

def checkRepeat(letter):
    letter = letter.lower()
    if letter in guessedLetters:
        return True   
    else:
        guessedLetters.add(letter)
        return False  

def checkAnswer(userAnswer, replaced, userLives):
    correct_guesses = list(theWord)
    isRepeat = checkRepeat(userAnswer)
    if isRepeat == False:
        if userAnswer.lower() in correct_guesses:
            indexPos = [index for index, value in enumerate(correct_guesses) if value == userAnswer.lower()]
            for i in range(len(indexPos)):
                replaced[indexPos[i]] = userAnswer.lower()
                guess = True
        else:
            print("Incorrect")
            userLives = userLives - 1
            return replaced, userLives

        if guess == True:
            print(replaced)
            return replaced, userLives

    elif isRepeat == True:
        print("You have already guessed this letter")
        return replaced, userLives




def checkIfGameDone(numOfLives, hiddenWord):
    if numOfLives == 0:
        print("Out of lives")
        time.sleep(1)
        clearScreen()
        return True
    elif "_" not in hiddenWord:
        print("Well done!, you have found the hidden word!")
        time.sleep(1)
        clearScreen()
        
        return True
    else:
        return False

def main():
    while True:
        print("     Hangman     \n  1.Start a new game  \n  2.Exit Program  ")
        picked = userChoice()
        if picked == 1:
            global guessedLetters
            time.sleep(0.5)
            clearScreen()
            userLives = 5
            getWord()
            replacedWord = obfuscateWord(theWord)
            guessedLetters = set() 
            while True:
                userAnswer = userInput()
                replacedWord, userLives = checkAnswer(userAnswer, replacedWord, userLives)
                if checkIfGameDone(userLives, replacedWord) == True:
                    break
        elif picked == 2:
            sys.exit()
            


main()


