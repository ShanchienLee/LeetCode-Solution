# 題目要求

1. 題目給一組數字序列，要求執行結果為：

    > runningSum[i] = sum(nums[0]...nums[i])

2. 回傳新陣列。

    > Examples:
    >    
    >> Input: nums = [1, 2, 3, 4]
    >>
    >> Output: [1, 3, 6, 10]
    >>
    >>Explanation: 
    >>
    >>>Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]

-----------------

# 解題思路

1. Input不斷疊加後，再放入陣列，所以可以用 for 迴圈堆疊。

2. 建立 for 迴圈，範圍為 1 至 list 長度。

    * 範圍不從 0 開始的原因如下：

        我們希望呈現的 list 是從第0位開始，逐項加上 list 中的值，所以迴圈為：

        > nums[ i ] += nums[i - 1]

        列表最低從 1 開始，加上 nums[i -1] ，也就是 nums[0] ，所以會呈現的第一個 list是 [nums[0], nums[0]+nums[1]] 。

3. 以 for 迴圈繼續直到 list 長度。
