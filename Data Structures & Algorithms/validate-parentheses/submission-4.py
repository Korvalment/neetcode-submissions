class Solution:
    def isValid(self, s: str) -> bool:
        stack = {'}':'{', ')':'(',']':'['}
        curent_stack = []

        for i in range(len(s)):
            if s[i] not in stack:
                curent_stack.append(s[i])
            else:
                if not curent_stack or stack[s[i]] != curent_stack[-1]:
                    return False
                else:
                    curent_stack.pop(-1)

        return len(curent_stack) == 0