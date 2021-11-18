line1 = "="*70
print(line1)
print("%50s" % ("Welcome to Grade Calculator"))
print(line1)
studentID = input("Enter student's ID : ")
studentName = input("Enter student's name : ")
studentFaculty = input("Enter student's faculty : ")
print()
subjectList = []
creditList = []
gradeList = []
sumScore = 0
sumCredit = 0

amt = int(input("Enter Subjects Amount : "))
for i in range(amt):
    Subject = input(f"Enter Subject #{i+1} : ")
    Credit = int(input("Enter Credit : "))
    Grade = input("Enter Greade : ").upper()
    subjectList.append(Subject)
    creditList.append(Credit)
    gradeList.append(Grade)
    score = 0
    if Grade == "A":
        score += 4.0
    elif Grade == "B+":
        score += 3.5
    elif Grade == "B":
        score += 3.0
    elif Grade == "C+":
        score += 2.5
    elif Grade == "C":
        score += 2
    elif Grade == "D+":
        score += 1.5
    elif Grade == "D":
        score += 1
    elif Grade == "F":
        score += 0

    if Grade != "W":
        sumScore += score * creditList[i]
        sumCredit += creditList[i]


print(line1)
print("%40s" % ("Grade Report"))
print(line1)
print(f"Student ID .{studentID}")
print(f"Name : {studentName}")
print(f"School : {studentFaculty}")
print(line1)
print("%27s%30s%10s" % ("Subject", "Credit(s)", "Grade"))
print(line1)
for i in range(amt):
  print("%-51s%-13s%s"%(subjectList[i],creditList[i],gradeList[i]))
print(line1)
print("%34s%0.2f"%("GPA.",(sumScore/sumCredit)))
print(line1)
