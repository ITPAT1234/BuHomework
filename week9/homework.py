with open("student.txt", "r") as student, open("male.txt", "w")as male, open("female.txt", "w")as female:
    readStudent = student.read().splitlines()
    for i in readStudent:
        studentList = i.split()
        if studentList[6] == "M":
            male.write(i+"\n")
        else:
            female.write(i+"\n")
