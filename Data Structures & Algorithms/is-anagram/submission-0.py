class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        s = s.replace(" ", "").lower()
        t = t.replace(" ", "").lower()

        if len(s) != len(t):
            return False

        charsT = {}
        charsS = {}

        for i in range(len(s)):
            charsS[s[i]] = 1 + charsS.get(s[i], 0)
            charsT[t[i]] = 1 + charsT.get(t[i], 0)
        
        if charsT == charsS:
            return True
        return False