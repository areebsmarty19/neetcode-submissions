class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}
        count=0
        for s1 in s:
            if s1 in dict1:
                dict1[s1]+=1
            else:
                dict1[s1]=0 
        count=0
        for t1 in t:
            if t1 in dict2:
                dict2[t1]+=1
            else:
                dict2[t1]=0     
        if dict1 == dict2:
            return True
        else:
            return False   