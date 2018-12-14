# MOdule for grading system
# Make a grading system for the students marks below
# [23,4,5,6,64,90,67,98,45,23,67,78,89]
import pprint

def grade_marks(marks):

    if marks >= 90:
        return f"{ marks } : Excellent"

    elif marks >= 89:
        return f"{marks } :Very good"

    elif marks >= 60:
        return f"{marks} : Good"

    elif marks >=40:
        return f"{marks} : poor"

    elif marks >= 20:
        return f"{marks} : Very poor"

    elif marks >= 0:
        return f"{marks} : Repeat"

def print_student_grades(grade_list):
    for grade in grade_list:
        pprint.pprint(grade)


def get_student_grades(marks_list):
    if not isinstance(marks_list, list):
        pprint.pprint("Please provide a list")
        return None



    marks_below_average = []
    marks_above_average = []

    for mark in marks_list:
        result = grade_marks(mark)
        if mark > 50:
            marks_above_average.append(result)
        else:
            marks_below_average.append(result)

    print("Marks Bellow Average")
    print_student_grades(marks_below_average)
    pprint.pprint("Marks Above Average")
    print_student_grades(marks_above_average)









# [ pprint.pprint(marks) for marks in marks_above_average)]
#
#     print("Grades below Average")
#     pprint.pprint(marks_below_average)
#


#

if __name__ == "__main__":
    get_student_grades((23,4,5,6,64,90,67,98,45,23,67,78,89))
