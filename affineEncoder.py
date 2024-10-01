import string

# Define the ASCII values for lowercase letters
ASCII = string.ascii_lowercase

# Gives the letter of the alphabet at the given index
def letterToIndex(letter):
		return ASCII.index(letter)

# Gives the index of the letter in the alphabet
def indexToLetter(index):
		return ASCII[index]

# Function used for affine cipher
def encrypt(plaintext, a, b):
		# Inputs the encoded messsage into this value each time the loop is ran
		ciphertext = ""
		# Loop each letter in the plaintext and encode it one by one
		for letter in plaintext:
				if letter in ASCII:
						x = letterToIndex(letter)
						encrypted_index = (a * x + b) % len(ASCII)
						ciphertext += indexToLetter(encrypted_index)
				else:
						ciphertext += letter
		return ciphertext

# Asks for user input for what they want to encrypt
plainText = input("Enter the sentence you want to encode (lowercase): ")

# Key values for affine cipher
a = 17
b = 15  

# Converts user input to lowercase if uppercase was inputted
convertedText = [x.lower() for x in plainText]

# Message is then encrypted by invoking all of the functions above
encrypted = encrypt(convertedText, a, b)

# Print the encrypted message and user input
print("")
print(f"Plaintext: {plainText}")
print(f"Encrypted: {encrypted}")