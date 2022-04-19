# function for checking anagram
def check_anagram(string1, string2):
    string1_letter = []
    for character in string1:
        char_ascii = ord(character)
        if((char_ascii > 65 and char_ascii < 91) or (char_ascii > 97 and char_ascii < 123)):
            string1_letter.append(character.lower())

    flag = 1
    for item in string1_letter:
        if item not in string2.lower():
            flag = 0
            break

    if flag == 1:
        print("Anagram\n")
    else:
        print("Not anagram\n")


# Main
input_string1 = input("Enter the first string : ")
input_string2 = input("Enter the second string : ")
check_anagram(input_string1, input_string2)
