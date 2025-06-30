import json

# --- Step 1: Define the data ---
vegetable_data = {
    "Daily Regular Vegetables": [
        {"name": "Onion", "name_hi": "प्याज", "price": 20},
        {"name": "Garlic", "name_hi": "लहसुन", "price": 30},
        {"name": "Ginger", "name_hi": "अदरक", "price": 40},
        {"name": "Green chilli", "name_hi": "हरी मिर्च", "price": 10},
        {"name": "Cabbage", "name_hi": "पत्ता गोभी", "price": 25},
        {"name": "Cauliflower", "name_hi": "फूलगोभी", "price": 30},
        {"name": "Bottle gourd", "name_hi": "लौकी", "price": 20},
        {"name": "Pumpkin", "name_hi": "कद्दू", "price": 25},
        {"name": "Ridge gourd", "name_hi": "तुरई", "price": 20},
        {"name": "Bitter gourd", "name_hi": "करेला", "price": 30}
    ],
    "Leafy Greens": [
        {"name": "Spinach", "name_hi": "पालक", "price": 20},
        {"name": "Fenugreek", "name_hi": "मेथी", "price": 10},
        {"name": "Amaranth", "name_hi": "चौलाई", "price": 20},
        {"name": "Mustard greens", "name_hi": "सरसों का साग", "price": 30},
        {"name": "Bathua", "name_hi": "बथुआ", "price": 15},
        {"name": "Coriander leaves", "name_hi": "धनिया पत्ता", "price": 10},
        {"name": "Mint", "name_hi": "पुदीना", "price": 10},
        {"name": "Drumstick leaves", "name_hi": "सहजन के पत्ते", "price": 20}
    ],
    "Fruiting Vegetables": [
        {"name": "Tomato", "name_hi": "टमाटर", "price": 30},
        {"name": "Brinjal", "name_hi": "बैंगन", "price": 25},
        {"name": "Okra", "name_hi": "भिंडी", "price": 20},
        {"name": "Capsicum", "name_hi": "शिमला मिर्च", "price": 20},
        {"name": "Cucumber", "name_hi": "खीरा", "price": 20},
        {"name": "Chillies", "name_hi": "हरी मिर्च", "price": 10},
        {"name": "Sweet corn", "name_hi": "स्वीट कॉर्न", "price": 20}
    ],
    "Root Vegetables": [
        {"name": "Carrot", "name_hi": "गाजर", "price": 30},
        {"name": "Beetroot", "name_hi": "चुकंदर", "price": 40},
        {"name": "Radish", "name_hi": "मूली", "price": 15},
        {"name": "Potato", "name_hi": "आलू", "price": 20},
        {"name": "Sweet potato", "name_hi": "शकरकंद", "price": 30}
    ]
}

# --- Step 2: Build the menu dictionary ---
menu = {}
index = 1
for category, veggies in vegetable_data.items():
    for veg in veggies:
        menu[index] = (category, veg['name'], veg['name_hi'], veg['price'])
        index += 1

# --- Step 3: Display the menu ---
def show_menu():
    print("\n🛒 Available Vegetables:")
    last_cat = None
    for idx in sorted(menu):
        cat, veg_en, veg_hi, price = menu[idx]
        if cat != last_cat:
            print(f"\n{cat}:")
            last_cat = cat
        print(f"  {idx:2d}. {veg_en.capitalize():15s} ({veg_hi}) — ₹{price}/kg")

# --- Step 4: Parse user input ---
def parse_selection(selection_str):
    picks = set()
    for part in selection_str.split(','):
        part = part.strip()
        if part.isdigit():
            idx = int(part)
            if idx in menu:
                picks.add(idx)
            else:
                print(f"Ignoring invalid choice: {part}")
        else:
            print(f"Ignoring invalid input: {part}")
    return sorted(picks)

# --- Step 5: Main shopping cart app ---
def main():
    print("✨ Welcome to the Veggie Bazaar! ✨")
    cart = []
    while True:
        show_menu()
        user_input = input("\nEnter item numbers to add (e.g., 1,3,5) or '0' to finish selection: ").strip()
        if user_input == '0':
            break
        picks = parse_selection(user_input)
        if not picks:
            print("\nYou have not selected anything.")
            user_choice = input("Would you like to buy Tomato instead? (y/n): ").strip().lower()
            if user_choice == 'y':
                cart.append({"vegetable": "Tomato", "price": 30, "quantity": 1})
                print("\nTomato has been added to your cart.")
            else:
                print("No items selected. Exiting the process.")
                return
        else:
            for idx in picks:
                cat, veg_en, veg_hi, price = menu[idx]
                while True:
                    qty_str = input(f"Enter quantity for {veg_en.capitalize()} ({veg_hi}) in kg: ").strip()
                    try:
                        qty = float(qty_str)
                        if qty > 0:
                            break
                        else:
                            print("Quantity must be positive.")
                    except ValueError:
                        print("Invalid input. Please enter a number like 1, 0.5, etc.")
                cart.append({"vegetable": veg_en, "price": price, "quantity": qty})

        # Display cart
        print("\n🧺 Your Cart:")
        total_price = 0
        for item in cart:
            veg = item['vegetable'].capitalize()
            qty = item['quantity']
            price = item['price']
            subtotal = qty * price
            total_price += subtotal
            print(f"  - {veg}: {qty}kg @ ₹{price}/kg → ₹{subtotal:.2f}")
        print(f"Total: ₹{total_price:.2f}")

        # Next options
        while True:
            print("\nWhat would you like to do next?")
            print("  1. Add more vegetables")
            print("  2. Delete an item from cart")
            print("  3. Proceed to checkout")
            choice = input("Enter 1, 2, or 3: ").strip()
            if choice == '1':
                break
            elif choice == '2':
                if not cart:
                    print("Cart is empty.")
                    continue
                print("\nItems in Cart:")
                for i, item in enumerate(cart, start=1):
                    print(f"  {i}. {item['vegetable'].capitalize()}: {item['quantity']}kg @ ₹{item['price']} → ₹{item['price'] * item['quantity']:.2f}")
                del_str = input("Enter item number to delete (or '0' to cancel): ").strip()
                if del_str.isdigit():
                    di = int(del_str)
                    if 1 <= di <= len(cart):
                        removed = cart.pop(di - 1)
                        print(f"Removed {removed['vegetable'].capitalize()} from cart.")
                    elif di == 0:
                        pass
                    else:
                        print("Invalid item number.")
                else:
                    print("Invalid input.")
            elif choice == '3':
                if not cart:
                    print("Cart is empty.")
                    continue
                with open('cart.json', 'w', encoding='utf-8') as f:
                    json.dump(cart, f, indent=2)

                address = input("\nPlease enter your delivery address: ").strip()
                total = sum(item['price'] * item['quantity'] for item in cart)
                receipt = {
                    "delivery_address": address,
                    "order": cart,
                    "total": total
                }
                with open('order_receipt.json', 'w', encoding='utf-8') as f:
                    json.dump(receipt, f, indent=2)

                print("\n🧾 Order Receipt:")
                print(f"Delivery Address: {address}")
                for item in cart:
                    veg = item['vegetable'].capitalize()
                    qty = item['quantity']
                    price = item['price']
                    print(f"  - {veg}: {qty}kg @ ₹{price}/kg → ₹{qty * price:.2f}")
                print(f"Total: ₹{total:.2f}")
                print("\nThank you for shopping with us! 🌽🍆🥦")
                return
            else:
                print("Please enter a valid option.")

if __name__ == "__main__":
    main()
