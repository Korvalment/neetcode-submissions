class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            stack = []

            cars_info = sorted(zip(position, speed))[::-1]

            for poss, spd in cars_info:
                car_time = (target - poss) / spd

                if not stack:
                    stack.append(car_time)
                    continue

                if car_time > stack[-1]:
                    stack.append(car_time)
                
                elif car_time <= stack[-1]: 
                    continue

            return (len(stack))
                