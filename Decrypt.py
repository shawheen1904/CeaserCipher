ciphertxt = str(input("What is your encrypted message? "))
plaintext = ""

key = int(input('What is your decryption key? '))

for char in ciphertxt:
    if (char.isupper()):
        plaintext += chr((ord(char) - key - 65) % 26 + 65)
 
    elif (char.islower()):
        plaintext += chr((ord(char) - key - 97) % 26 + 97)
    
    else:
        plaintext += ' '

print(plaintext)
