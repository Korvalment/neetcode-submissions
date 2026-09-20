class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grops_of_anagrams = {}
        for word in strs:
            word_anagram = ''.join(sorted(list(word)))

            if word_anagram in grops_of_anagrams:
                grops_of_anagrams[word_anagram].append(word)
            if word_anagram not in grops_of_anagrams:
                grops_of_anagrams[word_anagram] = [word]

        return list(grops_of_anagrams.values())