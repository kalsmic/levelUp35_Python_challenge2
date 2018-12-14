#
# QN3
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
def get_input(message):
    return input(message)

def validate_user_input():
    number_sequence = get_input("Enter a sequence of comma separated 4 digit binary numbers: ")
    numbers_list = number_sequence.split(",")
    print(numbers_list)

    if len(numbers_list) != 4:
        print("Provide a sequence of exactly four binary numbers separated by a comma")
        return None

    for number in numbers_list:
        try:
            number = int(number,int(2))
        except ValueError:
            print("You did not provide a sequence of binary numbers")
            return None

    return numbers_list

def get_numbers_divisible_by_five():
    binary_numbers_list = validate_user_input()

    for binary_number in binary_numbers_list:
        decimal_number = int(binary_number,2)
        if decimal_number % 5 == 0:
            print(str(binary_number),end=",")

