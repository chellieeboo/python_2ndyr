students = []
id_number = input("Enter your ID number: ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

last_name_length = len(last_name)

students.append(id_number)
students.append(last_name_length)

print("--- RESULTS ---")
print("Your ID Number:", id_number) 
print("Length of your last name:", students[1])