class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsMap = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in anagramsMap:
                anagramsMap[key] = []
            anagramsMap[key].append(s)

        return list(anagramsMap.values())