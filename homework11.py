def dyInput(number, unit):
    result = []
    for i in range(number):
        result.append(float(input("Enter %s : " % (unit[i]))))
    return result


def circle(number, unit):
    result = dyInput(number, unit)
    print(f"Triangle Area = {(22/7*(result[0]**2)):.2f}")


def triangle(number, unit):
    result = dyInput(number, unit)
    print(f"Circle Area = {((result[0]*result[1])/2):.2f}")


def rectangle(number, unit):
    result = dyInput(number, unit)
    print(f"Rectangle Area = {(result[0]*result[1]):.2f}")


while True:
    print("C: Circle Area | T: Triangle Area | R: Rectangle Area | E: Exit")
    menu = input("Enter menu : ").upper()
    if menu == "C":
        circle(1, ["radius"])
    if menu == "T":
        triangle(2, ["base", "height"])
    if menu == "R":
        rectangle(2, ["width", "height"])
    if menu == "E":
        print("Exit Program")
        break
