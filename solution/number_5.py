
def square_range_of_numbers(from_number, to_number):
    """Generate a list of squared numbers from a range"""
    squared_numbers = []
    for number in range(from_number, to_number):
        squared_numbers.append(number ** 2)
    return squared_numbers


def print_list():
    """Prints the first five squared numbers"""
    square_numbers_list = square_range_of_numbers(1, 21)
    for square_number in square_numbers_list[:5]:
        print(square_number)


if __name__ == "__main__":
    print_list()
