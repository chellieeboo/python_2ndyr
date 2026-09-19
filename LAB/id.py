# User-defined functions using Student ID: 7284
#notChecked

student_id = "7284"

# 1. Using return()
def use_return(number):
    # Return each digit of the number
    return number


# 2. Using break()
def use_break(number):
    print("\nUsing break():")

    for digit in number:
        print(digit)

        # Stop the loop when the digit is 8
        if digit == "8":
            break

# 3. Using pass()
def use_pass(number):
    print("\nUsing pass():")

    for digit in number:
        if digit == "2":
            pass  # Do nothing when the digit is 2
        print(digit)


# 4. Using continue()
def use_continue(number):
    print("\nUsing continue():")

    for digit in number:
        # Skip the digit 2
        if digit == "2":
            continue

        print(digit)


# Main program
print("Student ID:", student_id)

print("\nUsing return():")
for digit in student_id:
    result = use_return(digit)
    print(result)

use_break(student_id)
use_pass(student_id)
use_continue(student_id)