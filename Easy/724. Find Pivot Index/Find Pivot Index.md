題目要求在list中找到pivot index，定義為其左右的value總和相等，且皆不包含pivot index。

另一個條件是，若pivot index出現在list的左緣，因為不取pivot index(0)本身，所以left value = 0，此時right value = 0即可，便回傳pivot index 為 0。

當list無法取得pivot index時，回傳 -1。

解題思路如下：

先初始設定 sum left value 為 0，sum right value為全list值加總。

以for迴圈先讓sum right value自左開始減少nums[i]，然後設定if函式與sum left value比較，若比對成功，即回傳i。

  比對不到，再對sum left value逐項加上nums[i]，再進入下一輪迴圈進行比較。
  
#這邊有個重點，

            for i in range(len(nums)):
            
            sRight -= nums[i]
            
            sLeft += nums[i]
            
            if sLeft == sRight:
            
                return i
          
    如果把sLeft += nums[i]寫進if判斷式上面，就會讓左右同步加減，這樣會有可能出現交錯，導致無法比對成功，找到pivot index
    
    所以務必要寫在if判斷式之後，如下：
    
            for i in range(len(nums)):
            
            sRight -= nums[i]
            
            if sLeft == sRight:
            
                return i
                
            sLeft += nums[i]
            
最後，如果都無法找到pivot index，就回傳-1。
            

