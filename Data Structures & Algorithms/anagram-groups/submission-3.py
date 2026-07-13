class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        list1 = [0] * 26 
        for s1 in strs:
            list1 = [0] * 26 
            for s2 in s1:
                char1 = ord(s2) - 97
                list1[char1] += 1

            key1 = tuple(list1)
            dict1[key1].append(s1)
        return(list(dict1.values()))
