class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
        strs1={}
        strs.sort()
        for org_string in strs:
            dup_string = sorted(org_string)
            key="".join(dup_string)
            if key in strs1:
                strs1[key].append(org_string)
            else:
                strs1[key]=[org_string]
        result=list(strs1.values())
        return(result)
        