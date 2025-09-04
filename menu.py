# menu.py

menu = {
    1: {"name": "Burger", "price": 150},
    2: {"name": "Pizza", "price": 300},
    3: {"name": "Pasta", "price": 200},
    4: {"name": "Fried Chicken", "price": 250},
    5: {"name": "Coke", "price": 50}
}


def show_menu():
    print("\n------ MENU ------")
    for key, value in menu.items():
        print(f"{key}. {value['name']} - {value['price']} BDT")
