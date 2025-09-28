class MySet:
    def __init__(self, elements=None):
        self.set_ = set()
    
    def MyAdd(self, element):
        self.set_.add(element)

    def MyRemove(self, element):
        self.set_.discard(element)

    def MyCheck(self, element):
        if element in self.set_:
            return 1
        else:
            return 0
        
    def MyToggle(self, element):
        if element in self.set_:
            self.set_.remove(element)
        else:
            self.set_.add(element)

    def MyAll(self):
        self.set_ = set(range(1, 21))

    def MyEmpty(self):
        self.set_.clear()

import sys
read = sys.stdin.readline

n = int(read())
my_set = MySet()
for i in range(n):
    command = read().strip().split()
    if command[0] == "add":
        my_set.MyAdd(int(command[1]))
    elif command[0] == "remove":
        my_set.MyRemove(int(command[1]))
    elif command[0] == "check":
        print(my_set.MyCheck(int(command[1])))
    elif command[0] == "toggle":
        my_set.MyToggle(int(command[1]))
    elif command[0] == "all":
        my_set.MyAll()
    elif command[0] == "empty":
        my_set.MyEmpty()