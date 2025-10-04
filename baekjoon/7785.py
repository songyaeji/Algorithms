import sys
read = sys.stdin.readline

workingSet = set()

n = int(read())
for i in range(n):
    name, command = read().strip().split()
    if command == "enter":
        workingSet.add(name)
    elif command == "leave":
        workingSet.discard(name)

answer = sorted(workingSet, reverse=True)

print(*answer, sep='\n')