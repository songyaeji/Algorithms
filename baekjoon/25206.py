import sys

# [[course, credit, gpa],[course, credit, gpa]]
gpaList = [list(map(input().split()))]

for oneList in gpaList:
    for course, credit, gpa in oneList:
        if gpa == "P":
            del oneList
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
    for course, credit, gpa in oneList:
        sumCredit += credit
        sumGPA = credit*gpa

totalGPA = sumGPA/sumCredit
print(totalGPA)