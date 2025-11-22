# Stack class: can be implemented using a list in Python
class Stack:
    def __init__(self):
        self.stack = list()
        self.t = 0

    def isEmpty(self):
        return self.t == 0

    def push(self, item):
        self.stack.append(item)
        self.t += 1

    def pop(self):
        if self.isEmpty():
            return None
        self.t -= 1
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def size(self):
        return self.t
    
# Queue class: can be implemented using a list in Python
class Queue:
    def __init__(self):
        self.queue = list()

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def front(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)
    
def Gray_Code_Generator(n):
    result = []
    s = Stack()

    s.push("0")
    s.push("1")

    # 從 2 到 n
    for i in range(2, n + 1):
        reverse_s = Stack()
        copy_s = Stack()
        
        # 反轉 stack (stack 是後進先出，所以要用另一個 stack 來反轉)
        while (s.isEmpty() == False):
            pre_s = s.pop()
            copy_s.push(pre_s)  # 先反轉後的順序到 copy_s 中
            reverse_s.push(pre_s)

        # 反轉後的 copy_s 再反轉即可恢復原本的 stack
        while (copy_s.isEmpty() == False):
            pre_s = copy_s.pop()
            s.push(pre_s)

        original_stack = Queue()
        reverse_stack = Queue()

        # 原始的 stack 前面加 1 (stack 已經改變順序 [0, 1] -> [1, 0])
        while (s.isEmpty() == False):
            pre_s = s.pop()
            original_stack.enqueue("1" + pre_s)

        # 反轉的 stack 前面加 0 (stack 已經改變順序 [1, 0] -> [0, 1])
        while (reverse_s.isEmpty() == False):
            pre_s = reverse_s.pop()
            reverse_stack.enqueue("0" + pre_s)

        # 把兩個 stack 合併回 s
        while (reverse_stack.isEmpty() == False):
            s.push(reverse_stack.dequeue())
        while (original_stack.isEmpty() == False):
            s.push(original_stack.dequeue())

    while (s.isEmpty() == False):
        result.insert(0, s.pop())
    
    return result

if __name__ == "__main__":
    n = int(input("Please enter the number of bits for the binary codes: "))
    B = Gray_Code_Generator(n)
    for i in range(len(B)):
         print(f'{B[i]}', end='\n')