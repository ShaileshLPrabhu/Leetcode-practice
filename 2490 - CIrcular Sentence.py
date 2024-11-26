class Solution:
    def isCircularSentence(self, sentence: str) -> bool:   
        words = sentence.split(' ')
        if len(words) == 1:
            return sentence[0]==sentence[-1]
        i=0
        while i in range(0,len(words)):
            if i == len(words)-1:
                break

            if words[i][-1]!= words[i+1][0]:
                return False
            i+=1
            
        return words[-1][-1]==words[0][0]