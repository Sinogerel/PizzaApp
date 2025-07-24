import sys

def display_menu(menu):
    """Displays the pizza menu to the user."""
    print("--- Our Delicious Pizza Menu ---")
    for i, (pizza, price) in enumerate(menu.items()):
        print(f"{i + 1}. {pizza}: ${price:.2f}")
    print("------------------------------")

def take_order(menu):
    """Allows the user to select pizzas and quantities."""
    order = {}
    while True:
        try:
            choice = input("Enter the number of the pizza you want to order (or 'done' to finish): ").lower()
            if choice == 'done':
                break
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(menu):
                pizza_names = list(menu.keys())
                selected_pizza = pizza_names[choice_num - 1]
                
                while True:
                    try:
                        quantity = int(input(f"How many '{selected_pizza}' pizzas would you like? "))
                        if quantity > 0:
                            order[selected_pizza] = order.get(selected_pizza, 0) + quantity
                            break
                        else:
                            print("Quantity must be a positive number. Please try again.")
                    except ValueError:
                        print("Invalid quantity. Please enter a number.")
            else:
                print("Invalid pizza number. Please choose from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    return order

def calculate_total(order, menu):
    """Calculates the total cost of the order."""
    total_cost = 0
    print("\n--- Your Order Summary ---")
    if not order:
        print("No items in your order.")
        return 0
    
    for pizza, quantity in order.items():
        price = menu[pizza]
        item_cost = price * quantity
        total_cost += item_cost
        print(f"{pizza} x {quantity} = ${item_cost:.2f}")
    print(f"--------------------------")
    print(f"Total: ${total_cost:.2f}")
    return total_cost

def get_delivery_details():
    """Collects customer's delivery information."""
    print("\n--- Delivery Details ---")
    name = input("Enter your full name: ").strip()
    address = input("Enter your delivery address: ").strip()
    phone = input("Enter your phone number: ").strip()
    
    # Simple validation
    if not name or not address or not phone:
        print("All delivery details are required. Please try again.")
        return get_delivery_details() # Recursive call to retry
    
    return {"name": name, "address": address, "phone": phone}

def main():
    """Main function to run the pizza app."""
    pizzas = {
        "Margherita": 12.00,
        "Pepperoni": 15.00,
        "Vegetable Feast": 14.50,
        "Chicken BBQ": 16.00,
        "Hawaiian": 13.00
    }

    print("Welcome to our Pizza Delivery Service!")
    
    display_menu(pizzas)
    
    customer_order = take_order(pizzas)
    
    if not customer_order:
        print("You didn't order any pizzas. Goodbye!")
        sys.exit()

    total_amount = calculate_total(customer_order, pizzas)
    
    delivery_info = get_delivery_details()
    
    print("\n--- Order Confirmation ---")
    print("Your order has been placed!")
    print("\nOrder Details:")
    for pizza, quantity in customer_order.items():
        print(f"- {pizza} x {quantity}")
    print(f"\nTotal Cost: ${total_amount:.2f}")
    print("\nDelivery Information:")
    print(f"Name: {delivery_info['name']}")
    print(f"Address: {delivery_info['address']}")
    print(f"Phone: {delivery_info['phone']}")
    print("\nThank you for your order! Your pizza will be delivered soon.")

if __name__ == "__main__":
    main()