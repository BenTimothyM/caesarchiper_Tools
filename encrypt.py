import string
from time import sleep

alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"

def decrypt():
    print("--------------------------")
    print("|CAESAR CHIPER ENCRYPTION|")
    print("--------------------------")
    print("Write the message you want to encrypt! (lowercase)")
    encrypted_message = input("> ").strip()
    print()
    print("Choose a Key (1-26)!")
    key = int(input("> "))
    
    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c
    print(" ")
    print("##LOCK THE MESSAGE...")
    sleep(2)
    print("##A LITTLE BIT MORE...")
    sleep(2)
    print("-----------------------------------------------------------")
    print("Your Locked Message Is: "+ decrypted_message)
    print("-----------------------------------------------------------")

decrypt()