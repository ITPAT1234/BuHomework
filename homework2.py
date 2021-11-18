line1 = ("="*45)
line2 = ("-"*45)


def destTable():
    print(line1)
    print("%-5s%-10s%-8s%-8s%-6s%-5s%3s" %
          ("|", "Weight", "|", "BK", "|", "TH", "|"))
    print(line2)
    print("%-5s%-10s%-8s%-7s%-6s%-5s%3s" %
          ("|", "1-5", "|", "80", "|", "140", "|"))
    print("%-5s%-10s%-8s%-8s%-6s%-5s%3s" %
          ("|", "6-10", "|", "150", "|", "200", "|"))
    print("%-5s%-10s%-8s%-8s%-6s%-5s%3s" %
          ("|", "10+", "|", "200", "|", "250", "|"))
    print(line1)


def cal(order, shipping, discount):
    print()
    print("%-11s : %7.2f" % ("Order Total", order))
    print("%-11s :  %5.2f" % ("Shipping", shipping))
    print("%-11s : %7.2f" % ("Discount", -discount))
    print(line1)
    total = order + shipping - discount
    print("%-11s : %0.2f" % ("Total", total))
    print(line1)


print(line1)
print("|%10s >>> Order Summary <<< %10s|" % (" ", " "))
print(line2)
order = float(input("Enter Order total : "))
if order >= 3000 and order <= 5000:
    discount = 60
elif order >= 5000:
    discount = 120
else:
    discount = 0
print(line2)
print("| >>> Destination <<<%23s|" % (" "))
print("|%2s(BK) The Bangkok Metropolitan Region%5s|" % (" ", " "))
print("|%2s(TH) For areas in other provinces%8s|" % (" ", " "))
print(line2)
dest = input("Enter destination  : ").upper()
if dest == "BK" or dest == "TH":
    if dest == "BK":
        weight = int(input("Enter total weight(KG) : "))
        destTable()
        if weight >= 1 and weight <= 5:
            shipping = 80
        elif weight >= 6 and weight <= 10:
            shipping = 150
        elif weight > 10:
            shipping = 200
        else:
            shipping = 0
        cal(order, shipping, discount)
    elif dest == "TH":
        weight = int(input("Enter total weight(KG) : "))
        destTable()
        if weight >= 1 and weight <= 5:
            shipping = 140
        elif weight >= 6 and weight <= 10:
            shipping = 200
        elif weight < 10:
            shipping = 250
        else:
            shipping = 0
        cal(order, shipping, discount)
else:
    print("Invalid destination code! Please try again.")