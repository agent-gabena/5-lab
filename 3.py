import random
class Dice:
    def __init__(self,facets = 6,count_cubs = 2,Seed = None):
        random.seed(Seed)
        self.facets = facets
        self.count_cubs = count_cubs 
    def cast(self):
        result = []
        for i in range(self.count_cubs):
            result.append(random.randint(1, self.facets))
        return result

def exp(N = 100001):
    all = []
    res = []
    flag = 0
    for i in range(N):
        n = sum(Dice().cast())
        all.append(n)
    for i in range(2,13):
        for el in all:
            if i == el:
                flag+=1
        res.append(flag)
        flag = 0
    for i in range(len(res)):
        print('Частота суммы равной',i+2,' - ',1/res[i])
    return ''
print(exp())
