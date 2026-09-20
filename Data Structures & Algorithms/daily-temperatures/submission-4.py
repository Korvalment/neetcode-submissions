class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer_temp = [0 for i in range(len(temperatures))]
        stack = []

        for day in range(len(temperatures)):
            while stack and temperatures[day] > temperatures[stack[-1]]:
                last_day = stack.pop()
                answer_temp[last_day] = day - last_day


            stack.append(day)

        return answer_temp