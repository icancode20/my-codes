message = input("Enter a message to code or Decode: ")
key = input("Enter a key value form 1-26: ")
message = message.upper()
O = ("")
for L in message:
    if L.isupper():
        value = ord(L) + key
        L = chr(value)
        if not L.isupper():
            value -= 26
            L = chr(value)
    O += L
print ("Output Message: ", O)
H = abs(key - 26)
print ("The Decoder / Encoder Key is: ", H)
