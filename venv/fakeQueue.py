import random
class fakeQueue:
    def __init__(self):
        self.queue = []
        self.max = 50
    def __str__(self):
        out = ""
        for i in self.queue:
            out +=str(i) + " "
        return out
    def clear(self):
        self.queue[:] = []

    def add(self, x):
        if len(self.queue) == self.max:
            return None
        self.queue.append(x)
    def dequeue(self,numF):
        if not self.queue:
            return (random.randint(0,numF-1))
        return self.queue.pop(0)