class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        words = sentence.split(' ')
        l = len(searchWord)
        for i in range(len(words)):
            if words[i][:l] == searchWord:
                return i+1
        
        return -1
