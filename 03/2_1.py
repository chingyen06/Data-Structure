# Queue class: can be implemented using a list in Python
class Queue:
    def __init__(self):
        self.queue = list()
        self.t = 0

    def isEmpty(self):
        return self.t == 0

    def enqueue(self, item):
        self.queue.append(item)
        self.t += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        self.t -= 1
        return self.queue.pop(0)

    def front(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

def Binary_Code_Generator(n):
    # n denotes the length of the bit string
    result = []
    q = Queue()

    q.enqueue("0")
    q.enqueue("1")

    '''
    一開始先把 queue 設為 [0, 1]
    當 queue 不是空的話就將第一個元素取出
    當 queue 中的元素有一個已經滿 n-bit，就把它放到 result 中
    否則就把它後面分別接 0、1 再放回 queue 中
    當 queue 是空的話就代表所有可能為 n-bit 的數字都產生完了
    '''

    while (q.isEmpty() == False):
        pre_q = q.dequeue()

        if (len(pre_q) == n):
            result.append(pre_q)
            continue

        q.enqueue(pre_q + "0")
        q.enqueue(pre_q + "1")

    return result

if __name__ == "__main__":
    n = int(input("Please enter the number of bits for the binary codes: "))
    B = Binary_Code_Generator(n)
    for i in range(len(B)):
         print(f'{B[i]}', end='\n')