import random
import time
face = ['clubs','diamonds','hearts','spades']
number = [ 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
hands = 0
ties = 0
Player = 0
Computer = 0
while hands < 52:
    hands += 1
    Pnum = random.choice(number)
    Pface = random.choice(face)
    Cnum = random.choice(number)
    Cface = random.choice(face)
    print ("I have the", Pnum, "of", Pface)
    print ( "you have the", Cnum, "of", Cface)
    time.sleep(1)
    if face.index(Pface) < face.index(Cface):
        print ("I win!")
        Player += 1 + ties
        ties = 0
    elif face.index(Cface) < face.index(Pface):
        print ("You win!")
        Computer += 1 + ties
        ties = 0
    else:
        if number.index(Pnum) > number.index(Cnum):
            print ("I win!")
            Player += 1 + ties
            ties = 0
        elif number.index(Cnum) > number.index(Pnum):
            print ("You win!")
            Computer += 1 + ties
            ties = 0
        else:
            print ("It's a tie ")
            ties += 1
    print ("Score: Computer", Computer, "Score: Player", Player)
    time.sleep(5)

