import random
import time
def displayIntro():
    HP = 100
    attack = 10
    defence = 5
    day = 1
    print("You are an Immortal Adventurer. Every day you Explore from a choise of 4 areas.")
    time.sleep(1.5)
    print("You know tha two of these areas, Will require you to fight with monster's")
    time.sleep(1.5)
    print("One will be a Pure Mana Area that will add your attack or defence or HP,")
    time.sleep(1.5)
    print("While the remaining one is a Highly Mana Polluted are and will decrease your attack or/and defence.")
    time.sleep(1.5)
    print("You will always reset your HP.")
    time.sleep(1.5)
    print
    while True:
        print ("Day:", day)
        print ("Max Attack:", attack)
        print ("Max Defence:", defence)
        print ("HP:", HP)
        print
        time.sleep(1)

        if attack == 0 and defence == 0:
            print ("You cannot progress any futher as you attack and defence is 0, so you restart!")
            day = 1
            attack = 10
            defence = 5
            HP = 100

        E = [1, 2, 3, 4]
        incrarea = E[random.randint(0, len(E) - 1)]
        E.remove(incrarea)

        decrarea = E[random.randint(0, len(E) - 1)]
        E.remove(decrarea)

        moarea = E[random.randint(0, len(E) - 1)]
        E.remove(moarea)

        monarea = E[random.randint(0, len(E) - 1)]
        E.remove(monarea)

        area = input('Which area will you go into? (1 - 4)')
        day += 1

        print("You approach the area...")
        time.sleep(1)
        print

        typeaw = ["Attack", "Defence", "HP"]
        awapen = typeaw[random.randint(0, len(typeaw) - 1)]

        if area == incrarea:
            if awapen == "Attack":
                attack += 16
            elif awapen == "Defence":
                defence += 10
            elif awapen == "HP":
                HP += 20
            print("You chose the High Density Mana area, your", awapen, "will be changed correspondingly.")
            print
            time.sleep(1)

        elif area == decrarea:

            if awapen == "Attack":

                if attack >= 3:
                    attack -= 3
                    print("You chose the Normal Mana Polluted area! Your Attack will be changed by 3.")
                    print

                elif attack < 3:
                    attack = 0
                    print ("You chose the Normal Mana Polluted area! Your Attack will be changed to 0.")
                    print

                elif defence >= 2 and attack == 0:
                    defence -= 2
                    print("Your defence is decreased by 2.")
                    print

                elif defence < 2 and attack == 0:
                    defence = 0
                    print(" Your defence is decreased to 0")
                    print

            elif awapen == "Defence":
                if defence >= 3:
                    defence -= 3
                    print("You chose the Normal Mana Polluted area! Your Defence will be changed by 3.")

                elif defence < 3:
                    defence = 0
                    print("You chose the Normal Mana Polluted area! Your Defence will be changed to 0.")

                elif attack >= 3 and defence == 0:
                    attack -= 3
                    print("You chose the Normal Mana Polluted area! Your Attack will be changed by 3.")

                elif attack < 3 and defence == 0:
                    attack = 0
                    print("You chose the Normal Mana Polluted area! Your Attack will be changed to 0.")
                print

            elif awapen == "HP":
                if attack >= 3 and defence >= 1:
                    attack -= 3
                    defence -= 1
                elif attack < 3 and defence >= 1:
                    attack = 0
                    defence -= 1
                elif attack >= 3 and defence < 1:
                    attack -= 3
                    defence = 0
                elif attack < 3 and defence < 1:
                    attack = 0
                    defence = 0
                print("You chose the High Mana Polluted area! Your Attack and Defence will be changed by 3 and 1 perspectively.")
                print
            time.sleep(1)

        elif area == moarea:
            teHP = HP
            moatk = ((5 + (HP//8) + defence))
            moHP = (100 + attack * 4)
            print("The Area has a Monster! You use appraisal to see that His Max Attack is", moatk, "and his HP is", moHP)
            time.sleep(2)
            print ("Fight!")

            while teHP >= 0 and moHP >= 0:
                teatk = random.randint(1, (attack + 5))
                if teatk > 0:
                    moHP -= teatk
                    if teatk <= attack:
                        print ("You deal", teatk, " Damage. Leaving his HP at", moHP)
                    if attack < teatk:
                        print ("You deal", (teatk + 4), " critical Damage. Leaving his HP at", (moHP - 4))
                        moHP -= 4
                    print
                    time.sleep(2)

                if defence > 3:
                    tedef = random.randint(-2, defence)
                    temoatk = random.randint(0, moatk)
                    if tedef > 0:
                        temoatk -= tedef
                else:
                    temoatk = random.randint(1, moatk)

                if temoatk > 0:
                    teHP -= temoatk
                    print ("He deal's you", temoatk, " Damage. Leaving your HP at", teHP)
                    print
                    time.sleep(2)

            if teHP <= 0:
                print ("You Died! No.. You have to restart")
                day = 1
                attack = 10
                defence = 5
                HP = 100
                time.sleep(2)
            elif moHP <= 0:
                print ("!You killed the monster!")
                print ("You gained experience from that fight your attack and defence go up by 2")
                attack += 2
                defence += 2
                time.sleep(2)

        elif area == monarea:
            teHP = HP
            moatk = (5 + (HP // 6) + (defence//2))
            moHP = (100 + attack * 3)
            print(
            "The Area has a High Monster! You use appraisal to see that His Max Attack is", moatk, "and his HP is", moHP)
            time.sleep(1)
            print ("Fight!")
            while teHP >= 0 and moHP >= 0:
                if defence > 3:
                    temodef = random.randint(-6, defence)
                    teatk = random.randint(0, (attack + 2))
                    if temodef > 4:
                        temoatk -= temodef
                else:
                    teatk = random.randint(0, (attack + 2))
                if teatk > 0:
                    moHP -= teatk
                    if attack >= teatk:
                        print ("You deal", teatk, " Damage. Leaving his HP at", moHP)
                    if teatk > attack:
                        print ("You deal", (teatk + 20), " Critical Damage. Leaving his HP at", (moHP - 20))
                        moHP -= 20
                    print
                    time.sleep(2)

                if defence > 3:
                    tedef = random.randint(-5, defence)
                    temoatk = random.randint(0, moatk)
                    if tedef > 4:
                        temoatk -= tedef
                else:
                    temoatk = random.randint(1, moatk)

                if temoatk > 0:
                    teHP -= temoatk
                    print ("He deal's you", temoatk, " Damage. Leaving your HP at", teHP)
                    print
                    time.sleep(2)
            time.sleep(2)
            if teHP <= 0:
                print ("You Died! No.. You have to restart")
                day = 1
                attack = 10
                defence = 5
                HP = 100
                time.sleep(2)
            elif moHP <= 0:
                print ("!You killed the monster!")
                print ("You gained experience from that fight your attack, defence and HP go up by 10")
                attack += 10
                defence += 10
                Hp += 10
                time.sleep(1)

displayIntro()