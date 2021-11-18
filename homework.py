longline = "="*35
R = "Rectangle"
T = "Trapezoid"
P = "Parallelogram"
C = "Cicle"
print(longline)
print("| *** Area Calculator Program *** |")
print(longline)
print("|       Shape code list :         |")
print("|       (R) %2s             |" % (R))
print("|       (T) %2s             |" % (T))
print("|       (P) %2s         |" % (P))
print("|       (C) %2s                 |" % (C))
print(longline)


def Rectangle(res, unit):
    sumRectangle = res[0] * res[1]
    formatOutput(sumRectangle, unit)


def Traoezoid(res,  unit):
    sumTraoezoid = (((res[0]+res[1])*res[2])/2)
    formatOutput(sumTraoezoid, unit)


def Parallelogram(res, unit):
    sumParallelogram = res[0] * res[1]
    formatOutput(sumParallelogram, unit)


def Circle(res, unit):
    sumCircle = ((22/7)*(res[0]**2))
    formatOutput(sumCircle,  unit)


def loopInput(number, v):
    re = []
    for i in range(number):
        Ln = int(input("Enter your %s : " % (v[i])))
        re.append(Ln)
    return re


def sum(number, formula, v, unit):  # loop input and send Data to formula
    re = loopInput(number, v)
    formula(re, unit)


def formatOutput(res, unit):
    print(longline)
    print("%13s = %0.2f %2s" % ("Area", res, unit))
    print(longline)


def checkInput(sum, number, Code, formula, v):  # check input that it is 1 or 2
    print(longline)
    print("%14s of %2s" % ("Area", Code))
    print(longline)
    if len(v) == 2:
        print("Inputs width and height in cm. or m.")
    elif len(v) == 3:
        print("Inputs parallel sides and height in cm. or m.")
    else:
        print("Inputs radius in cm. or m.")
    In_Cm = input("select a unit code 1 (cm.) or 2 (m.) : ")
    Cm = "Cm2"
    M = "M2"
    if In_Cm == "1":
        sum(number, formula, v, Cm)
    elif In_Cm == "2":
        sum(number, formula, v, M)
    else:
        print("Please Try again")


inputCode = input("Select Code [R,T,P,C] : ").upper()  # upper input
if inputCode == "R":
    v = ["width", "heigth"]
    print("you select %s = %s" % (inputCode, R))
    checkInput(sum, 2, R, Rectangle, v)
elif inputCode == "T":
    v = ["sideA", "sideB", "height"]
    print("you select %s = %s" % (inputCode, T))
    checkInput(sum, 3, T, Traoezoid, v)
elif inputCode == "P":
    v = ["base", "height"]
    print("you select %s = %s" % (inputCode, P))
    checkInput(sum, 2, P, Parallelogram, v)
elif inputCode == "C":
    v = ['radius']
    print("you select %s = %s" % (inputCode, C))
    checkInput(sum, 1, C, Circle, v)
else:
    print("you select %s is Invalid shape Code !" % (inputCode))
    print("Please Try again")
