 # File contains a program that accepts sequence of lines as inputWrite
 # a program that accepts sequence of lines as input and prints the lines after
 # making all characters in the sentence capitalized. and prints the lines
 # after making all characters in the sentence capitalized.

import pprint
import sys
print("#"*50)

print("This program accepts a sequence of lines as input and prints a them after capitalizing them:\n")



def get_input(message):
    return  input(message)

def get_sentence():
    pprint.pprint("Enter a Sentence to capitalize: ")
    return get_input("Sentence: ")

def capitalize(sequence):
    for sentence in sequence:
        print(sentence.upper())

def sequence_capitalizer():
    sequence = []
    sentence = get_sentence()
    sequence.append(sentence)


    while True:
        print("Enter 1 to add another sentence \n 2 to print Capitalized sequence \n Enter r to return to the main menu \n Enter q to quit")
        control_options = get_input("Enter your option: ")
        try:
            if int(control_options) == 1:
                sequence.append(get_sentence())
            elif int(control_options) == 2:
                capitalize(sequence)
                return False
        except ValueError:
            if control_options == 'r':
                print("Thank you for using Sequence Capitalizer")
                return False
            elif control_options == 'q':
                print("Thank you for using Sequence Capitalizer. Bye Bye")
                sys.exit(0)
            else:
                print("You did not enter a valid response")


if __name__ == "__main__":
    sequence_capitalizer()