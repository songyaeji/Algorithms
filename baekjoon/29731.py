promise = ["Never gonna give you up",
           "Never gonna let you down",
           "Never gonna run around and desert you",
           "Never gonna make you cry",
           "Never gonna say goodbye",
           "Never gonna tell a lie and hurt you",
           "Never gonna stop"]

import sys
read = sys.stdin.readline

n = int(read())
done = 0

for i in range(n):
    sentence = read().strip()
    if sentence in promise:
        continue
    else:
        print("Yes")
        done += 1
        break

if done == 0:
    print("No")