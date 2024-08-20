#Leet code solution to find length of the last word in string
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst= s.strip().split(" ")
        
        return len(lst[-1])

s = "Hello World"
print(Solution().lengthOfLastWord(s))