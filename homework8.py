line = "="*70
print(line)
print("%43s" % ("BU Restaurant"))
print("%38s" % ("Menu"))
print(line)
menuId = ["F01", "F02", "F03", "F04", "D01", "D02", ]
allMenu = ["Pan Fried Egg", "Grilled Sandwich",
           "Spaghutti Olio", "Caesar Salad", "Coffee", "Soft Drink"]
Price = [125, 145, 169, 139, 120, 90]
QTY = []
menu_List = []
priceList = []
drinkPrice = 0
Quit = "N"
print("%-34s%-27s%s" % ("Menu ID", "Menu", "Price"))
for i in range(len(menuId)):
    print("%2s%-28s%-32s%s" % (" ", menuId[i], allMenu[i], Price[i]))
print(line)

if Quit == "N":
    while Quit == "N":
        menuIdInput = input("Enter Menu ID : ").upper()
        while menuIdInput not in menuId:
            print("Invalid Code! Please try again...")
            menuIdInput = input("Enter Menu ID : ").upper()
        quantity = int(input("Enter quantity : "))
        Quit = input("Quit (Y/N) : ").upper()
        QTY.append(quantity)
        for i in range(len(menuId)):
            if menuIdInput == menuId[i]:
                menu_List.append(allMenu[i])
                priceList.append(Price[i] * quantity)
                print()
            if menuIdInput == menuId[4]:
                drinkPrice = Price[4] * quantity
            if menuIdInput == menuId[5]:
                drinkPrice = Price[5] * quantity
if Quit == "Y":
    print(line)
    member = input("BU Member Card (Y/N): ")
    if member.upper() == 'Y':
        discount = (sum(priceList)-drinkPrice) * 0.1
    elif member.upper() == 'N':
        discount = 0
    tax = sum(priceList) * 0.07
    print(line)
    print("%18sBU Restaurant%18s" % (" ", " "))
    print("%21sReceipt%21s" % (" ", " "))
    print(line)
    print("%5sMenu%14sQTY%14sPrice" % (" ", " ", " "))
    for a in range(len(menu_List)):
        print("%-24s%-17s%s" % (menu_List[a], QTY[a], priceList[a]))
    print(line)
    print("Price%35s%0.2f" % (" ", sum(priceList)))
    print("Discount (only food)%20s-%-20.2f" % (" ", discount))
    print("Tax(%s)%35s%0.2f" % ("7%", " ",tax ))
    print("Total%35s%0.2f" % (" ", sum(priceList)-discount+tax))
    print(line)
else:
    print("Please Try again...")
