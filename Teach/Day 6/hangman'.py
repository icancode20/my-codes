import random

Lives = ["9 Chances Remaining", "8 Chances Remaining", "7 Chances Remaining", "6 Chances Remaining", "5 Chances Remaining", "4 Chances Remaining", "3 Chances Remaining", "2 Chances Remaining", "1 Chance Remaining"]

words = ["ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "clam", "cobra", "cougar", "coyote", "crow", "deer", "dog", "donkey", "duck", "eagle", "fox", "frog", "hawk", "lion", "lizard", "llama", "monkey", "mule", "owl", "pigeon", "rabbit", "rat", "rhino", "shark", "sheep", "spider", "swan", "turtle", "whale", "wolf", "zebra"]

A = random.randint(0, len(words) - 1)

C = ""
E = ""
F = words[A]
W = False

def displayBoard(Lives, C, E, F):
    print(Lives[len(C)])
    print
    print('Missed letters:')
    for H in C:
        print(H)
    print

    blanks = '_' * len(F)

    for i in range(len(F)):
        if F[i] in E:
            blanks = blanks[:i] + F[i] + blanks[i+1:]

    print(blanks)
    print

def getGuess(g):
    while True:
        G = input("Guess a letter?" )
        G = G.lower() # TRUE = true
        if len(G) != 1:
            print('Please enter a !single! letter.')
        elif G in g:
            print('You have already guessed that letter.')
        elif G not in 'abcdefghijklmnopqrstuvwxyz':
            print('Dude enter a !LETTER!!!.')
        else:
            return G

while True:
    displayBoard(Lives, C, E, F)
    y = getGuess(C + E)

    if y in F:
        E = E + y
        N = True
        for i in range(len(F)):
            if F[i] not in E:
                N = False
        if N == True:
            print("Congrats! The secret word is ", F)
            W = True
    else:
        C = C + y
        if len(C) == len(Lives) - 1:
            print("You have run out of guesses! The word was ", F)
            W = True

    if W == True:
        C = ""
        E = ""
        W = False
        F = words[A]