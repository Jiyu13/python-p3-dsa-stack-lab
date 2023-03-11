class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0


    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()
        

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        # if not full, pop() .append()
        return len(self.items) == self.limit

    def search(self, target):
        distance = len(self.items) - 1

        for i in range(len(self.items)):
            if target in self.items:
                if self.items[i] != target:
                    distance -= 1
                else:
                    return distance
            else: 
                return -1
            # solution:
            # for i in reversed(range(len(self.items))):
            #     if self.items[i] == target:
            #         return len(self.items) -1  - i 
            # return -1

# stk = Stack([5,6,7,8,9,10])
# print(stk.search(7))