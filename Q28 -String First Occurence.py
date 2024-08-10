class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
    

s=Solution()
haystack = "sadbutsad"
needle = "sad"
r= s.strStr(haystack,needle)
print(r)
