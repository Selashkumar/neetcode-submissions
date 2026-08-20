class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 4 = 6 / 2 => 3
        # 1 = 9 / 2 => 4.2
        # 0 = 10 / 1 => 10
        # 7 = 3 / 1 => 3
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair)[::-1]:
            need = (target - p) / s
            if not stack:
                stack.append(need)
            if stack and need > stack[-1]:
                stack.append(need)

            # print(need)
        return len(stack)