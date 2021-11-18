mainLine = "="*30
line2 = "="*91
employMenu = ["Register Employee", "Delete Employee","Show Data Employee", "Exit Program"]
menuNumber = ["1","2","3"]
chooseMenu = "1"
employeeMember = []

def loopMenu():
    for i in range(len(employMenu)):
        print(f"{i+1} {employMenu[i]}")


def header(employMenu):
    print(line2)
    print("%52s" % (employMenu).upper())
    print(line2)

print("%s%s%s" % (mainLine, "Welcome Employee System Program", mainLine))
while chooseMenu in menuNumber:
    loopMenu()
    selectMenu = input("Please select menu[1-3] : ")
    while selectMenu > len(employMenu):
        print("Incorrect menu!!")
        print(line2)
        loopMenu()
        selectMenu = input("Please select menu[1-3] : ")

    if selectMenu == menuNumber[0]:
        header(employMenu[0])
        nameSurname = input("Enter Name Surname : ")
        idCard = input("Enter ID card [13 digits] : ")
        while not len(idCard) == 13 or not idCard.isnumeric():
            print("Invalid ID card!!")
            idCard = input("Enter ID card [13 digits] : ")
        nameAndSur = nameSurname.split(" ")
        username = nameAndSur[0]+"."+nameAndSur[1][0]
        password = nameAndSur[0][1].lower() + nameAndSur[0][3].upper() + nameAndSur[0][2].upper() + str(len(nameSurname)) + nameAndSur[0][4]
        employeeMember.append({"name": nameAndSur[0], "Surname": nameAndSur[1], "Username": username, "Password": password, "IDCard": idCard})
        print("Register Complete")
        print(line2)

    if selectMenu == menuNumber[1]:
        header(employMenu[1])
        employeeName = input("Enter name Employee to delete : ")
        deleteEmployee = [i for i, key in enumerate(employeeMember) if employeeName in key.values()]
        while not deleteEmployee:
            print("Invalid name !!")
            employeeName = input("Enter name Employee to delete : ")
            deleteEmployee = [i for i, key in enumerate( employeeMember) if employeeName in key.values()]
        employeeMember.pop(deleteEmployee[0])
        print("Delete Complete")
        print(line2)

    if selectMenu == menuNumber[2]:
        header(employMenu[2])
        print("%-7s%-17s%-17s%-17s%-17s%s" %("NO.", "Name", "Surname", "Username", "Password", "ID Card"))
        no = 1
        for x in employeeMember:
          print("%-7s%-17s%-17s%-17s%-17s%s" % ( no, x["name"].lower(), x["Surname"].lower(), x["Username"].lower(), x["Password"], x["IDCard"].lower()))
        no += 1
        print(line2)
    if selectMenu == 4:
        print("%s%s%s" % ("="*40, employMenu[3], "="*40))

    chooseMenu = selectMenu