
plaintext = str(input("What is your seceret message"))
ciphertxt = ""

key = int(input('What is your encryption key?'))

for char in plaintext:
    if (char.isupper()):
        ciphertxt += chr((ord(char) + key - 65) % 26 + 65)
 
    elif (char.islower()):
        ciphertxt += chr((ord(char) + key - 97) % 26 + 97)
    
    else:
        ciphertxt += ' '

print(ciphertxt)
