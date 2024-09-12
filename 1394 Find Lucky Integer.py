from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt =Counter(arr)
        lucky =[]
        for key in cnt:
            if key== cnt[key]:
                lucky.append(cnt[key])

        if(len(lucky)==0):
            return -1
        return max(lucky)
