
passenger = ["5", "12", "8"]

print("Available stops:")
for i in range(len(passenger)):# chine check kung ilan ang element ng pass list
    print(f"Stop {i}: {passenger[i]} passengers")#index tapos yung laman ng element

print("\n" + "="*40)

stop_num = int(input("Enter stop number (index): "))

if stop_num >= 0 and stop_num < len(passenger):
    print(f"\nStop {stop_num} has {passenger[stop_num]} passengers")
else:
    print(f"\n Invalid stop number! Please enter a number from 0 to {len(passenger)-1}.")
   