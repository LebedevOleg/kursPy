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
        try:
            return self.queue.pop(random.randint(0,len(self.queue)-1))
        except:
            return random.randint(0,numF-1)
    def maxcount(self,numF):
        temp = 0
        n = 0
        #x = 0
        for i in range(0,numF):
            if temp < self.queue.count(i):
                n = i
                temp = self.queue.count(i)
                #x = self.queue.index(n)
        self.queue = list(filter(lambda a: a!=n,self.queue))
        return n