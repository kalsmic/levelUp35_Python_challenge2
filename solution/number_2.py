# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# Consider use range(#begin, #end) method


def get_multiples_of_seven_not_divisible_by_five():
    result = []

    for number in range(2000,3201):
        if number % 7 == 0 and not number % 5 == 0:
            result.append(number)
            print(number,end=",")

    # print(result)

if __name__ =="__main__":
    get_multiples_of_seven_not_divisible_by_five()