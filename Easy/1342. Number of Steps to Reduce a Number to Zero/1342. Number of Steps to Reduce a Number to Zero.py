class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num != 0:
            divided_by_2 = (num % 2 == 0)
            non_divided_by_2 = (num % 2 == 1)

            if divided_by_2:
                num = num/2
                step += 1
            elif non_divided_by_2:
                num = (num-1)
                step += 1
        return step
