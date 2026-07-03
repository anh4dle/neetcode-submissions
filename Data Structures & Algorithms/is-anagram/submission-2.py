class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #2 string is anagram if their string are identical
        #but differe position
        #which mean that count of character is the same 
        #dictionary to count first string
        #for second string we iterate and use dict to remove
        _dict = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in _dict:
                _dict[i] += 1
            else:
                _dict[i] = 1
        for i in t:
            if i in _dict:
                _dict[i] -= 1
                if _dict[i] == 0:
                    del _dict[i]
        return len(_dict) == 0