import random

wordList = ('apple', 'albumen', 'toothpaste', 'enthusiastic')

word = random.choice(wordList)

letter_guess = ""

word_guess = ""

store_letter = ""

count = 1

limit = 5

countLetters = len(word)

choice1 = ("Do you want to spell the word now? (y/n):")

choice2 = ("Spell another word? (y/n):")

choiceY = ("y")

choiceN = ("n")



startGame = print("The word ________ has {} letters. Spell it in 5 tries.".format(countLetters))

while count < limit:
    letter_guess = input("Try {} - Current: ________. Your guess? ".format(count))

    if letter_guess in word:
        print ("yes")
        print (input(choice1))

    else :
        print("no")
        count += 1

    if choice1 == choiceY:
        print (input("Spell the complete word: "))

    else:
        print (letter_guess)
        store_letter += letter_guess
        count += 1


while count == limit:
    spellFinal = input("Spell the complete word: ")

    if spellFinal in word:
        print ("You are correct!")
        print ("Spell another word? (y/n):")

    if choice == "y":
        print (startGame)

    else:
        print('Remaining Words are: ', store_letter)

    if spellFinal not in word:
        print ("You are incorrect")
        print ("The correct word is {}.".format(correct))
