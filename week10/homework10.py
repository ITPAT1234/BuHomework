gradeList = []
scoreList = []

with open("profile.txt", "r")as profile, open("midterm.txt", "r")as midterm, open("final.txt", "r")as final:
    profileData = profile.read().splitlines()
    midtermData = midterm.read().splitlines()
    finalData = final.read().splitlines()
    profileData.sort()
    midtermData.sort()
    finalData.sort()
    for i in range(len(midtermData)):
        midtermItem = midtermData[i].split()
        finalItem = finalData[i].split()
        scoreList.append(float(midtermItem[1]) + float(finalItem[1]))
    for i in scoreList:
        if i >= 80 and i <= 100:
            gradeList.append("A")
        if i >= 70 and i <= 79:
            gradeList.append("B")
        if i >= 60 and i <= 69:
            gradeList.append("C")
        if i >= 50 and i <= 59:
            gradeList.append("D")
        if i <= 50:
            gradeList.append("F")
with open("gradereport.txt", "w") as report:
    for i in range(len(profileData)):
        profileItem = profileData[i].split()
        profileItem.pop(4)
        report.write("%-9s%-30s%-5s%-8.2f%-7s%s" % (
            profileItem[0], profileItem[1]+" "+profileItem[2], profileItem[3], scoreList[i], "Grade", gradeList[i]+"\n"))
