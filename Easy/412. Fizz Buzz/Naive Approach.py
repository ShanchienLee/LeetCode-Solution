class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        ans = []
        
        for num in range(1, n+1):
            
            dividable_by_3 = (num % 3 == 0 )
            dividable_by_5 = (num % 5 == 0 )
            
            if dividable_by_3 and dividable_by_5:
                ans.append("FizzBuzz")         
            elif dividable_by_3:
                ans.append("Fizz")
            elif dividable_by_5:
                ans.append("Buzz")
            else:
                ans.append(str(num))
                
        return ans
