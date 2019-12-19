import random
from itertools import groupby
class fakeQueue:
    def __init__(self):
        self.queue = []
        self.max = 50
        self.min = 0
        self.maxx = 0
    def __str__(self):
        out = ""
        for i in self.queue:
            out +=str(i) + " "
        return out
    def clear(self):
        self.queue[:] = []
    def add4(self,x):
        temp = 0
        if len(self.queue) == self.max:
            return None
        if len(self.queue) == 0:
            self.queue.append(x)
        else:
            for i in self.queue:
                if i != x:
                    temp = 1
                else:
                    temp = 0
                    return
            self.queue.append(x)
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
    def maxim(self,pers):
        temp = []
        for i in pers:
            temp.append(i.getFloor())
        return max(temp)
    def minim(self,pers):
        temp = []
        for i in pers:
            temp.append(i.getFloor())
        return min(temp)

