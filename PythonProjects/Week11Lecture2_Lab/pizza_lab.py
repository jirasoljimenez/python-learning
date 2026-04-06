# ============================================
# PIZZA ORDER SYSTEM
# CS 1300 — Lecture 6 Lab
# ============================================

# ----- Unmodified Data -----
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
size_prices = [6.99, 9.99, 12.99, 16.99]
topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions", "Sausage", "Bacon", "Extra Cheese", "Pineapple"]
topping_price = 1.50
order_descriptions = []
order_prices = []

# Pizza Size Menu
pizza = True
while pizza:
    print("=" * 30) 
    print("\tPIZZA SIZES") 
    print("=" * 30) 
    for i in range(len(sizes)): 
        print(f"{i + 1}. {sizes[i]:<15}\t${size_prices[i]:>5}") 
    print("=" * 30)
    
    # Asking for the Pizza Size
    try:
        size_choice = int(input("Pick a size (1-4): "))
        if size_choice == 0:
            pizza = False
            break
        elif size_choice < 1 or size_choice > 4:
            print("Choose 1-4.")
            continue
    except ValueError:
        print("Please enter a number!")
        continue
    
    # Show Menu of Toppings
    print("\nTOPPINGS:")
    for i in range(len(topping_names)):
        print(f"{i + 1}. {topping_names[i]}")

    # User Selects toppings
    selected_toppings = []
    user_input = input("Enter Topping Number. Type done to finish: ")

    while user_input.lower() != "done":
        if user_input.isdigit() and 1 <= int(user_input) <= 8:
            topping = topping_names[int(user_input) - 1]
            if topping not in selected_toppings:
                selected_toppings.append(topping)
                print(f"✓ Added {topping}")
            else:
                print(f"Already Added {topping}!")
        else:
            print("Not a Topping")
        user_input = input("Enter topping number. Type done to finish: ")

    # If no toppings selected, add cheese
    if not selected_toppings:
        selected_toppings.append("Cheese")

    # Calculate and store price/pizza
    price = size_prices[size_choice - 1] + len(selected_toppings) * topping_price
    order_descriptions.append(f"{sizes[size_choice - 1]} {', '.join(selected_toppings)}")
    order_prices.append(price)

    # Ask user if they want another pizza
    while True:
        order_another = input("Order another pizza? (y/n): ").lower()
        if order_another in ["y", "yes"]:
            break  # loop again and build another pizza
        elif order_another in ["n", "no"]:
            pizza = False
            break
        else:
            print("Invalid, Please Try Again")

# Calculate receipt totals
subtotal = sum(order_prices)
tax = subtotal * 0.07
discount_rate = 1

if not order_descriptions:
    print("\nNo pizzas ordered. See you next time!")
else:
    # Discount section
    attempts = 0
    while attempts < 3:
        discount_question = input("Do you have a discount?: ").lower()
        if discount_question == "none":
            break
        if discount_question in ["y", "yes"]:
            discount_input = input("What is it? ")
            if discount_input == "STUDENT10":
                discount_rate = 0.90
                print("Discount = 10% Off")
                break
            elif discount_input == "HALFOFF":
                discount_rate = 0.50
                print("Discount = 50% Off")
                break
            else:
                print(f"Invalid discount code. {attempts + 1} Attempts Tried.")
                attempts += 1
                continue
        else:
            print("Invalid response.")
        if attempts == 3:
            print("No discount applied.")

    # Receipt
    print("=" * 35)
    print("\tYOUR ORDER RECEIPT")
    print("=" * 35)
    for i in range(len(order_descriptions)):
        print(f"{i + 1}. {order_descriptions[i]}")
        print(f"   ${order_prices[i]:.2f}")
    print("=" * 35)
    print(f"Subtotal:                ${subtotal * discount_rate:>6.2f}")
    print(f"Tax (7%):                ${tax:>6.2f}")
    print(f"Total:                   ${subtotal * discount_rate + tax:>6.2f}")
    print("=" * 35)
    print("\nThank you for your order!")

    most_expensive = max(order_prices)
    print(f"Most Expensive Pizza: ${most_expensive:.2f}")

    least_expensive = min(order_prices)
    print(f"Least Expensive Pizza: ${least_expensive:.2f}")

personal_count=0
medium_count=0
large_count=0
party_count=0

for i in range(len(order_descriptions)):
    if order_descriptions[i][0:5]=="Large":
        large_count +=1
    if order_descriptions[i][0:5]=="Perso":
        personal_count+=1
    if order_descriptions[i][0:5]=="Mediu":
        medium_count+=1
    if order_descriptions[i][0:5]=="Party":
        party_count+=1

print(f"personal count {personal_count}, medium count {medium_count}, large count {large_count}, party count {party_count}")  