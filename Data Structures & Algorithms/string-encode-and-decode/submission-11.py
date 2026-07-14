class Solution:
    def encode(self, strs: List[str]) -> str:
        enstr=""
        for s in strs:
            en1 = str(len(s)) + "#" + s
            enstr += en1 
        return enstr

    def decode(self, s: str) -> List[str]:
        List1 = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            List1.append(s[j+1 : j+1+length])
            i = j + 1 + length
            
        return List1