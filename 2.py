import random
class Dice:
    def __init__(self,facets = 6,count_cubs = 1,Seed = None):
        random.seed(Seed)
        self.facets = facets
        self.count_cubs = count_cubs 
    def cast(self):
        result = []
        for i in range(self.count_cubs):
            result.append(random.randint(1, self.facets))
        print(result, sep='\n') 
First_Cast = Dice(count_cubs= 3,Seed=1)
First_Cast.cast()
Second_Cast = Dice(count_cubs= 3,Seed=1)
Second_Cast.cast() 
