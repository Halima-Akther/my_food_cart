# app.py
from cart import add_item, view_cart, remove_item, checkout
from menu import menu, show_menu


def add_to_cart_ui():
    show_menu()
    try:
        choice = int(input("Enter item number: "))
        if choice in menu:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("❌ Quantity must be greater than 0!")
                return
            item = menu[choice]
            add_item(item['name'], item['price'], quantity)
            print(f"✅ {quantity} x {item['name']} added to cart.\n")
        else:
            print("❌ Invalid choice!")
    except ValueError:
        print("❌ Please enter a valid number!")


def remove_from_cart_ui():
    try:
        view_cart()
        index = int(input("Enter item number to remove: "))
        remove_item(index)
    except ValueError:
        print("❌ Please enter a valid number!")


def main():
    while True:
        print("\n===== ONLINE FOOD ORDERING SYSTEM =====")
        print("1. Show Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Remove Item from Cart")
        print("5. Checkout")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            show_menu()
        elif choice == "2":
            add_to_cart_ui()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            remove_from_cart_ui()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print("👋 Thank you for using our system!")
            break
        else:
            print("❌ Invalid choice! Please select 1-6.")


if __name__ == "__main__":
    main()
