class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}
        count=0
        for s1 in s:
            if s1 in dict1:
                count = dict1[s1]
                count+=1
                dict1[s1] = count
            else:
                dict1[s1]=0 
        count=0
        for t1 in t:
            if t1 in dict2:
                count = dict2[t1]
                count+=1
                dict2[t1] = count
            else:
                dict2[t1]=0     
        if dict1 == dict2:
            return True
        else:
            return False   