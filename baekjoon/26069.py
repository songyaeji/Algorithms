import sys
read = sys.stdin.readline

rainbow = set()
rainbow.add("ChongChong")

n = int(read())
for i in range(n):
    people = read().strip().split()
    if people[0] == "ChongChong":
        rainbow.add(people[1])
    rainbow.add(people[1])

print(len(rainbow))