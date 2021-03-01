import random

def rand_num(A):
    Z = 100
    while Z > 0:
        print ("You have, $", Z,)
        print
        D = input("How much money do you wish to bet? ")
        if 0 < D <= Z:
            B = input("Playing roulette chose between 0 - 36? " )
            C = A[random.randint(0, len(A) - 1)]
            if B > 36 or 0 > B:
                print "Come on! Be in range :)"
                print
            else:
                if B != C:
                    print ("No, You lost your money by", D, "The number the wheel hit was,", C)
                    Z = Z - D
                else:
                    print ("Congrats! You won, ", ((D**2) - 1), "It was your number", C)
                    Z = Z + ((D ** 2) - 1)
                print
        elif D > Z:
            print "You do not have that much money."
            print
        if 0 >= D:
            print "You cannot bet nothing!"
            print
    if Z == 0:
        print "You lost all your money!"

rand_num(range(0, 37))


import random

