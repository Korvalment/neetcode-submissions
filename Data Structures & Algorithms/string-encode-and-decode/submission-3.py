class Solution:

    # 5#hello
    def encode(self, strs: List[str]) -> str:
        encode_list = []
        for word in strs:
            len_word = len(word)
            target_str = f'{len_word}#{word}'
            encode_list.append(target_str)
        return ''.join(encode_list)
    
    # ["Hello","World"]
    def decode(self, s: str) -> List[str]:
        decode_str = []
        pointer = 0

        while pointer < len(s):
            j = pointer

            while s[j] != '#':
                j+=1

            lenght = int(s[pointer:j])

            str_start = j + 1
            str_end = j + 1 + lenght
            
            target_word = s[str_start:str_end]
            decode_str.append(target_word)

            pointer = str_end
        return decode_str
