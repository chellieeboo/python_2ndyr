# STORE INVENTORY SYSTEM
# Note: I used AI to help me understand and structure the Queue (FIFO)
# and Stack (LIFO) operations properly - Enqueue, Dequeue, Peek, IsEmpty, Push, Pop.
# I reviewed and adjusted the code  to match what we discussed in class.

# Inventory: [Name, Price, Status, Expired]
inventory = [
    ["Milk", 89.50, "Old", True],      
    ["Bread", 65.00, "Old", False],
    ["Coffee", 120.00, "New", False],
    ["Juice", 75.00, "New", True],
    ["Rice", 250.00, "New", False]
]

# ================================
# BARCODE GENERATION
# Rule: first 2 letters of name (uppercase) + length of the name
# ================================
for item in inventory:                      
    item_name = item[0]                      
    barcode = item_name[:2].upper() + str(len(item_name))
    # item_name[:2]  -> take only the first 2 characters (e.g. "Milk" -> "Mi")
    # .upper()       -> convert those letters to uppercase ("Mi" -> "MI")
    # len(item_name) -> count total letters in the name ("Milk" = 4)
    # str(...)       -> convert that number to text so it can be joined with "MI"
    # +              -> combine letters + number into one barcode string ("MI4")
    item.append(barcode)                     # add barcode to the end of this item's list (becomes item[4])

print("===== STORE INVENTORY SYSTEM =====")

# ================================
# QUEUE (FIFO - First In, First Out)
# Operations: Enqueue, Dequeue, Peek/Front, IsEmpty
# ================================
incoming_goods = []                          

# ENQUEUE - adding new stock to the back of the line
incoming_goods.append("Milk")               
incoming_goods.append("Bread")               
incoming_goods.append("Coffee")             
print("\nIncoming Goods Queue:", incoming_goods)   # show current contents of the queue

# PEEK / FRONT - check who's next in line WITHOUT removing them
if len(incoming_goods) > 0: # only peek if the queue is not empty
    print("Next to process (Peek):", incoming_goods[0])  # index 0 = front of the queue

# DEQUEUE - process and remove the one at the front of the line
print("\nProcessing Incoming Goods (Dequeue):")
while len(incoming_goods) > 0: # ISEMPTY check - keep looping while queue has items
    front_item = incoming_goods.pop(0) # DEQUEUE - remove and return the FIRST item (index 0)
    print(front_item) # display the item we just removed/processed

# ISEMPTY - confirm the queue has nothing left
print("Queue is empty:", len(incoming_goods) == 0)# True if length is 0, meaning queue is empty

# TRAVERSAL - go through the whole inventory list without removing anything
print("\n===== CURRENT INVENTORY =====")
for item in inventory: # loop through each item in inventory
    print("Name:", item[0])                   
    print("Price: ₱", item[1])                
    print("Status:", item[2])                 
    print("Barcode:", item[4])                 
    print()                                    

# ================================
# STACK (LIFO - Last In, First Out)
# Operations: Push, Pop, Peek, IsEmpty
# ================================
old_products = []                         
new_products = []                          

for item in inventory:# go through inventory to sort items into 2 stacks
    if item[2] == "Old":
        old_products.append(item)    
    else:
        new_products.append(item)             
# PEEK - look at the top item WITHOUT removing it
print("===== OLD PRODUCTS STACK =====")
if len(old_products) > 0: 
    print("Top of stack (Peek):", old_products[-1][0])  # index -1 = last item = top of stack

while len(old_products) > 0:# ISEMPTY check - loop while stack still has items
    item = old_products.pop() # POP - remove and return the LAST item (top of stack)
    print(item[0], "-", item[4])  # print the name and barcode of that item
print("Old products stack is empty:", len(old_products) == 0)  # confirm stack is now empty

print("\n===== NEW PRODUCTS STACK =====")
if len(new_products) > 0:                    
    print("Top of stack (Peek):", new_products[-1][0])  # index -1 = top of stack

while len(new_products) > 0: # ISEMPTY check - loop while stack still has items
    item = new_products.pop()  # POP - remove and return the LAST item (top of stack)
    print(item[0], "-", item[4])  # print the name and barcode of that item
print("New products stack is empty:", len(new_products) == 0)  # confirm stack is now empty

# ================================
# REMOVE EXPIRED ITEMS
# ================================
print("\n===== REMOVING EXPIRED ITEMS =====")
i = 0
while i < len(inventory):                    
    if inventory[i][3] == True: # check the Expired flag (index 3) of current item
        inventory.pop(i) # remove this item from inventory
    else:
        i = i + 1# only move to next index if current item was NOT removed

# ================================
# UPDATED INVENTORY - final display after removing expired items
# ================================
print("\n===== UPDATED INVENTORY =====")
for item in inventory:                       # loop through what's left in inventory
    print(
        "Name:", item[0],                      # item name
        "| Price: ₱", item[1],                  # item price
        "| Status:", item[2],                   # item status (Old/New)
        "| Barcode:", item[4]                   # item barcode
    )