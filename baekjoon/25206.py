# [[course, credit, gpa],[course, credit, gpa]]
gpaList = [list(input().split()) for _ in range(20)]

for oneList in gpaList:
    oneList[1] = float(oneList[1])
    gpa = oneList[2]
    if gpa == "P":
        gpaList.remove(oneList)
    elif gpa == "A+":
        gpa = 4.5
    elif gpa == "A0":
        gpa = 4.0
    elif gpa == "B+":
        gpa = 3.5
    elif gpa == "B0":
        gpa = 3.0
    elif gpa == "C+":
        gpa = 2.5
    elif gpa == "C0":
        gpa = 2.0
    elif gpa == "D+":
        gpa = 1.5
    elif gpa == "D0":
        gpa = 1.0
    else:
        gpa = 0.0


sumCredit = 0.0
sumGPA = 0.0
for oneList in gpaList:
    credit = oneList[1]
    gpa = oneList[2]
    sumCredit += credit
    sumGPA += credit*gpa

totalGPA = float(sumGPA)/float(sumCredit)
print(totalGPA)