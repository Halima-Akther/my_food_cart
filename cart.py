# cart.py
cart = []


def add_item(item_name, price, quantity):
    total = price * quantity
    cart.append({
        "item": item_name,
        "quantity": quantity,
        "price": price,
        "total": total
    })


def view_cart():
    if not cart:
        print("Cart is empty!")
        return 0
    grand_total = 0
    print("\n------ YOUR CART ------")
    for idx, c in enumerate(cart, 1):
        print(f"{idx}. {c['quantity']} x {c['item']} = {c['total']} BDT")
        grand_total += c['total']
    print("------------------------")
    print(f"TOTAL: {grand_total} BDT")
    return grand_total


def remove_item(index):
    if 1 <= index <= len(cart):
        removed = cart.pop(index - 1)
        print(
            f"🗑️ Removed {removed['quantity']} x {removed['item']} from cart.")
    else:
        print("❌ Invalid item number!")


def checkout():
    if not cart:
        print("❌ Cart is empty!")
        return
    grand_total = view_cart()
    print(f"✅ Order placed successfully! Total Bill: {grand_total} BDT")
    cart.clear()
