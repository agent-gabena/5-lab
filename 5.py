import secrets
import random
class Password:
    def __init__(self, pas_size = 10, alphabet = ['aalkdjhalkdsjalksjd','12354636','AJDHALKJSDHAK']):
        self.pas_size = pas_size
        self.alphabet = alphabet
    def new_pass(self):
        result = []
        j = 0
        for i in range(self.pas_size):
            rand = (secrets.randbelow(len(self.alphabet[j])))
            result.append((self.alphabet[j])[rand])
            j += 1
            if j > len(self.alphabet)-1:
                j = 0
        random.shuffle(result)
        body = ''.join(result)
        print(body)  
        return None
Password().new_pass()

