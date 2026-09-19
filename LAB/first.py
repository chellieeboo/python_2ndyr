# Step 1: Start

# Step 2: Empty arrays
student_ids = []
lastnames = []
name_lengths = []

# Step 3: Ask how many students
num_students = int(input("Enter number of students: "))

# Step 4: Loop
for i in range(num_students):
    # Step 4.1: Get Student ID
    student_id = input(f"Enter Student ID #{i+1}: ")
    student_ids.append(student_id)
    
    # Step 4.3: Get Lastname
    lastname = input(f"Enter Lastname #{i+1}: ")
    lastnames.append(lastname)
    
    # Step 4.5: Compute length
    length = len(lastname)
    name_lengths.append(length)

# Step 5: Print results
print("\n--- STUDENT RECORDS ---")
print("ID\t| Lastname\t| Length")
print("-" * 30)
for i in range(num_students):
    print(f"{student_ids[i]}\t| {lastnames[i]}\t| {name_lengths[i]}")

# Step 6: End