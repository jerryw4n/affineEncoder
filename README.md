# Affine Cipher Encryption Tool

This repository provides a Python implementation of the affine cipher for encryption. The affine cipher is a type of substitution cipher where each letter in the plaintext is transformed based on a mathematical formula using two keys: `a` (multiplicative key) and `b` (additive key).

## Functions

### 1. `letterToIndex(letter)`
Converts a letter to its corresponding index in the alphabet.

- **Parameters:**
  - `letter` (char): The letter to convert.
  
- **Returns:**
  - The index (int) of the letter in the alphabet (0-25).

### 2. `indexToLetter(index)`
Converts an index (0-25) back to the corresponding letter of the alphabet.

- **Parameters:**
  - `index` (int): The index to convert.

- **Returns:**
  - The corresponding letter (char) at that index in the alphabet.

### 3. `encrypt(plaintext, a, b)`
Encrypts a given plaintext using the affine cipher formula.

- **Parameters:**
  - `plaintext` (string): The message to be encrypted (must be in lowercase).
  - `a` (int): The multiplicative key used in the encryption.
  - `b` (int): The additive key used in the encryption.

- **Returns:**
  - `ciphertext` (string): The encrypted message.

- **Encryption Steps:**
  1. Each letter in the plaintext is converted to its index in the alphabet.
  2. The affine cipher formula `(a * index + b) % 26` is applied to calculate the new index.
  3. The resulting index is converted back into a letter, forming the ciphertext.

### Example
```bash
Enter the sentence you want to encode (lowercase): hello
Plaintext: hello
Encrypted: mdwwz
