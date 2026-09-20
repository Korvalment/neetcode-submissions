class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp_array = []

        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b) 
        }

        for i in range(len(tokens)):
            try:
                curent_number = int(tokens[i])
                temp_array.append(curent_number)

            except ValueError:
                second_number = temp_array.pop()
                first_number = temp_array.pop()

                temp_array.append(ops[tokens[i]](first_number, second_number))

        return int(temp_array[-1])