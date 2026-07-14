class Solution:

    def encode(self, strs: List[str]) -> str:
        enstr=""
        for s in strs:
            en1 = s + "&@ap"
            enstr += en1 
        return enstr

    def decode(self, s: str) -> List[str]:
        List1 = []
        i=0
        temp=""
        while i != len(s):
            if s[i] == "&" and s[i+1] == "@" and s[i+2] == "a" and s[i+3] == "p":
                i+=4
                List1.append(temp)
                temp=""
            else:
                temp += s[i]
                i+=1
        return List1
            


