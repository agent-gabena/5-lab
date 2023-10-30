import random
import secrets
class Dice:
    def __init__(self, name_size = 5, expansion = '.txt',facets = 6,count_cubs = 2,Seed = None):
        random.seed(Seed)
        self.facets = facets
        self.count_cubs = count_cubs
        self.expansion = expansion
        self.name_size = name_size
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','y','w','x','z'] 
    def cast(self):
        result = []
        for i in range(self.count_cubs):
            result.append(random.randint(1, self.facets))
        return result
    def file_name(self):
        result = []
        for i in range(self.name_size):
            rand = (secrets.randbelow(len(self.alphabet)))
            result.append(self.alphabet[rand])
        body = ''.join(result) + '.' + self.expansion 
        print(body)
Dice(expansion='py', name_size=10).file_name()
