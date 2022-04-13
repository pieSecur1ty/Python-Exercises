# function to check the input string is pangram or not
def check_pangram(sentence):
    input_characters = []
    for word in sentence:
        for letter in word.lower():
            if ord(letter) in range(97, 123):
                input_characters.append(letter)
            else:
                pass

    input_characters = list(set(input_characters))

    if len(input_characters) == 26:
        print("Pangram\n")
    else:
        print("Not Pangram\n")


# user input and output
input_string = input("Enter the sentence : ").split()
check_pangram(input_string)
