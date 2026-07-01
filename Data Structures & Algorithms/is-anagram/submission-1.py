class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #2 string is anagram if their string are identical
        #but differe position
        #which mean that count of character is the same 
        #dictionary to count first string
        #for second string we iterate and use dict to remove
        _count = {}
        for char in s:
            if char in _count:
                _count[char] += 1
            else:
                _count[char] = 1
        _count2 = {}
        for char in t:
            if char in _count2:
                _count2[char] += 1
            else:
                _count2[char] = 1
        return _count == _count2