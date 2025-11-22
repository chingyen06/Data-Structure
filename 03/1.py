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
    
def Finding_LuckyStar(namelist, num):
    q = Queue()

    for i in namelist:
        q.enqueue(i)

    while (q.size() != 1):
        for i in range(num+1):
            move = q.dequeue()

            if (i < num):
                q.enqueue(move)

    return q.front()

if __name__ == "__main__":
    print(f'The lucky star is {Finding_LuckyStar(["Bill","David","Susan","Jane","Kent","Brad"],7)}')