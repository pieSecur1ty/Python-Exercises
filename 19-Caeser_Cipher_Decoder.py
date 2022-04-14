# function for getting plain letter
def get_plain_letter(letter, key):
    plain_letter = ""
    if ord(letter) in range(65, 91):
        new_ascii = ord(letter) - 3
        if new_ascii < 65:
            new_ascii = new_ascii + 26
        plain_letter = chr(new_ascii)

    elif ord(letter) in range(97, 123):
        new_ascii = ord(letter) - 3
        if new_ascii < 97:
            new_ascii = new_ascii + 26
        plain_letter = chr(new_ascii)
    else:
        plain_letter = letter
    return plain_letter


# function for getting decoded text
def get_decoded_text(cipher_text, key):
    decoded_text = []
    for letter in cipher_text:
        decoded_letter = get_plain_letter(letter, key)
        decoded_text.append(decoded_letter)
    return ''.join(decoded_text)


# main
caesar_cipher = input("Enter the Caesar cipher text : ")
shift_key = int(input("Enter the shift key : "))

if shift_key > 26:
    shift_key = shift_key % 26

plain_text = get_decoded_text(caesar_cipher, shift_key)

print(f"Plain Text : {plain_text}")
