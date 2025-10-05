import sys
read = sys.stdin.readline

def decryption(count, public1, public2, encrypted):
    decrypted = []
    for i in range(count):
        for j in range((count)):
            if public1[i] == public2[j]:
                decrypted.append(encrypted[j])
    print(*decrypted)

n = int(read())
for i in range(n):
    count = int(read())
    public1 = read().strip().split()
    public2 = read().strip().split()
    encrypted = read().strip().split()
    decryption(count, public1, public2, encrypted)