# proj-its-certification-python
Project: ITS Certification Python.

## 練習題指引

- 將練習題的 GitHub Repository 下載到自己的電腦，解壓縮後以 VS Code 開啟專案資料夾。
- 先閱讀 `README.md`，再將答案寫在 `answers.py`
- 練習題共分為四種：
  - 是非題：預設答案 `answer_01 = None`，請以布林型別宣告答案，若覺得是非題的敘述**不正確**，就宣告 `answer_01 = False`，若覺得是非題的敘述**正確**則宣告 `answer_01 = True`
  - 單選題：預設答案 `answer_02 = None`，請以整數型別宣告答案，若覺得單選題的第一個選項**正確**宣告為 `answer_02 = 1`，若覺得單選題的第二個選項**正確**則宣告 `answer_02 = 2`，若覺得單選題的第三個選項**正確**則宣告 `answer_02 = 3`，若覺得單選題的第四個選項**正確**則宣告 `answer_02 = 4`
  - 複選題：預設答案 `answer_03 = set()`，請以集合資料結構宣告答案，若覺得複選題的第一個選項、第三個選項與第四個選項**正確**，則宣告為 `answer_03 = {1, 3, 4}`
  - 連連看：預設答案 `answer_04 = dict()`，請以字典資料結構宣告答案，若覺得連連看的 `A.` 應該與 `1.` 相連，則宣告為 `answer_04 = {"A": 1}`
- 如果練習題需要載入檔案，檔案會與練習題存放在同個資料夾中，這時可以運用工作目錄的相對路徑直接指定檔案名稱載入。
- 寫作完成後將 `answers.py` 存檔，再執行專案資料夾中的 `test_runner.py` 進行測試，再依照測試結果修正答案或截圖測試結果繳交作業。

## 01.（單選題）你編寫了以下的程式碼：

```python
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = list_1 + list_2
list_4 = list_3 * 2
print(list_4)
```

執行程式碼的輸出值是？

1. `[[1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6]]`
2. `[4, 10, 18]`
3. `[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]`
4. `[[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]`

```python
answer_01 = None
```

## 02.（單選題）你是運動 App 的程式設計師，你必須製作一個函式為跑者計算步速，所謂步速就是每公里所花的時間，輸出結果必須盡可能精確，要如何完成程式碼？請在回答區中選擇適當的程式碼片段，其中距離須轉換為浮點數，時間的輸入值都要轉換為整數。

```python
distance = (A)(input("Enter the distance traveled in meters"))
distance_kms = distance / 1000
time_minute = (B)(input("Enter the time elapsed in minutes"))
time_sec = (C)(input("Enter the time elapsed in seconds"))
time = time_minute * 60 + time_sec
pace = time / distance_kms
print("The average velocity is", str((pace // 60)) + ":" + str((pace % 60)))
```

以上分別要填入的函式名為：

1. (A)`int`(B)`float`(C)`float`
2. (A)`float`(B)`int`(C)`int`
3. (A)`float`(B)`str`(C)`str`
4. (A)`int`(B)`int`(C)`float`

```python
answer_02 = None
```

## 03.（複選題）高年級的老師要製作一份報表來顯示這次考試班上所有學生的平均分數，報表必須去除平均分數的小數部分，你應該使用哪兩個程式碼？

1. `平均分數 = float(全班總分 // 全班人數)`
2. `平均分數 = int(全班總分 / 全班人數)`
3. `平均分數 = float(全班總分 ** 全班人數)`
4. `平均分數 = 全班總分 // 全班人數`

```python
answer_03 = set()
```

## 04.（連連看）你正在編寫一個 Python 程式用來記錄客戶資料並將其儲存在資料庫中，這個程式處理各式各樣的資料，以下的變數宣告後它們的資料類別是？請將適合的程式碼片段連到正確的回答區。

程式碼片段

A. `age = 12`
B. `minor = False`
C. `name = 'David'`
D. `weight = 64.5`
E. `zip = "545"`

回答區

1. `int`
2. `bool`
3. `str`
4. `float`

```python
answer_04 = dict()
```

## 05.（單選題）你編寫了以下的程式碼：

```python
a = 24
b = 7
ans = (a % b * 100) // 2.0 ** 3.0 - b
print(ans)
```

```python
answer_05 = None
```

執行程式碼的輸出值是？

1. `30.0`
2. `30.5`
3. `457`
4. `SyntaxError`

## 06.（單選題）你正在編寫一個計算使用者出生年份的程式，該程式詢問使用者的年齡和當前月份，然後輸出使用者的出生年份，你編寫以下程式碼，其中包含的列號只是做參考。

```python
age = input("Enter your age:") # 01
year = input("Enter the four digit year:") # 02
born = int(year) - int(age) # 03
message = "You were born in " + str(born) # 04
print(message) # 05
```

請問下列何者是正確的？

1. 在 02 列中 `year` 的資料類型是 `str`
2. 在 03 列中 `born` 的資料類型是 `float`
3. 在 04 列中 `message` 的資料類型是 `bool`

```python
answer_06 = None
```

## 07.（複選題）在 Python 資料類型的課程中創建以下三個程式碼片段：

```python
# Code segment 1
x1 = "5"
y1 = 4
a = x1 * y1

# Code segment 2
x2 = 10
y2 = 4
b = x2 / y2

# Code segment 3
x3 = 5.5
y3 = 1
c = x3 / y3
```

你需要評估程式碼片段，請問下列何者是正確的？

1. 執行 Code segment 1 後，變數 `a` 的資料類型為 `str`
2. 執行 Code segment 2 後，變數 `b` 的資料類型為 `float`
3. 執行 Code segment 3 後，變數 `c` 的資料類型為 `int`

```python
answer_07 = set()
```

## 08.（單選題）在 Python 程式中我們利用 `type()` 查詢每個值的資料類別，以下的程式執行後出現的資料類別分別是：

```python
print(type(+1E10))
print(type(5.0))
print(type("True"))
print(type(False))
```

1. `int`, `int`, `bool`, `bool`
2. `float`, `float`, `str`, `bool`
3. `int`, `float`, `str`, `bool`
4. `float`, `int`, `str`, `str`

```python
answer_08 = None
```

## 09.（單選題）你加入了電子商務公司成為其程式開發部門的實習生，你的程式中有一個地方要讓使用者提供一個數值。即使使用者輸入了小數，該值也必須轉換為整數來進行計算，你應該使用哪個程式碼片段？

1. `totalNums = input("How many items would you like?")`
2. `totalNums = int(input("How many items would you like?"))`
3. `totalNums = str(input("How many items would you like?"))`
4. `totalNums = float(input("How many items would you like?"))`

```python
answer_09 = None
```

## 10.（單選題）你設計了一個 Python 程式用來顯示每個員工每天工作到現在的小時數，你需要計算工作時數並顯示訊息，程式碼如下：

```python
start = input("What time did you start working today?") # 01
end = input("What time is it now?") # 02
# 03
```

如果要完成這個程式，在 03 列應該使用哪個程式碼？

1. `print("You have worked for" + str(int(end) - int(start)) + " hours")`
2. `print("You have worked for" + (int(end) - int(start)) + " hours")`
3. `print("You have worked for" + str(end - start) + " hours")`
4. `print("You have worked for" + int(end - start) + " hours")`

```python
answer_10 = None
```

## 11.（單選題）你正在編寫 Python 程式用於計算一個數學公式，公式內容為 `b` 等於 `a` 加上 `5`，然後再平方，其中 `a` 是輸入，`b` 是結果。你設計了以下的程式碼片段：

```python
a = int(input("Enter a number for the equation:")) # 01
# 02
```

如何完成 02 列的程式碼？

1. `b = (a + 5)**2`
2. `b = a + 5**2`
3. `b = a + 5*2`
4. `b = a + (5**2)`

```python
answer_11 = None
```

## 12.（單選題）你正在開發一個補習班的 Python 函式來計算折扣，補習班希望鼓勵小朋友和老年人報名，只要是小朋友和老年人報名相關課程就會獲得 10% 的折扣。你編寫了以下程式碼：

```python
def get_discount(kid: bool, senior: bool) -> float: # 01
    discount = 0.1 # 02
    # 03
        discount = 0.0 # 04
    return discount # 05
```

為了完成這個程式碼，你應該在 03 列加入什麼程式碼？

1. `if not (kid or senior):`
2. `if (not kid) or senior:`
3. `if not (kid and senior):`
4. `if (not kid) or senior:`

```python
answer_12 = None
```

## 13.（複選題）你開發了一個比較的 Python 程式，下列何者的值是 `True`？

1. `0 or 5`
2. `bool(0)`
3. `None is None`
4. `-5 < 0 < 5`

```python
answer_13 = set()
```

## 14.（單選題）計算以下的 Python 數學運算式：

```python
3 * (1 + 2)**2 - 2**2 * 3
```

結果為何？

1. 3
2. 13
3. 15
4. 69

```python
answer_14 = None
```

## 15.（連連看）你編寫了以下的程式碼：

```python
a = "Test1" # 01
print(a)    # 02
b = "Test2" # 03
a += b      # 04
print(a)    # 05
print(b)    # 06
```

根據程式碼片段中提供的資訊將問題與答案相連。

問題區

A. 在 02 列 `print(a)` 後會顯示什麼？
B. 在 05 列 `print(a)` 後會顯示什麼？
C. 在 06 列 `print(b)` 後會顯示什麼？

答案區

1. `Test1`
2. `Test1Test2`
3. `Test2`

```python
answer_15 = dict()
```

## 16.（連連看）你為公司開發了一個 Python 應用程式，程式碼如下：

```python
def test(a, b, c, d):
    value = (a + b) * c - d
    return value
```

根據程式碼片段中的資訊將問題與答案相連。

問題區

A. 運算式的哪個部分將第一個進行計算？（從 1. 至 3. 擇一）
B. 運算式的那個部分將第二個進行計算？（從 4. 至 6. 擇一）
C. 哪個運算式等於題目函數中的運算式？（從 7. 至 9. 擇一）

答案區

1. `a+b`
2. `b*c`
3. `c-d`
4. `+`
5. `-`
6. `*`
7. `(a + b)*(c - d)`
8. `(a + (b*c)) - d`
9. `((a + b)*c) - d`

```python
answer_16 = dict()
```

## 17. （單選題）請按先後順序從頭至尾排列這六類運算的正確順序：

- 加法和減法
- 乘法和除法
- 正數、負數與反位元（`not`）
- 括弧
- 指數
- 且（`and`）

1. 加法和減法 -> 乘法和除法 -> 正數、負數與反位元 -> 括弧 -> 指數 -> 且
2. 括弧 -> 指數 -> 正數、負數與反位元 -> 乘法和除法 -> 加法和減法 -> 且
3. 指數 -> 乘法和除法 -> 正數、負數與反位元 -> 括弧 -> 且 -> 加法和減法
4. 乘法和除法 -> 括弧 -> 正數、負數與反位元 -> 指數 -> 且 -> 加法和減法

```python
answer_17 = None
```

## 18.（連連看）租車公司需要一種方法來決定客戶租用車輛的費用，該費用取決於車輛歸還的時間，然而，週四和週日也有特別的費率，費用結構如下所示：

- 費用是每天 100 美元。
- 如果車輛在晚上 11 點後還，客戶將被多收取額外一天的費用。
- 如果車輛是在星期天租的，客戶可以享受 10% 的折扣。
- 如果車輛是在星期四租的，客戶可以享受 20% 的折扣。

你需要撰寫程式碼符合這個需求，要如何完成這段程式碼？

```python
ontime = input("Was car returned before 11 pm? y or n").lower()
days_rented = int(input("How many days was car rented?"))
day_rented = input("What day was the car rented?").capitalize()
cost_per_day = 100
if ontime (A.):
    days_rented += 1
if day_rented (B.):
    total = (days_rented * cost_per_day) * 0.9
elif day_rented (C.):
    total = (days_rented * cost_per_day) * 0.8
else:
    total = days_rented * cost_per_day
print("Cost of the car rental is: $", total)
```

A. 1. !="n" 2. =="n" (C) 3. =="y"
B. 1. =="Sunday" 2. >="Sunday" 3. is "Sunday"
C. 1. =="Thursday" 2. <= "Thursday" 3. is "Thursday"

```python
answer_18 = dict()
```

## 19.（連連看）你設計了一個數學運算的 Python 程式，程式碼如下：

```python
a = 11
b = 5
```

下列何者為每個數學運算式的結果？將程式碼與答案相連。

程式碼

A. `print(a/b)`
B. `print(a // b)`
C. `print(a % b)`

答案

1. `1`
2. `2`
3. `2.2`

```python
answer_19 = dict()
```

## 20. （連連看）你設計了一個比較數字的 Python 程式，內容如下：

```python
n1 = int(input("Please enter the first number:")) # 01
n2 = int(input("Please enter the second number:")) # 02
if n1 = n2: # 03
    print("The two numbers are equal.") # 04
if n1 <= n2: # 05
    print("Number 1 is less than number 2.") # 06
if n1 > n2: # 07
    print("Number 1 is greater than number 2.") # 08
if n2 <> n1: # 09
    print("The two numbers are the same.") # 10
```

針對下列每個敘述與正確與否相連。

敘述

A. 在 03 列的語法是不正確的比較。
B. 在 06 列的只有 `n1` 小於 `n2` 時才會列印出來。
C. 在 08 列的只有 `n1` 大於 `n2` 時才會列印出來。
D. 在 09 列的語法是不正確的比較。

正確與否

1. False
2. True

```python
answer_20 = dict()
```

## 21. （單選題）老闆要求你對以下程式碼除錯：

```python
x = 0
while x < 4:
    if x % 4 == 0:
        print("party")
    elif x - 2 < 0:
        print("cake")
    elif x / 3 == 0:
        print("greeting")
    else:
        print("birthday")
    x = x + 1
```

什麼將會輸出列印到螢幕上？

1. `party \n greeting \n birthday \n cake`
2. `party \n cake \n birthday \n birthday3e`
3. `birthday \n party \n greeting \n cake`
4. `birthday \n greeting \n party \n cake`

```python
answer_21 = None
```

## 22.（單選題）在下列的程式碼中：

```python
aList = [0, 1, 2, 3, 4]
print(4 in aList)
```

會輸出列印的內容？

1. `4`
2. `5`
3. `True`
4. `False`

```python
answer_22 = None
```

## 23.（連連看）你為公司開發了一個 Python 應用程式，設計了以下的程式碼：

```python
aList = ["a", "b", "c", "d", "e"]
bList = [1, 2, 3, 4, 5]
print(aList is bList)
print(aList == bList)
aList = bList
print(aList is bList)
print(aList == bList)
```

根據程式碼片段中提供的資訊選擇每個問題的答案。

問題

A. 在第一次 print 後會顯示什麼？
B. 在第一次 print 後會顯示什麼？
C. 在第一次 print 後會顯示什麼？
D. 在第一次 print 後會顯示什麼？

答案 

1. False
2. True

```python
answer_23 = dict()
```

## 24.（連連看）同事開發一個將產品名稱輸入到資料庫的程式，但是其中發生了錯誤，每個存入的名稱字母順序都顛倒了。請你開發一個 Python 函式，將每個產品名稱以正確的順序輸出，請選擇適當的程式碼片段填寫缺漏處：

```python
def reverse_pname(backwards_pname):
    forward_pname = ""
    for index in (A.):
        forward_pname += (B.)
    return forward_pname
```

缺漏處

A. 從 1. 至 4. 擇一
B. 從 5. 至 8. 擇一

程式碼片段

1. `backwards_pname`
2. `len(backwards_pname)`
3. `range(0, len(backwards_pname), -1)`
4. `range(len(backwards_pname) - 1, -1, -1)`
5. `backwards_name[index - 1]`
6. `backwards_name[len(forward_name) - 1]`
7. `backwards_name[len(forward_name) - len(backwards_pname)]`
8. `backwards_name[index]`

```python
answer_24 = dict()
```

## 25.（連連看）你有以下的 `str` 物件：

```python
alph = "abcdefghijklmnopqrstuvwxyz"
```

以下各個程式碼片段的結果各是如何？請將程式碼片段與回答相連。

程式碼片段

A. `alph[3:15]`
B. `alph[3:15:3]`
C. `alph[15:3:-3]`
D. `alph[::-3]`

回答

1. `zwtqnkheb`
2. `pmjg`
3. `defghijklmno`
4. `ponmlkjihgfe`
5. `defghijklmnop`
6. `dgjm`
7. `olif`

```python
answer_25 = dict()
```

## 26.（複選題）你為學校設計了一個 Python 應用程式，在 `classroom` 的清單中包含了 60 位同學的姓名，最後 3 名是班上的幹部，你需要分割清單內容顯示除了幹部以外的所有同學，你可以利用以下哪兩個程式碼達成？

1. `classroom[0:-2]`
2. `classroom[0:-3]`
3. `classroom[1:-3]`
4. `classroom[:-3]`
5. `classroom[1:-3]`

```python
answer_26 = set()
```

## 27.（單選題）你開發了一個 Python 應用程式，其中有一個名為 `month` 的清單儲存所有月份的英文，你要分割這個清單，取得由第二個月份開始，每間隔一個值的月份名稱，你應該使用哪個程式碼？

1. `month[2:2]`
2. `month[::2]`
3. `month[1::2]`
4. `month[1:2]`

```python
answer_27 = None
```

## 28.（連連看）你設計了一個函式來執行除法，因為除法的除數不能為零，所以在函式中必須要針對這個重點進行檢查，你要如何完成這段程式碼？請選擇適當的程式碼片段填寫缺漏處：

```python
def safe_divide(numerator, denominator):
    (A.)
        print("A requried value is missing.")
    (B.)
        print("The denominator is zero.")
    else:
        return numerator / denominator
```

缺漏處

A. 從 1. 至 4. 擇一
B. 從 5. 至 8. 擇一

程式碼片段

1. `if numerator is None or denominator is None:`
2. `if numerator is None and denominator is None:`
3. `if numerator = None or denominator = None:`
4. `if numerator = None and denominator = None:`
5. `elif denominator == 0:`
6. `elif denominator = 0:`
7. `elif denominator != 0:`
8. `elif denominator in 0:`

```python
answer_28 = dict()
```

## 29.（連連看）你設計了以下程式用座號來查詢學生的姓名，加上列號為參考之用。

```python
students = {1: "John", 2: "Mary"} # 01
id = input("輸入學生座號：") # 02
if not id in students: # 03
    print("該學生並不存在") # 04
else: # 05
    print("學生姓名為：" + students[id]) # 06
```

同事們報告說程式有時會產生不正確的結果，請將問題與答案相連。

問題

A. 在 01 列中有哪兩種資料類型儲存在 students？（從 1. 至 4. 擇一）
B. 在 02 列中 `id` 的資料類型是什麼？（從 5. 至 8. 擇一）
C. 在 03 列中為什麼會在 students 中找不到資料？（從 9. 至 11. 擇一）

1. `bool` 與 `str`
2. `float` 與 `bool`
3. `int` 與 `str`
4. `float` 與 `int`
5. `bool`
6. `float`
7. `int`
8. `str`
9. 語法不正確
10. 資料型態不符合
11. 變數命名錯誤

```python
answer_29 = dict()
```

## 30. （單選題）你正在撰寫一個 Python 程式評估算數公式，此公式描述 X 等於 Y 乘以負一，然後再平方，其中 Y 是即將輸入的值，而 X 是結果。請選擇適當的符號或文字完成第二列程式碼，每個符號或文字可能使用一次或多次，甚至完全用不到。

```python
Y = int(input("Enter a number for the equation:"))
X = __ __ __ __ __
```

符號或文字

A. `-`
B. `(`
C. `)`
D. `**`
E. `**2`
F. `2`
G. `Y`

1. BAGCE
2. ABGDF
3. AGDFE
4. BADCE

```python
answer_30 = None
```

## 31.（連連看）你設計了一個程式要依學生的成績來顯示等級，它的規定如下：

|Percentage range|Letter grade|
|----------------|------------|
|90 through 100|A|
|80 through 89|B|
|70 through 79|C|
|60 through 69|D|
|0 through 59|F|

如果使用者輸入 90，則輸出應該是 `"Your grade is: A"`，如果使用者輸入 89，則輸出應該為 `"Your grade is: B"`，你要如何完成這段程式？請選擇適當的程式碼片段填寫缺漏處：

```python
grade = int(input("Enter a numeric grade"))
(A.)
    letter_grade = "A"
(B.)
    letter_grade = "B"
(C.)
    letter_grade = "C"
(D.)
    letter_grade = "D"
else:
    letter_grade = "F
print("Your letter grade is: ", letter_grade)
```

A. 從 1. 至 4. 擇一
B. 從 5. 至 8. 擇一
C. 從 9. 至 12. 擇一
D. 從 13. 至 16. 擇一

1. `if grade <= 90:`
2. `if grade >= 90:`
3. `elif grade > 90:`
4. `elif grade >= 90:`
5. `if grade > 80:`
6. `if grade >= 80:`
7. `elif grade > 80:`
8. `elif grade >= 80:`
9. `if grade > 70:`
10. `if grade >= 70:`
11. `elif grade > 70:`
12. `elif grade >= 70:`
13. `if grade > 60:`
14. `if grade >= 60:`
15. `elif grade > 60:`
16. `elif grade >= 60:`

```python
answer_31 = dict()
```

## 32.（連連看）你要設計一款以使用者年齡進行電影分級的程式，必須符合以下要求：

- 任何 18 歲或以上的人會顯示「限制級」。
- 任何 13 歲或以上但小於 18 歲的人會顯示「輔導級」。
- 任何 12 歲或更年輕的人會顯示「普通級」。
- 如果年齡未知，則會顯示「未知」。

你需要完成程式碼以符合要求，應該要如何完成這段程式碼？

```python
def get_rating(age):
    if (A.)
    elif (B.)
    elif (C.)
    else (D.)
    return rating
```

程式碼片段

1. `age < 13: rating = "普通級"`
2. `age < 18: rating = "輔導級"`
3. `:rating = "限制級"`
4. `age is None: rating = "未知"`

```python
answer_32 = dict()
```

## 33.（單選題）你用學生的成績（`grade`）及排名（`rank`）編寫程式碼來決定最後成績：

```python
if grade > 80 and rank >= 3:
    grade += 10
if grade > 70 and rank > 3:
    grade +=5
else:
    grade -= 5
```

當 `grade = 76`、`rank = 3` 時，執行程式碼的輸出是？

1. `71`
2. `76`
3. `81`
4. `86`

```python
answer_33 = None
```

## 34.（連連看）你正在編寫一個函式來判別負數與非負數，這個函式必須符合以下要求：

- 如果 `a` 是負數，則回傳 `"The result is a negative number"`
- 如果 `a` 不是負數，則為非負數，再繼續判別。
- 如果 `a` 大於 0 則回傳 `"The result is a positive number"`，否則回傳 `"The result is a zero"`

你要如何完成這段程式碼？

```python
def reResult(a):
    (A.)
        answer = "The result is a negative number"
    (B.)
        (C.)
            answer = "The result is a positive number"
        (D.)
            answer = "The result is a zero"
    return answer
```

1. `if a < 0:`
2. `if a > 0:`
3. `else:`
4. `elif:`

```python
answer_34 = dict()
```

## 35.（連連看）你設計了一個電影票收費的函式，票價的規則如下：

- 5 歲以下，免費入場
- 5 歲及以上的學生，60 元
- 5 歲到 17 歲但不是學生，120 元
- 17 歲以上但不是學生，180 元

你要如何完成這段程式碼？

```python
def ticket_fee(age, school):
    fee = 0
    (A.)
        fee = 60
    (B.)
        (C.)
            fee = 120
        else:
            fee = 180
    return fee
```

1. `if age >= 5 and school = True:`
2. `if age >= 5 and school = False:`
3. `if age <= 17:`

```python
answer_35 = dict()
```

## 36.（連連看）你設計一個 Python 程式檢查使用者輸入的數字是 1 位數或者 2 位數，其中規定輸入的值必須是正整數，你要如何完成這段程式碼？

```python
num = int(input("Enter a number with 1 or 2 digits:"))
if num > 0:
    (A.)
        digits = "1"
    (B.)
        digits = "2"
    (C.)
        digits = ">2"
    print(digits + " digits.")
elif num == 0:
    print("The number is 0")
else:
    print("The number is not a positive number")
```

1. `if num < 10:`
2. `if num < 100:`
3. `elif num < 100:`
4. `else:`

```python
answer_36 = dict()
```

## 37.（連連看）你正在設計一個 Python 程式遊戲，讓參加的人從 1 到 100 之間猜一個數字，最多有三次機會，程式碼如下：

```python
from random import randint # 01
target = randint(1, 100) # 02
chance = 1 # 03
print("Guess an integer from 1 to 100. You will have 3 chances.") # 04
# 05
    guess = int(input("Guess an integer:")) # 06
    if guess > target: # 07
        print("Guess is too high") # 08
    elif guess < target: # 09
        print("Guess is too low") # 10
    else: # 11
        print("Guess is just right") # 12
# 13
# 14
```

程式可以讓使用者猜三次，如果猜出正確數字即停止程式，你要如何完成列號 05、13、14 的程式碼？請將正確的程式碼片段與問題相連。

問題

A. 在 05 列你要使用哪個程式碼片段？
B. 在 13 列你要使用哪個程式碼片段？
C. 在 14 列你要使用哪個程式碼片段？

程式碼片段

1. `while chance <= 3:`
2. `while chance < 3:`
3. `break`
4. `pass`
5. `chance += 1`
6. `chance = 2`

```python
answer_37 = dict()
```

## 38.（連連看）在以下的程式碼中，要加入哪些程式碼片段可以正確執行？

```python
aList = [1, 2, 3]
bList = ["a", "b", "c"]
(A.)
    print("aList is equal to bList")
(B.)
    print("aList is not equal to bList")
```

1. `if aList == bList:`
2. `elif aList == bList:`
3. `else:`
4. `else if:`

```python
answer_38 = dict()
```

## 39.（連連看）你設計了一個 Python 程式來檢查英文姓名的大小寫，請選擇四個程式碼片段完成這個程式。

```python
(A.)
(B.)
(C.)
(D.)
```

1. `name = input("Enter your English name:")`
2. 

```python
elif name.lower() == name:
    print(name, "is all lower case.")
```

3. 

```python
else:
    print("name", "is upper case.")
```

4. 

```python
else:
    print("name", "is mixed case.")
```

5. 

```python
if name.upper() == name:
    print(name, "is all upper case.")
```

6.

```python
else:
    print("name", "is lower case.")
```

```python
answer_39 = dict()
```

## 40.（連連看）公司決定要幫所有年薪不到 50 萬的員工調升基本工資 5%，並給予獎金 1 萬元：

```
新工資 = 目前工資 * 105% + 10000
```

`salaryList` 是由員工資料庫取得，你要如何完成這段程式碼？

```python
(A.)
    if salaryList[index] >= 500000:
        (B.)
    salaryList[index] = (salaryList[index] * 1.05) + 10000
```

缺漏處

A. 從 1. 至 4. 擇一
B. 從 5. 至 8. 擇一

1. `for index in range(len(salaryList) + 1):`
2. `for index in range(len(salaryList) - 1):`
3. `for index in range(len(salaryList)):`
4. `for index in salaryList:`
5. `exit()`
6. `continue`
7. `break`
8. `end`