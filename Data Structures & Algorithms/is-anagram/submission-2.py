class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charFreqS = {}
        charFreqT = {}
        for i, n in enumerate(s):
            if s[i] in charFreqS:
                charFreqS[s[i]] = charFreqS[s[i]] + 1
            else:
                charFreqS[s[i]] = 1

        for j, n in enumerate(t):
            if t[j] in charFreqT:
                charFreqT[t[j]] = 1 + charFreqT.get(t[j], 0)
            else:
                charFreqT[t[j]] = 1
        
        return charFreqS == charFreqT