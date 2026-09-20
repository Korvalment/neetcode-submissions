class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')':'(',
            '}':'{',
            ']':'['}
        stack =[]

        for char in s:
            if char in mapping:
                if stack:
                    last_entry = stack.pop()
                else:
                    return False
                    
                if last_entry != mapping[char]:
                    return False

            else:
                stack.append(char)

        return len(stack) == 0