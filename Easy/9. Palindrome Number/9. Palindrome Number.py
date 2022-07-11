class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        temp_rev = "".join(list(reversed(temp)))
        if temp_rev == temp:
            return True
        else:
            return False
