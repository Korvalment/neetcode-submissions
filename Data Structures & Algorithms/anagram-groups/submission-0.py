class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsMap = {}
    
        for i, anagram in enumerate(strs):
            key = tuple(sorted(Counter(anagram).items()))

            if key in anagramsMap:
                anagramsMap[key].append(anagram)
                continue

            anagramsMap[key] = [anagram]

        return list(anagramsMap.values())