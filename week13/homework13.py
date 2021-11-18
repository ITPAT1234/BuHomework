with open("profile.txt", "r") as profile:
    profileData = profile.read().splitlines()
    profileItem = [i.split() for i in profileData]

def sumIncome(shift):
        income = 0
        for i in shift:
            income += int(i[6])
        return income

def getData(profileItem):
    for i in range(len(profileItem)):
        summary = int(profileItem[i][4]) + (int(profileItem[i][5]) * 0.1)
        profileItem[i].append(summary)
    writedata2file(profileItem)


def writedata2file(profileItem):
    fullTime = [i for i in profileItem if i[3] == "F"]
    partTime = [i for i in profileItem if i[3] == "P"]
    with open("Fulltime.txt", "w") as fullTimefile:
        fullTimefile.write("%40s" % ("SHOW INCOME EMPLOYEE FULLTIME\n"))
        fullTimefile.write("%-3s%-10s%-13s%-9s%-10s%s" %(" ", "NAME", "SURNAME", "SALARY", "SALE", "INCOME\n"))
        fullTimefile.write("%-3s%-10s%-13s%-9s%-10s%s" %(" ", "====", "=======", "======", "====", "======\n"))
        for i in range(len(fullTime)):
            fullTimefile.write("%-13s%-13s%-9s%-10s%.0f\n" % (fullTime[i][1], fullTime[i][2], fullTime[i][4], fullTime[i][5], fullTime[i][6]))
        fullTimefile.write("="*50)
        income = sumIncome(fullTime)
        fullTimefile.write(f"\nTotal Income ={income}")
    with open("Parttime.txt", "w") as partTimefile:
        partTimefile.write("%40s" % ("SHOW INCOME EMPLOYEE PARTTIME\n"))
        partTimefile.write("%-3s%-10s%-13s%-9s%-10s%s" %(" ", "NAME", "SURNAME", "SALARY", "SALE", "INCOME\n"))
        partTimefile.write("%-3s%-10s%-13s%-9s%-10s%s" %(" ", "====", "=======", "======", "====", "======\n"))
        for i in range(len(partTime)):
            partTimefile.write("%-13s%-13s%-9s%-10s%.0f\n" % (partTime[i][1], partTime[i][2], partTime[i][4], partTime[i][5], partTime[i][6]))
        partTimefile.write("="*50)
        income = sumIncome(partTime)
        partTimefile.write(f"\nTotal Income ={income}")


getData(profileItem)
