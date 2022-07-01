# 題目要求

1. 在list中找到 pivot index，其定義為其左右的 value 總和相等，且皆不包含 pivot index 。

2. 若 pivot index 出現在 list 的左緣，因為不取 pivot index [0] 本身，所以 left value = 0 ， 此時 right value = 0 即可，便回傳 pivot index 為 0 。

3. 當list無法取得 pivot index 時，回傳 -1 。

------





# 解題思路

1. 先初始設定 sum left value 為 0，sum right value 為全list 值加總。

2. 以 for 迴圈先讓 sum right value 自左開始減少 nums[i] ，然後設定 if函式與 sum left value 比較，若比對成功，即回傳 i 。

3. 比對不到，再對 sum left value 逐項加上 nums[i] ，再進入下一輪迴圈進行比較。

    * 這邊有個重點，

        >            for i in range(len(nums)):       
        >                  sRight -= nums[i]        
        >                  sLeft += nums[i]        
        >               if sLeft == sRight:     
        >                  return i
      
        
        如果把 sLeft += nums[i] 寫進 if 判斷式上面，就會讓左右同步加減，這樣會有可能出現交錯，導致無法比對成功，找到 pivot index ‧

        所以務必要寫在if判斷式之後，如下：

        >           for i in range(len(nums)):
        >               sRight -= nums[i]
        >              if sLeft == sRight:
        >                  return i   
        >               sLeft += nums[i]

4. 最後，如果都無法找到 pivot index，就回傳 -1 。
