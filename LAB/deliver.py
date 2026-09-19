#notChecked
class Node:
    # This is a node that will store one package or route
    def __init__(self, data):
        self.data = data       # stores the route name
        self.next = None       # points to the next node


class DeliveryRoute:
    # This class is used to create our singly linked list
    def __init__(self):
        self.head = None       # the first node
        self.count = 0         # counts how many items are added

    def add_package(self, item):
        # Create a new node for the new route
        new_node = Node(item)

        # If there is no node yet, make this the first node
        if self.head is None:
            self.head = new_node
        else:
            # Start from the first node
            current = self.head

            # Keep moving until we reach the last node
            while current.next:
                current = current.next

            # Add the new node at the end
            current.next = new_node

        # Add 1 to the number of items
        self.count += 1

    def display_route(self):
        # Check if the list is empty
        if self.head is None:
            print("No packages in the route.")
            return

        # Start from the first node
        current = self.head

        # This will store the whole delivery sequence
        route_str = "Start Route ----> "

        # Go through each node in the list
        while current:
            route_str += f"{current.data}----> "

            # Move to the next node
            current = current.next

        # Add message after all routes
        route_str += "Item delivered succesfully!"

        # Display the final route
        print(route_str)


def main():
    # Maximum number of routes allowed
    MAX_ROUTES = 5

    # Create a DeliveryRoute object
    route = DeliveryRoute()

    # Keep asking until the user enters a valid number
    while True:
        try:
            # Ask the user how many items they want to enter
            num_items = int(input("Enter number of items: "))

            # Check if the number is 0 or negative
            if num_items <= 0:
                print("Please enter a number greater than 0.")
                continue

            # Check if the number is more than the maximum
            if num_items > MAX_ROUTES:
                print(f"Maximum of {MAX_ROUTES} routes allowed. Setting to {MAX_ROUTES}.")
                num_items = MAX_ROUTES

            # Stop the loop if the input is valid
            break

        except ValueError:
            # This happens if the user enters letters or invalid input
            print("Invalid input. Please enter a whole number.")

    # Ask the user to enter each route
    for i in range(num_items):
        stop = input(f"Enter route {i + 1}: ")

        # Add the route to the linked list
        route.add_package(stop)

    # Display the delivery sequence
    print("\nDelivery Sequence:")
    route.display_route()


# This runs the main function when the program is started
if __name__ == "__main__":
    main()

