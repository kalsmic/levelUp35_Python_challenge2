import sys
from solution.number_0 import get_student_grades
from solution.number_1 import get_multiples_of_seven_not_divisible_by_five
from solution.number_2 import sequence_capitalizer
from solution.number_4 import transact

print("Solutions to Level up 35 December Python challenges")
while True:
    print("Enter 0 to run solution to Question 0")
    print("Enter 1 to run solution to Question 1")
    print("Enter 2 to run solution to Question 2")
    print("Enter 3 to run solution to Question 3")
    print("Enter 4 to run solution to Question 4")
    print("Enter 5 to run solution to Question 5")
    print("Enter q to exit the program\n")
    print("-"*60)

    input_option = input("Enter Option: ")

    try:

        if int(input_option) == 0:
            get_student_grades([23, 4, 5, 6, 64, 90, 67, 98, 45, 23, 67, 78, 89])
            print("-" * 60)

        elif int(input_option) == 1:
            get_multiples_of_seven_not_divisible_by_five()
            print("-" * 60)

        elif int(input_option) == 2:
            sequence_capitalizer()
            print("-" * 60)

        elif int(input_option) == 3 or int(input_option) == 4:
            print("Not yet compeleted, kindly choose another option \n")
            print("-" * 60)

    except ValueError:
        if input_option == 'q':
            print("Thank you for reviewing my solutions. Bye Bye")
            sys.exit(0)
        else:
            print("You did not enter a valid response")


