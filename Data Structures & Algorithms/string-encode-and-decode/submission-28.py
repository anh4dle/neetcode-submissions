class Solution:

    def encode(self, strs: List[str]) -> str:
        #Store the metadata of each string, basically just its length
        #Return a string contain its length randomchar and string
        final = ""
        for string in strs:
            print("INside", string)
            final += str(len(string)) + "@" + string
        print("Showing encoded", final)
        return final

    def decode(self, s: str) -> List[str]:
        #Return a list of words based on this string 3@ape4@lion
        #Process the string by each subgroup: length, separator, word
        digit = ""
        results = []
        i = 0
        while i < len(s):
            if s[i] == '@':
                i += 1
                digit = int(digit)
                results.append(s[i:i + digit])
                i = i + digit
                digit = ""
            elif s[i].isdigit():
                digit += s[i] #[0]
                i += 1
        return results
                    

        
        