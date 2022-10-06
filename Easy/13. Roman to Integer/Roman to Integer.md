# 題目要求

1. 將羅馬數字轉換為整數。

    >   I: 1
    >
    >   V: 5
    >
    >   X: 10
    >
    >   L: 50
    >
    >   C: 100
    >
    >   D: 500
    >
    >   M: 1000 

2. 羅馬數字有特殊規則：

   * I 可以連三個代表 3 ，但 4 必須是 (5-1) ，也就是 IV 。
   * 同理， 6 到 8 可以用 VI 至 VIII 表示，但 9 必須為(10-1)，也就是 IX 。
   * 以此類推。
---------

# 解題思路

1. 可以先辨識羅馬字符與所對應數字，並建立資料；因為字符與對應的數字，有鍵值關係，所以用字典資料型態較為適合。

    >       roman = {'I':1, 
    >                'V':5, 
    >                'X':10, 
    >                'L':50, 
    >                'C':100, 
    >                'D':500, 
    >                'M':1000
    >                    }

2. 再來我們必須思考羅馬數字的組成邏輯，我們取一個大一點的數字來檢視，例如 1994 ，其羅馬數字為 MCMXCIV ，我們可以由後往前檢查，可以發現組合規則。
   
3. 字符如果同位，則為數字相加；但如果後一位字符比前一位字符大階，則為較大字符所代表的數字減去較小字符所代表的數字。舉例如下：

        III 為同字符，故為 1+1+1=3
        IV 為異字符，且後一字符較前一字符大階，故為 5-1=4
        MC 為異字符，且後一字符較前一字符大階，故為 1000-100=900

4. 為了計算，先建立一個變數並設定初始值為 0 。
    >       sum = 0

5. 將題目給定的羅馬字符字串轉為序列，並存放於變數 list_s 。
    >       list_s = list(s)

6. 以 for 迴圈來迭代加總，並依前述邏輯，從給定羅馬數字倒數選取來做檢查，所以會設定 for 迴圈的 range 如下：
    >       for i in range(len(list_s)-1, -1, -1):

    * range 的第一個參數表示範圍的起點，而len函數算出來的長度與位置會差一個 "0" 的位置，所以要 -1 。
    * range 的第二個參數表示範圍的終點，且又因為 range函式計首不計尾，所以寫上 "-1" ，但只會回到 "0" 。
    * range 最後一個參數，表示迴圈取樣的方向及間距， "-1" 表示一次倒序選取一位。
        
7. 依據前述的「由後往前」規則，可以用 if 判斷式完成。
   >        if i == (len(list_s)-1):
   >            sum += roman[list_s[i]]

   * 如果取樣數字與字符序列最後一位相同時，則 sum 疊加從 roman 字典依取樣所取出得值。
  
8. 再將其餘狀況寫入子 if 判斷式。
    >       else:
    >           if roman[list_s[i+1]] > roman[list_s[i]]:
    >               sum -= roman[list_s[i]]
    >           else:
    >               sum += roman[list_s[i]]

   * 如果從 roman 字典鍵 "i+1" 取出的值大於依 "i" 所取出的值，則此時 sum 要減掉依 "i" 所取出的值；其餘情況，就是 sum 加上依 "i" 所取出的值。

9. 回傳完成的加總數 sum 。


    >       return sum