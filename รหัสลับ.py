def bon(w):
    w = str(w)
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    for i in range(1, len(w)):
        if w[i] == w[i - 1]:
            number = int(alphabet.find(w[i]))
    return number * 4

### Enter Your Code Here ###
secretCode = input("Enter secret code : ")
print(bon(secretCode))
