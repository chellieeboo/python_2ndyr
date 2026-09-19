# Create a function that greets a student
def greet(name):
    # Return the greeting message 
    return f"\nHello, {name}, welcome to Data Structure and Algorithms"


# Ask for the names of two students
name1 = input("Enter first student's name: ")
name2 = input("Enter second student's name: ")

# Call the function and display the returned message
print(greet(name1))
print(greet(name2))