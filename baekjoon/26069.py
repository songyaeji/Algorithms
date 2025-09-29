import sys
read = sys.stdin.readline

rainbow = set()
rainbow.add("ChongChong")

n = int(read())
for i in range(n):
    people = read().strip().split()
    if people[0] in rainbow and people[1] not in rainbow:
        rainbow.add(people[1])
    elif people[1] in rainbow and people[0] not in rainbow:
        rainbow.add(people[0])

print(len(rainbow))