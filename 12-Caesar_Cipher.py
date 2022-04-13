# function for converting a plain word into it's ceaser cipher
def get_caesar_cipher(plain_word, key):
    if key > 26:
        key = key % 26

    characters = list(plain_word)
    cipher = []
    for letter in characters:
        if ord(letter) in range(65, 91):
            new_ascii = ord(letter) + key
            if new_ascii > 90:
                new_ascii = ord(letter) - 26 + key
            cipher_letter = chr(new_ascii)

        elif ord(letter) in range(97, 123):
            current_ascii = ord(letter) + key
            if current_ascii > 122:
                current_ascii = ord(letter) - 26 + key
            cipher_letter = chr(current_ascii)

        else:
            cipher_letter = letter

        cipher.append(cipher_letter)

    cipher_word = ''.join(cipher)
    return cipher_word


# function for getting cipher text
def caesar_cipher(plain_text, key):
    cipher_text = []
    for word in plain_text:
        cipher_word = get_caesar_cipher(word, key)
        cipher_text.append(cipher_word)
    return ' '.join(cipher_text)


# main
input_text = input("Enter the plain text : ").split()
shift_key = int(input("Enter the shift key : "))
caesar_cipher_text = caesar_cipher(input_text, shift_key)
print(f"Cipher text : {caesar_cipher_text}")
