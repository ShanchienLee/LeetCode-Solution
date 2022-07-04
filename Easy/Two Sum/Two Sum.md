# 題目要求

1. 題目給一組數字序列，及目標數字，要求在數字序列中找到相加符合目標數字的兩個值。

2. 回傳該二值的位置序列。

    > Examples:
    >    
         Input: nums = [2, 7, 11, 15]
        
         Target = 9
        
         Output: [0, 1]
        
         Explanation: 
        
            Because nums[0] + nums[1] == 9, so we return [0, 1]

-----------------

# 解題思路

## 1. Brute Force 暴力解

1. 利用巢狀迴圈來對數字序列做加總比對。

2. 建立 兩個 for 迴圈階層：

        第一階層 i 範圍為 list 長度。

        第二階層 j 範圍為 i + 1 至 list 長度。

3. 利用 if 判斷式將 nums[j] 與目標數字和 nums[i] 比對，得解時即傳回 [i, j]

    * 因為我們希望藉由兩次迴圈來達到比對差額的效果，所以會先用第一層迴圈確定 nums[i] ，然後再用第二層迴圈取得的 nums[j] 去與 target - nums[i] 的值去比對。

    * 而 i 從頭開始逐序選取， j 的選取範圍必定不能為 i 本身，故範圍為 i+1 至系列長度。

        >     for i in range(len(nums)):
        >         for j in range(i + 1, len(nums)):

4. 以 if 判斷式比對 nums[j] 與目標數字和 nums[i] 之差額。

    >       if nums[j] == target - nums[i]:

5. 回傳找到的[i, j]

    >       return[i, j]


* ##  這種解法思路直接，但效率太差。

----------------

## 2. Two-pass Hash Table 

* ## 可以利用 Hash Table 來協助，且能提升效能。

1. 先建立一個 hashmap 。

2. 以 for 迴圈先將 list 的值與對應的 index 存入hashmap。

3. 一樣利用 for 迴圈找出目標值與 nums[i] 的差額，並設定此差額為變數 a 。

4. 以 if判斷式，將變數 a 作為 key ，於 hashmap 中找出 hashmap[a] 值，而此hashmap[a]實際上是 array index。

    * 必須設定條件：hasmap[a] 不等於 i

5. 回傳 [i, hashmap[a]]
