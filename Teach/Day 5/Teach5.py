import random

def rps(A):
    Z = "yes"
    while Z == "yes":
        B = input("What do you choose? " )
        C = A[random.randint(0, len(A)-1)]
        print ("Computer chooses,", C)

        if B.lower() == C:
            print "Oh.. It's a tie"

        if B.lower() == "rock":
            if C == "paper":
                print "Ting. Ting. Computer wins"
            elif C == "scissor":
                print "Ting. Ting. Player wins"

        elif B.lower() == "paper":
            if C == "rock":
                print "Ting. Ting. Player wins"
            elif C == "scissor":
                print "Ting. Ting. Computer wins"

        elif B.lower() == "scissor":
            if C == "paper":
                print "Ting. Ting. Player wins"
            elif C == "rock":
                print "Ting. Ting. Computer wins"

        Z = input("Do you want to play again? ")
        print ()

rps(['rock', 'paper', 'scissor'])
