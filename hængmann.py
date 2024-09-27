word = "oslo"
wordlengthint = int(len(word))
word.upper()
guesses = ""

wordIsFound = False
while wordIsFound == False:
    print("Hele ordet har " + str(wordlengthint) + " tegn")

    guess = input()

    guesses += guess

    if len(guesses) == 1:
        print("|¨¨¨¨¨¨¨¨¨\n|\n|\n|\n")
    
    if len(guesses) == 2:
        print("|¨¨¨¨|¨¨¨¨\n|   ---   \n|  |   |\n|   ---   \n")

    if len(guesses) == 3:
        print("|¨¨¨¨|¨¨¨¨\n|   ---   \n|  |   |\n|   ---   \n|    |\n     | \n   ------  \n Du e dævv")
        wordIsFound = True

    for char in word:
        if char in guesses: 
            print(char)

        else: 
            print("_")