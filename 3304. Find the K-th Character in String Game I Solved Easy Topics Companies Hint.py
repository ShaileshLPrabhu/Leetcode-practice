class Solution:
    def generate(self,word:str)->str:
        new_str =''
        for i in word:
            new_str+=chr(ord(i)+1)
        return new_str
    
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        while len(word)<=k:
            word+= self.generate(word)
    
        return word[k-1]