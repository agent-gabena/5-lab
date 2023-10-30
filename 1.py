import random
class Dice:
    def __init__(self,facets = 6,count_cubs = 1):
        self.facets = facets
        self.count_cubs = count_cubs 
    def cast(self):
        result = []
        for i in range(self.count_cubs):
            result.append(random.randint(1, self.facets))
        print(result, sep='\n') 
First_Cast = Dice(facets=10, count_cubs=3)
First_Cast.cast()
