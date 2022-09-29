class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 
                 'V':5, 
                 'X':10, 
                 'L':50, 
                 'C':100, 
                 'D':500, 
                 'M':1000
                      }
        
        sum = 0
        list_s = list(s)
        
        for i in range(len(list_s)-1, -1, -1):
            if i == (len(list_s)-1):
                sum += roman[list_s[i]]
            else:
                if roman[list_s[i+1]] > roman[list_s[i]]:
                    sum -= roman[list_s[i]]
                else:
                    sum += roman[list_s[i]]

        return sum
