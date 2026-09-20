class Solution:
    def encode(self, strs: List[str]) -> str:
        encode_str = []
        for word in strs:
            len_word = len(word)
            encode_str.append(f'{len_word}#{word}')

        return ''.join(encode_str)

    def decode(self, s: str) -> List[str]:
        decode_str = []

        pointer = 0
        while pointer < len(s):

            j = pointer

            while s[j] != '#':
                j += 1

            lenght = int(s[pointer:j])

            word_start = j + 1
            word_end = j + 1 + lenght

            word = s[word_start:word_end]
            decode_str.append(word)

            pointer = word_end

        return decode_str