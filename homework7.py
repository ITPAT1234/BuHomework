chooseMenu = ""
price = 0

while chooseMenu != "E":
    print("Menu : H = Hamburger, P = Pizza, W = Water, E = Exit")
    chooseMenu = input("Choose Menu (H,P,W,E=Exit) : ").upper()
    if chooseMenu == "H":
        amount = int(input("Enter Amount : "))
        price += 100 * amount
    elif chooseMenu == "P":
        amount = int(input("Enter Amount : "))
        price += 200 * amount
    elif chooseMenu == "W":
        amount = int(input("Enter Amount : "))
        price += 300 * amount
    elif chooseMenu == "E":
        print()
        print(f"Total price = {price} baths")
    else:
        print("Please try again...")
        break
    print()
    chooseMenu = chooseMenu
