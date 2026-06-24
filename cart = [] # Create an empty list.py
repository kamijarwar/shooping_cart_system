cart = []  # Create an empty list

while True:
    item = input("Enter product name (or type 'done' to finish): ").strip()
    
    if item.lower() == "done":
        break  # Exit the loop immediately
    
    cart.append(item)  # Add the item to the list

# Final Validation
if len(cart) == 0:
    print("\nCart Empty 🛒")
else:
    print(f"\nTotal Items in Cart: {len(cart)}")
    print("Your Shopping Items:")
    for product in cart:
        print(f"- {product}")
