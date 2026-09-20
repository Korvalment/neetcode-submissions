class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsMap = {}

        for word in strs:
            curent_word = ''.join(sorted(word))
            if curent_word in anagramsMap:
                anagramsMap[curent_word].append(word)
            else:
                anagramsMap[curent_word] = [word]
        
        return list(anagramsMap.values())