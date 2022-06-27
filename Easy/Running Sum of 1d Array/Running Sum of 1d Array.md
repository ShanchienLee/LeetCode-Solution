建立for迴圈，範圍為1至list長度

範圍不從0開始的原因如下：

我們希望呈現的list是從第0位開始，逐項加上list中的值，所以迴圈為：

  nums[i] += nums[i - 1]
  
列表最低從1開始，加上nums[i -1]，也就是nums[0]，所以會呈現的第一個list是[nums[0], nums[0]+nums[1]]

以下回圈繼續直到list長度。
