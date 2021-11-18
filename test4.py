with open("users.txt", "r") as file:
    data = file.read().splitlines()
    dataItem = [i.split("|") for i in data]

user = "pat"
password = "pat"
print(dataItem)

for i in dataItem:
    for x in i:
        if x == user and x == password :
            print("HI")
