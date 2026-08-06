class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for char in strs:
            key = ''.join(sorted(char))
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(char)
        return list(hash_map.values())