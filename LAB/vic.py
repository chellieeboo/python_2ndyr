# ======================================
# VICTORY BUS LINER TICKETING SYSTEM
# ======================================
# AI USAGE AGREEMENT
# I, [Your Full Name], acknowledge that I used AI assistance 
# to help me understand concepts and write this code.
# I fully understand the logic and take responsibility 
# for this submission.
# Date: [Date]
# ======================================

print("======================================")
print("VICTORY BUS LINER TICKETING SYSTEM")
print("======================================")

# Initialize variables
ticket_counter = 1
passenger_records = []
processing_queue = []
ticket_stack = []
continue_loop = True

# Main loop
while continue_loop == True:
    print()
    name = input("Enter Passenger Name (or 'DONE' to exit): ")
    
    if name.upper() == "DONE":
        continue_loop = False
    else:
        passenger_type = input("Enter Passenger Type (Regular/Student/Senior/PWD): ")
        destination = input("Enter Destination (Baguio/Batangas/La Union/Cebu/Davao): ")
        
        # Determine base fare based on destination
        if destination == "Baguio":
            base_fare = 800
        elif destination == "Batangas":
            base_fare = 400
        elif destination == "La Union":
            base_fare = 600
        elif destination == "Cebu":
            base_fare = 1200
        elif destination == "Davao":
            base_fare = 1500
        else:
            base_fare = 500
            print("Note: Unknown destination. Default fare applied.")
        
        # Determine discount based on passenger type
        if passenger_type == "Regular":
            discount = 0
        elif passenger_type == "Student":
            discount = 0.20
        elif passenger_type == "Senior":
            discount = 0.20
        elif passenger_type == "PWD":
            discount = 0.20
        else:
            discount = 0
            print("Note: Unknown passenger type. No discount applied.")
        
        # Calculate fare
        fare = base_fare - (base_fare * discount)
        
        # Generate ticket number
        ticket_number = ticket_counter
        ticket_counter = ticket_counter + 1
        
        # Create passenger record
        passenger_record = str(ticket_number) + "|" + name + "|" + passenger_type + "|" + destination + "|" + str(fare)
        
        # Record passenger
        passenger_records.append(passenger_record)
        
        # Enqueue to processing queue (FIFO)
        processing_queue.append(passenger_record)
        
        # Push to ticket stack (LIFO)
        ticket_stack.append(passenger_record)
        
        # Print ticket
        print()
        print("======================================")
        print("VICTORY BUS LINER TICKET")
        print("======================================")
        print("Ticket No.: " + str(ticket_number))
        print("Passenger : " + name)
        print("Type      : " + passenger_type)
        print("Destination: " + destination)
        print("Fare      : PHP " + str(fare))
        print("======================================")
        print("Ticket issued successfully!")

# End of transaction
print()
print("======================================")
print("END OF TRANSACTION")
print("======================================")

# Display all passenger records
print()
print("--- PASSENGER RECORDS ---")
for record in passenger_records:
    print(record)

# Display processing queue
print()
print("--- PROCESSING QUEUE (FIFO) ---")
for record in processing_queue:
    print(record)

# Display ticket stack
print()
print("--- TICKET STACK (LIFO) ---")
for record in ticket_stack:
    print(record)

# Display total passengers
print()
print("Total Passengers: " + str(len(passenger_records)))

print()
print("======================================")
print("Thank you for using Victory Bus Liner!")
print("======================================")