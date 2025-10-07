import sys

read = sys.stdin.read

a,b = int(read().split())

a_s = set()
b_s = set()

a_s.add(int(read().split))
b_s.add(int(read().split))

if a > b:
    print(len(a_s - b_s))
else:
    print(len(b_s - a_s))