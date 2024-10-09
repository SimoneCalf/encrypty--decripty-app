import random
import string

# GET CARACTERS TO USE FOR ENCRYPTION

# characters to use for encryption
caracters = " " + string.punctuation + string.digits + string.ascii_letters

# make a list of all the characters
caracters = list(caracters)

#################################################################################################################################

# CREATE A KEY

# create a key
key = caracters.copy()

# shuffle the key
# everythime you run the program the key will be different
random.shuffle(key)


#print(f"caracters: {caracters}")
#print(f"key      : {key}")

#################################################################################################################################

# ENCRYPT A MESSAGE

# original message
original_message = input("Enter a message that you want to encrypt: ")

# encrypted message
encrypted_message = ""


# encryt the original message
for letter in original_message:
    # find the index of the letter in the characters list
    index = caracters.index(letter)
    # find the letter at that index in the key
    encrypted_message += key[index]

print(f'original message: {original_message}')
print(f"Encrypted message: {encrypted_message}")

#################################################################################################################################

# DECRYPT A MESSAGE

# ask if the user wants to decrypt the message
message_to_decrypt = input("Enter a message you want to decrypt: ")


# decrypted message
decrypted_message = ""

# decrypt the encrypted message
for letter in message_to_decrypt:
    # find the index of the letter in the key
    index = key.index(letter)
    # find the letter at that index in the characters list
    decrypted_message += caracters[index]

print(f"Decrypted message: {decrypted_message}")


