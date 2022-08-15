item = 0
discount = 0.1
totalprice = 0
cart = {}
itemquantity = 1
finalpayabnle = 0.00

dairy = {"Milk": 2.30, "Butter": 4.50,
         "Eggs": 3.40, "Cheese slices": 3.15,
         "Evaporated Milk Creamer": 1.40, "Milo": 12.50,
         "Biscuits": 5.30, "Yogurt": 0.95}


def print_inventory(dairy):
    print("----- Dairy Items ----- ")
    print()
    for item, amount in dairy.items():
        print("{:<25s} | ${:<15.2f}".format(item, amount))


pgoods = {"Bread": 2.70, "Cereal": 7.00,
          "Crackers": 3.10, "Chips": 2.60,
          "Raisin": 2.10, "Nuts": 2.00,
          "Green Bean": 1.05, "Barley": 1.05}


def print_inventory(pgoods):
    print("----- Packed Goods Items -----")
    print()
    for item, amount in pgoods.items():
        print("{:<25s} | ${:<15.2f}".format(item, amount))


cgoods = {"Tomato": 1.45, "Button Mushroom": 1.15,
          "Baking Bean": 1.35, "Tuna Fish": 1.45,
          "Kernel Corn": 1.25, "Sardine Fish": 1.25,
          "Chicken Luncheon Meat": 1.95, "Pickled Lettuce": 0.95}


def print_inventory(cgoods):
    print("----- Canned Goods Items ----- ")
    print()
    for item, amount in cgoods.items():
        print("{:<25s} | ${:<15.2f}".format(item, amount))

sauce = {"Fine Salt": 0.80, "Sea Salt Flakes": 1.30,
         "Chicken Stock": 3.15, "Chilli Sauce": 2.65,
         "Oyster Sauce": 4.50, "Sweet Soy Sauce": 3.75,
         "Tomato Ketchup": 3.20, "Sesame Oil": 4.95}


def print_inventory(sauce):
    print("----- Condiments/Sauces Items -----")
    print()
    for item, amount in sauce.items():
        print("{:<25s} | ${:<15.2f}".format(item, amount))


drink = {"Green Tea Canned 330 ML": 15.00, "Blackcurrant Ribena 330 ML": 31.00,
         "100 Plus 24 Cans": 15.00, "Orange Cordial 2 Litre": 3.90,
         "Mineral Water 24 x 600 ML": 7.00, "Pineapple juice": 0.80,
         "Nescafe Coffee": 9.90, "Coke 24 Cans": 12.40}


def print_inventory(drink):
    print("Drink & Beverages Items: ")
    print("--------------------------")
    print()
    for item, amount in drink.items():
        print("{:<25s} | ${:<15.2f}".format(item, amount))


allgro = {"Milk": 2.30, "Butter": 4.50, "Eggs": 3.40, "Cheese slices": 3.15,
          "Evaporated Milk Creamer": 1.40, "Milo": 12.50, "Biscuits": 5.30, "Yogurt": 0.95, "Bread": 2.70,
          "Cereal": 7.00,
          "Crackers": 3.10, "Chips": 2.60, "Raisin": 2.10, "Nuts": 2.00, "Green Bean": 1.05, "Barley": 1.05,
          "Tomato": 1.45,
          "Button Mushroom": 1.15, "Baking Bean": 1.35, "Tuna Fish": 1.45, "Kernel Corn": 1.25, "Sardine Fish": 1.25,
          "Chicken Luncheon Meat": 1.95, "Pickled Lettuce": 0.95, "Fine Salt": 0.80, "Sea Salt Flakes": 1.30,
          "Chicken Stock": 3.15, "Chilli Sauce": 2.65, "Oyster Sauce": 4.50, "Sweet Soy Sauce": 3.75,
          "Tomato Ketchup": 3.20, "Sesame Oil": 4.95, "Green Tea Canned 330 ML": 15.00,
          "Blackcurrant Ribena 330 ML": 31.00,
          "100 Plus 24 Cans": 15.00, "Orange Cordial 2 Litre": 3.90, "Mineral Water 24 x 600 ML": 7.00,
          "Pineapple juice": 0.80,
          "Nescafe Coffee": 9.90, "Coke 24 Cans": 12.40}

def mainmenu():
    while True:
        print("Welcome to your shopping list! What would you like to do today? (1-7)\n"
              "\n"
              "1. View available item Categories\n"
              "2. View Grocery List in alphabetical order\n"
              "3. View items in Ascending price\n"
              "4. View items in your Cart\n"
              "5. Add items in your Cart\n"
              "6. Remove an item from your Cart\n"
              "7. Proceed to Checkout")
        search = int(input("Choose an action: "))
        try:
            if search == 1:
                return additem()
            elif search == 2:
                sort_alpha()
            elif search == 3:
                ascendprice(allgro)
            elif search == 4:
                view_cart()
            elif search == 5:
                additem()
            elif search == 6:
                delete()
            elif search == 7:
                cal()
                checkout()
        except ValueError:
            print("Your input is invalid.")
            break

def additem():
    while True:
        print(
            "Categories:\n1. Dairy\n2. Packaged Goods\n3. Canned Goods\n4. Condiments/Sauces\n5. Drink & "
            "Beverages\n6. Return to Main Menu")
        catview = int(input("What category would you like to view? (1-6): "))
        if catview == 1:
                print(print_inventory(dairy))
        elif catview == 2:
                print(print_inventory(pgoods))
        elif catview == 3:
                print(print_inventory(cgoods))
        elif catview == 4:
                print(print_inventory(sauce))
        elif catview == 5:
                print(print_inventory(drink))
        elif catview == 6:
                return mainmenu()
        else:
            print("Your input is invalid. Please try again.")
        add = input("Which item do you want to add into your cart? ('None' if you don't want anything): ")
        if add in allgro:
            thing = allgro.get(add)
            cart[str(add)] = thing
            print("{} has been added.".format(add))
            itemquantity = int(input("How many units of {} would you like?".format(add)))
            cart[str(add)] = itemquantity
            print("You've added {} units of {} into your cart!".format(itemquantity, add))
            cont = input("Would you like the continue shopping? (Y/N): ")
            if cont == "Y" or "y" or "Yes" or "YES":
                continue
            elif cont == "N" or "n" or "no" or "NO":
                return mainmenu()
            else:
                print("Please enter a valid input. Thank you!")
                return
        elif add not in allgro:
            print("Your item is not in our grocery. Please try again.")
            return
        # this doesn't work
        elif add == "None" or "none" or "NONE":
            return additem()

def sort_alpha():
    alpha_dict = allgro.items()
    new_alpha = sorted(alpha_dict)
    print(new_alpha)
    for key, value in new_alpha:
        print("{:<25s} | {:<15.2f}".format(key, value))

def ascendprice(allgro):
    sort_ascend = sorted(allgro.items(), key=lambda x: x[1])
    for key, value in sort_ascend:
        print("{:<25s} | {:<15.2f}".format(key, value))

def view_cart():
    if len(cart) == 0:
        print("Your cart is empty! Returning to main menu now...")
    elif len(cart) > 0:
        print("{:^50s}" .format("-------- Your Cart ---------"))
        print("{:^15s} | {:^15s} | {:^15s}" .format("Item", "Price", "Quantity"))
        print("{:<25s} | {:<15.2f} | {:<15d}" .format(cart.keys, cart.values, itemquantity))
        print(cart)

def delete():
    if len(cart) == 0:
        print("Your cart is empty! Returning to main menu now...")
    elif len(cart) > 0:
        removingitem = input("What do you want to remove from your cart?: ")
    if removingitem in cart:
        del cart[what]
    print("You have removed {} from your Cart.".format(removingitem))


def cal():
    if len(cart) == 0:
        print("Your cart is empty! Going back to main menu now...")
        return mainmenu()

    print("{:^25s}" .format("------- Checkout -------"))
    print()
    cart = tuple(cart.items)
    card = input("Do you have a discount card? Y/N: ")
    if card == "Yes" or "Y" or "yes" or "y" or "YES":
        discount = totalprice * 0.9
        gst = discount * 0.7
        finalpayable = gst + discount
    elif card == "No" or "N" or "no" or "n" or "NO":
        # totalprice =
        gst = totalprice * 0.7
        discount = 0.00
        finalpayable = gst + totalprice + discount
    else:
        print("Your input is invalid. Please try again.")



def receipt():
    print("{:^10s}\n"
          "--------------------".format("Shopping List Receipt"))
    for item, amount in cart.items():
        print("{:<25s} | ${:<15.2f}" .format("Item", "Price", "Quantity"))
        print("{:<25s} | ${:<15.2f} | {:<15d} ".format(item, amount, itemquantity))
    print("Sub Total: {:<15.2f}\n"
          "Members' Discount (if applicable): {:<15.2f}\n"
          "GST (7%) : {:<15.2f}\n"
          "--------------------\n"
          "TOTAL: {:<15.2f}\n".format(totalprice, discount, 0, 0))


mainmenu()
