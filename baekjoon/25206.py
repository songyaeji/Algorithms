# [[course, credit, gpa],[course, credit, gpa]]
gpaList = []

for _ in range(20):
    course, credit, gpa = input().split()
    if gpa == "P":
        continue
    else:
        gpaList.append([str(course), float(credit), str(gpa)])

gpaMap = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

sumCredit = 0.0
sumGPA = 0.0
for oneList in gpaList:
    oneList[2] = gpaMap[oneList[2]]
    sumCredit += oneList[1]
    sumGPA += oneList[1]*oneList[2]

totalGPA = float(sumGPA)/float(sumCredit)
print(totalGPA)