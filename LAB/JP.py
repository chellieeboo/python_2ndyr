# List ng mga jeepney stops
jeepney_stops = ["Rosario", "Nlac", "Sison", "Paldit", "Magic Mall"]
# total distance (km)
total_distance = 10
# Base fare at additional fare per km
base_fare = 20
fare_per_km = 0.10
# total stops
total_stops = len(jeepney_stops)
# Distance sa pagitan ng bawat stop
distance_between_stops = total_distance / (total_stops - 1)

# Display ng jeepney route
print("=" * 40)
print("JEEPNEY ROUTE")
print("=" * 40)
for i in range(total_stops):
    distance = distance_between_stops * i
    print(f"{i + 1}. {jeepney_stops[i]} - {distance:.2f} km")
print("=" * 40)

# Input ng passenger
user_stop = input("Enter drop-off stop: ")

# Variable para malaman kung nakita ang stop
found = False

# Hanapin ang stop sa list
for i in range(total_stops):
    if jeepney_stops[i].lower() == user_stop.lower():
        found = True
        user_stop = jeepney_stops[i]
        # Compute ang distance ng napiling stop
        travel_distance = distance_between_stops * i
        # Compute ang fare
        fare = base_fare + (travel_distance * fare_per_km)
        print(f"\n{user_stop} found!")
        print(f"Distance: {travel_distance:.2f} km")
        print(f"Fare: ₱{fare:.2f}")
        break

# Kapag wala ang stop
if not found:
    print(f"\n{user_stop} jeepney stop not found!")
    # Idagdag ang bagong stop sa route
    jeepney_stops.append(user_stop)
    # Update ang bilang ng stops
    total_stops = len(jeepney_stops)
    # Recompute ang distance bawat stop
    distance_between_stops = total_distance / (total_stops - 1)
    print(f"\n{user_stop} has been added to the route!")
    print("\n" + "=" * 40)
    print("UPDATED JEEPNEY ROUTE")
    print("=" * 40)
    # Display ang updated route
    for i in range(total_stops):
        distance = distance_between_stops * i
        print(f"{i + 1}. {jeepney_stops[i]} - {distance:.2f} km")
    print("=" * 40)
    # Compute ang distance ng bagong stop
    travel_distance = distance_between_stops * (total_stops - 1)
    # Compute ang fare
    fare = base_fare + (travel_distance * fare_per_km)
    print(f"\nDistance: {travel_distance:.2f} km")
    print(f"Fare: ₱{fare:.2f}")

# ===== Passenger type at discount =====
print("\nPassenger Type: [1] Regular  [2] Student  [3] Senior Citizen / PWD")
passenger_type = input("Choose passenger type (1/2/3): ")

if passenger_type == "2":
    passenger_label = "Student"
    discount_rate = 0.20
elif passenger_type == "3":
    passenger_label = "Senior Citizen / PWD"
    discount_rate = 0.20
else:
    passenger_label = "Regular"
    discount_rate = 0

# Compute ang discount at total fare
discount_amount = fare * discount_rate
total_fare = fare - discount_amount

# ===== Jeepney Receipt =====
print("\n" + "=" * 40)
print("JEEPNEY RECEIPT")
print("=" * 40)
print(f"Route: {jeepney_stops[0]} to {user_stop}")
print(f"Passenger Type: {passenger_label}")
print(f"Base Fare: P{fare:.2f}")
print(f"Discount: -P{discount_amount:.2f}")
print(f"Total Fare: P{total_fare:.2f}")
print(f"Jeepney Driver: Rochelle Bayogbog")
print("=" * 40)
print("Thank you, to God be the glory!")