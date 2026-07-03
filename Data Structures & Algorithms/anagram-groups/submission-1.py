class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Rearrange char, store as key, if string after rearrange match the key then add to array
        _map = {}
        for _str in strs:
            _key = "".join(sorted(_str))
            if _key in _map:
                _map[_key].append(_str)
            else:
                _map[_key] = [_str]
        final_res = []
        for k,v in _map.items():
            final_res.append(v)
        return final_res