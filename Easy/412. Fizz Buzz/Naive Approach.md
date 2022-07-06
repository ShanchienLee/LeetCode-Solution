# 題目要求

1. 題目給一個整數 n 須按以下條件回傳序列 [1...i...n]‧
   
   1. 如果整數 i 可被 3 和 5 整除，則在序列中回傳字串 "FizzBuzz"。
   
   2. 如果整數 i 可被 3 整除，則在序列中回傳字串 "Fizz"。

   3. 如果整數 i 可被 5 整除，則在序列中回傳字串"Buzz"。

   4. 如果以上三個條件都無法成就，則在序列中回傳 [i]。

    > Examples:
    >    
         Input: 3
        
         Output: ["1", "2", "Fizz"]

-----------------

# 解題思路

##  1. Naive Approach

1.  題目給定的整數 n ，會需要重複計算，所以可用 for 迴圈處理。

2. 先建立一個 for 迴圈，範圍為 1 至 n + 1 。

    >       for num in range(1, n+1):

    * range 函式是取首不取尾，所以假設 n == 3 ，我們希望迴圈跑出 ["1", "2", "3"]，則 range(1, 4)才對。

3.  我們希望在迴圈中，每一輪都去跟 3, 5 相除，檢視是否整除，或是有餘數。所以設定以下條件：

    >       dividable_by_3 = (num % 3 == 0 )
    > 
    >       dividable_by_5 = (num % 5 == 0 )

4. 再來利用 if 函式按照題目條件建立判斷式：
    >      if dividable_by_3 and dividable_by_5:
    >           ans.append("FizzBuzz")         
    >      elif dividable_by_3:
    >           ans.append("Fizz")
    >      elif dividable_by_5:
    >           ans.append("Buzz")
    >      else:
    >           ans.append(str(num))  

5. 回傳 ans 。
