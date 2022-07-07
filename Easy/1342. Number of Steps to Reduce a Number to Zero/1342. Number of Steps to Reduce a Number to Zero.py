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

    
-------------------------

# or sipmlier code in same thought, while a little slower.

class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num != 0:
            if num % 2 == 0:
                num = num/2
                step += 1
            elif num % 2 == 1:
                num = (num-1)
                step += 1
        return step
