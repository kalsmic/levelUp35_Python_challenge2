import sys
def get_input(message):
    return input(message)

def validate_input(number_sequence):
    numbers_list = number_sequence.split(",")

    if len(numbers_list) != 4:
        print("Provide a sequence of exactly four binary numbers separated by a comma")
        return None

    for number in numbers_list:
        try:
            number = int(number, int(2))

        except ValueError:
            print("You did not provide a sequence of binary numbers")
    return numbers_list

def get_numbers_divisible_by_five():
    while True:
        print("** Enter 1 to try out this solution")
        print("** Enter r to return to the main menu or q to quit")
        control_options = get_input("Enter your option: ")
        try:
            if int(control_options) == 1:

                print()
                number_sequence = get_input("Enter a sequence of comma separated 4 digit binary numbers: ")
                numbers_list = validate_input(number_sequence)
                if not isinstance(numbers_list,list):
                    continue
                for binary_number in numbers_list:
                    decimal_number = int(binary_number, 2)
                    if decimal_number % 5 == 0:
                        print(str(binary_number), end=",")
                return True
#
        except ValueError:
            if control_options == 'r':
                print("Thank you for reviewing solution 3.")
                return False
            elif control_options == 'q':
                print("Thank you for reviewing solution 3. Bye Bye")
                sys.exit(0)
            else:
                print("You did not enter a valid response")

