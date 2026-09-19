 # Name: Rochelle Bayogbog | Status: Present | Not Checked #
num = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in range(len(num)):
    for j in range(0, len(num) - i - 1):

      #If the number on the left is bigger than the number on the right, swap them.
        if num[j] > num[j + 1]:

            # Swap the numbers
            temp = num[j]
            num[j] = num[j + 1]
            num[j + 1] = temp

print(num)