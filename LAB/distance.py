# =====================================================
# Student Name: Rochelle Bayogbog
# Course/Section: BSIT 2
# Activity: SARAO Jeepney Route, Fare & Receipt System
# Status: NOT CHECKED
# =====================================================

# ---------------- Series 2: Search the Route ----------------
# initialize jeepney stop route

jeepney_stops = ["Rosario", "Nalac", "Sison", "Paldit", "Pozzorubio"]  
total_distance = 10  # km, Rosario (start) to Pozzorubio (end)
total_stops = len(jeepney_stops)
distance_between_stops = total_distance / (total_stops - 1)

print("=" * 40)
print("JEEPNEY ROUTE")
print("=" * 40)
for i in range(total_stops):
    distance = distance_between_stops * i
    print(f"{i + 1}. {jeepney_stops[i]} - {distance:.2f} km")
print("=" * 40)

user_stop = input("Input jeepney stop: ")

found = False  # flag variable

for i in range(total_stops):
    if jeepney_stops[i] == user_stop:
        found = True
    elif jeepney_stops[i] != user_stop:
        pass  # keep searching

if found:
    print(f"{user_stop} stop found!")
else:
    print(f"{user_stop} jeepney stop not found!")

    # ---------------- Series 3 (part 1): Grow the Route (Append) ----------------
    jeepney_stops.append(user_stop)
    total_stops = len(jeepney_stops)
    distance_between_stops = total_distance / (total_stops - 1)

    print("\nUPDATED JEEPNEY ROUTE")
    print("=" * 40)
    for i in range(total_stops):
        distance = distance_between_stops * i
        print(f"{i + 1}. {jeepney_stops[i]} - {distance:.2f} km")
    print("=" * 40)

# ---------------- Series 3 (part 2): Calculate the Fare ----------------
# Compute distance & fare

stop_index = jeepney_stops.index(user_stop)
distance_traveled = distance_between_stops * stop_index

base_fare = 20.00 
extra_charge = 2.00        

if found:
    fare = base_fare
elif not found:
    fare = base_fare + extra_charge

# ---------------- Series 4: Apply Discounts ----------------

passenger_type = input("Enter passenger type (Regular/Student/Senior/PWD): ")

if passenger_type.lower() == "regular":
    discount_rate = 0
elif passenger_type.lower() == "student":
    discount_rate = 0.20
elif passenger_type.lower() == "senior":
    discount_rate = 0.20
elif passenger_type.lower() == "pwd":
    discount_rate = 0.20
else:
    discount_rate = 0

discount_amount = fare * discount_rate
total_fare = fare - discount_amount

# ---------------- Series 4: Finish the Receipt ----------------

print("\n" + "=" * 40)
print("=SARAO JEEPNEY RECEIPT=")
print(f"Route: Rosario to Pozzorubio V.V")
print(f"Drop-off Stop: {user_stop}")
print(f"Distance Traveled: {distance_traveled:.2f} km")
print(f"Passenger Type: {passenger_type}")
print(f"Discount: {discount_rate * 100:.0f}% (₱{discount_amount:.2f})")
print(f"Total Fare: ₱{total_fare:.2f}")
print("Jeepney Driver: Your Fullname")
print("=Thank You! To God Be the Glory=")
print("=" * 40)