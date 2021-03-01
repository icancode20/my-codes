def DeEncode(option):
    if Option.lower() == "encode":
        Actmess = input(" What do you want to Encode: ")
        temp = []
        for ch in Actmess.lower():
            temp.append(ord(ch))
        temp[0] += 1

        for i in range(1, len(temp)):  #ry in cry
            temp[i] += temp[(i - 1)]
            while 122 < temp[i]:
                temp[i] -= 26

        for CH in temp:
            print chr(CH)

    elif Option.lower() == "decode":
        Actmess = input(" What do you want to Decode: ")
        prv = 1
        decoed = []
        for i in range (0, len(Actmess)):
            new = ord(Actmess[i])
            new = new - prv
            while new < 97:
                new += 26
            decoed += chr(new)
            prv += new
        print (decoed)
    else:
        return

Option = input("Do you want to Encode or Decode: ")
DeEncode(Option)

