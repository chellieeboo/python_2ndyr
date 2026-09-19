# Student Name: Rochelle Bayogbog
# Course/Section: BSIT 2
# Activity: first_route
# Status: NOT CHECKED

total_distance = 10
route = []

# Loop exactly 5 times (i goes from 0 to 4)
for i in range(5):
    distance = float(input(f"Enter distance for Stop {i + 1}: "))
    route.append(distance)
    total_distance += distance

print("\n" + "=" * 40)
print(f"Stops entered: {route}")
print(f"Final Total Distance: {total_distance} km")
route = []

# Loop exactly 5 times (i goes from 0 to 4)
for i in range(5):
    distance = float(input(f"Enter distance for Stop {i + 1}: "))
    route.append(distance)
    total_distance += distance

print("\n" + "=" * 40)
print(f"Stops entered: {route}")
print(f"Final Total Distance: {total_distance} km")