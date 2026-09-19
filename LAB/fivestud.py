id_numbers = []
last_names = []

for i in range(5):
    id_input = input("Enter Id-number: ")
    ln_input = input("Enter Lastname: ")
    id_numbers.append(id_input)
    last_names.append(ln_input)

print("\n==Generated Id-numbers with Student lastname==")
for i in range(5):
    length = len(last_names[i])
    print(i + 1, ". ", last_names[i], ": 2026-", id_numbers[i], length, sep="")
    
    #I didn't know their ID numbers, so I just created random numbers for them.
    
