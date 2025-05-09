# proj-its-certification-python
Project: ITS Certification Python.

## 練習題指引

- 將練習題的 GitHub Repository 下載到自己的電腦，解壓縮後以 VS Code 開啟專案資料夾。
- 先閱讀 `README.md`，再將答案寫在 `answers.py`
- 練習題共分為四種：
  - 是非題：預設答案 `answer_01 = None`，請以布林型別宣告答案，若覺得是非題的敘述**不正確**，就宣告 `answer_01 = False`，若覺得是非題的敘述**正確**則宣告 `answer_01 = True`
  - 單選題：預設答案 `answer_02 = None`，請以整數型別宣告答案，若覺得單選題的第一個選項**正確**宣告為 `answer_02 = 1`，若覺得單選題的第二個選項**正確**則宣告 `answer_02 = 2`，若覺得單選題的第三個選項**正確**則宣告 `answer_02 = 3`，若覺得單選題的第四個選項**正確**則宣告 `answer_02 = 4`
  - 複選題：預設答案 `answer_03 = set()`，請以集合資料結構宣告答案，若覺得複選題的第一個選項、第三個選項與第四個選項**正確**，則宣告為 `answer_03 = {1, 3, 4}`
  - 連連看：預設答案 `answer_04 = dict()`，請以字典資料結構宣告答案，若覺得連連看的 `A` 應該與 `1` 相連，則宣告為 `answer_04 = {"A": 1}`
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

1. [[1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6]]
2. [4, 10, 18]
3. [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
4. [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]

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

執行程式碼的輸出值是？

1. `30.0`
2. `30.5`
3. `457`
4. `SyntaxError`