import random as rd

line1 = ("="*60)

print(line1)
print("|%23s Welcome to %23s|"%(" "," "))
print("|%15s Program Password Generator %15s|"%(" "," "))
print(line1)

def login():    
    condition = "N"
    print("|%18sPlease Select the menu%18s|"%(" "," "))
    print("|%23s1 = Login%26s|"%(" "," "))
    print("|%23s2 = Register%23s|"%(" "," "))
    print(line1)
    while True:    
        reg = input("Please Choose menu (1-2) : ")
        if reg == "1":
            print(line1)
            print("|%26sLogin%27s|"%(" "," "))
            print(line1)
            print("Please Enter your Username & Password")
            user = input("Username : ")
            passw = input("Password : ")
            f = open("users.txt", "r")
            for line in f.readlines():
                us, pw = line.strip().split("|")
                if (user in us) and (passw in pw):
                    print(line1)
                    print("Login successful!")
                    menu()
            print(line1)
            print("Wrong username/password")
            print("Please try again")
            print(line1)
            print("|%18sPlease Select the menu%18s|"%(" "," "))
            print("|%23s1 = Login%26s|"%(" "," "))
            print("|%23s2 = Register%23s|"%(" "," "))
            print(line1)
        elif reg == "2":
            print(line1)
            print("|%25sRegister%25s|"%(" "," "))
            print(line1)
            user = input("Create your Username: ")
            passw = input("Create your Password: ")
            with open("users.txt","a") as usera:
                usera.write("\n%s|%s"%(str(user),str(passw)))
            print(line1)
            print("|%19sRegister successful!%19s|"%(" "," "))
            menu()
        else:
            print("Invalid menu")
        return False
            
def menu():
    
    passwordsaved_list = []
    chars = "abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ123456789!$@%#&"
    
    def print1():
        print(line1)
        print("|%24s>> Menu <<%24s|"%(" "," "))
        print("|%18s 1 = Password Generator %16s|"%(" "," "))
        print("|%18s 2 = Password list %21s|"%(" "," "))
        print("|%18s 3 = Save to File %22s|"%(" "," "))
        print("|%18s 4 = Exit %30s|"%(" "," "))
        print(line1)

    def pg():
        condition = "N"
        print(line1)
        print("|%19s Password Generator %19s|"%(" "," "))
        print(line1)
        while condition == "N" :
            if condition == "N":
                password_len = int(input("What length would you like your password to be? : "))
                password_count = int(input("How many passwords would you like? : "))
                for x in range(0,password_count):
                    password = ""
                    for x in range(0,password_len):
                        password_char = rd.choice(chars)
                        password = password + password_char
                    passwordsaved_list.append(password)  
                    print("Here your password : %s"%(password))
                print(passwordsaved_list)
                save = input("Do you want to save this password? (Y/N) : ")
                if save.upper() == "N":
                    for i in range(password_count):
                        passwordsaved_list.pop()
                    print(passwordsaved_list)
                    condition = input("Quit(Y/N) : ").upper()
                elif save.upper() == "Y":
                    condition = input("Quit(Y/N) : ").upper()
    
    def pl():
        print(line1)
        print("|%19s Password Lists %19s|"%(" "," "))
        print(line1) 
        for a in range(len(passwordsaved_list)):
            print("%-8s%-12s"%(a+1,passwordsaved_list[a]))
        print(line1)
    
    def wf():
        print(line1)
        print("|%23sSave to File%23s|"%(" "," "))
        print(line1)
        with open("saved.txt","w") as saved:
            print()
    
    print1()
    
    while True:
        choose = input("Please Choose menu (1-4) : ")
        if choose.upper() == "1":    
            pg()
            print1()
        elif choose.upper() == "2":
            pl()
            print()
        elif choose.upper() == "3":
            wf()
        elif choose.upper() == "4":
            print("Thank you for use my Program :)")
            break
        else:
            print("Invalid menu")
            

first = True

if first == True:
    first = login()

