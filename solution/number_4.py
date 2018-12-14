# Contains a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:

import pprint
import sys

pprint.pprint("This program computes the net amount of a bank account based a transaction log")


def get_input(message):
    return input(message)


class BankAccount:
    Balance = 0

    def __init__(self, balance=0):
        BankAccount.Balance += balance

    def deposit(self, ammount):
        BankAccount.Balance += ammount
        print(f"You have deposited {ammount}  Balance:{BankAccount.Balance}\n")
        return True

    def withdral(self, ammount):
        if BankAccount.Balance >= ammount:
            BankAccount.Balance -= ammount
            print(f"You have withdrawn {ammount}  Balance:{BankAccount.Balance}")
            return True
        else:
            print(f"You cannot with draw more than {BankAccount.Balance}\n")
            return True


def get_ammount():
    try:
        ammount = int(get_input("Enter Ammount: "))
        return ammount
    except ValueError:
        print("ammount must be an integer")
        return None

def validate_ammount(ammount):
    if isinstance(ammount,int):
        return True
    return False




def transact():
    user_account = BankAccount()


    while True:
        print("Enter D to deposit or W to withdral or q to exit\n")
        input_option = get_input("Enter option: ")
        if input_option.upper() == "D":
            ammount = get_ammount()
            if validate_ammount(ammount):
                user_account.deposit(ammount)

        elif input_option.upper() == "W":
            ammount = get_ammount()
            if validate_ammount(ammount):
                user_account.withdral(ammount)
        elif input_option == "q":
            print("thank you for banking with us\n")
            sys.exit(0)


if __name__ == "__main__":
    transact()
