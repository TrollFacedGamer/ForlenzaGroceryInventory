def add_item(inventory, name, price, quantity):
    """
    Add a new item to the inventory.
    
    Args:
    inventory (dict): The current inventory
    name (str): The name of the item
    price (str): The price of the item
    quantity (str): The quantity of the item
    """
    #added if else statment to check if name aready present
    if name in inventory:
        print("Warning, adding a new item with the same name as a existing item will cause the new item to override the old item.")
        continue_question = input("Do you wish to continue?(yes/no)")

        #add if statments for confirmation
        if continue_question == "yes":
            continue_yn = True
        elif continue_question == "no":
            continue_yn = False
        else:    
            print("error: you can only enter yes and no as a response, no uppercasae.")

        #if continue_yn is true
        if continue_yn:
            inventory[name] = {"price": price, "quantity": quantity}
            print(f"{name} added to the inventory.")
    else:
        inventory[name] = {"price": price, "quantity": quantity}
        print(f"{name} added to the inventory.")

def remove_item(inventory, item_name):
    """
    Remove an item from the inventory.
    
    Args:
    inventory (dict): The current inventory
    item_name (str): The name of the item to remove
    """
    #put in if to check input
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed from the inventory.")
    else:
        print("error: you need to enter the name of a existing item, you can't enter the number of the item")

def update_quantity(inventory, item_name, new_quantity):
    """
    Update the quantity of an item in the inventory.
    
    Args:
    inventory (dict): The current inventory
    item_name (str): The name of the item to update
    new_quantity (str): The new quantity of the item
    """
    #==to= for value assignment
    inventory[item_name]["quantity"] = new_quantity
    print(f"{item_name} quantity updated to {new_quantity}.")

def display_inventory(inventory):
    """
    Display all items in the inventory.
    
    Args:
    inventory (dict): The current inventory
    """
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for name in inventory:
            item = inventory[name]
            print(f"{name}: Price: ${item['price']:.2f}, Quantity: {item['quantity']}")

# Initialize inventory with two example items
inventory = {
    "apple": {"price": 0.50, "quantity": 100},
    "banana": {"price": 0.75, "quantity": 150}
}

while True:
    print("\n1. Add item\n2. Remove item\n3. Update quantity\n4. Display inventory\n5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        #auto display for easy use
        display_inventory(inventory)
        name = input("Enter item name: ")
        #changed type of process input
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        add_item(inventory, name, price, quantity)
    elif choice == "2":
        #auto display for easy use
        display_inventory(inventory)
        name = input("Enter item name to remove: ")
        remove_item(inventory, name)
    elif choice == "3":
        #auto display for easy use
        display_inventory(inventory)
        name = input("Enter item name to update: ")
        quantity = input("Enter new quantity: ")
        update_quantity(inventory, name, quantity)
    elif choice == "4":
        display_inventory(inventory)
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")