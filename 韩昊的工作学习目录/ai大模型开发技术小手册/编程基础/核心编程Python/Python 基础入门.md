---
marp: true
paginate: true
theme: default
---

# Python 基础入门
### 从 print 到循环
韩昊 · 未来元启

---

# 目录
1. 初识 Python
2. 变量、常量、关键字
3. 数据类型与转换
4. 输入与运算符
5. 条件判断
6. 循环结构
7. 综合案例

---

# 1. 初识 Python
- `print()` 输出
- 字符串推荐双引号
- 注释：`#`，快捷键 `Ctrl + /`

```python
print("hello world")
print('hello python')
print("2 + 3")  # 字符串
```

- 转义字符：`\n` 换行、`\t` 制表、`\'` 单引号

---

# 1.1 格式化输出练习
```python
print("学号\t姓名\t性别\t年龄\t成绩")
print("S001\t光尘\t男\t18\t99")
```

- 常见错误：
  - 引号未闭合
  - 使用中文引号
  - 关键字不能作变量名

---

# 2. 变量与常量
- 变量：可重新赋值
- 常量：约定全大写，如 `PI`

```python
name = "python"
print(f"hello {name}")

name = "C++"
print(f"我正在学习{name}")

PI = 3.1415926
SCHOOL_NAME = "未来元启"
```

- Python 大小写敏感：`name` 与 `Name` 不同

---

# 3. 关键字与命名
- Python 保留字不能用作变量名

```python
import keyword
print(keyword.kwlist)
```

合法命名：
```python
a = "李四"
x = 95
y = True
```

非法命名：
```python
# 2name = "张三"
# class = "计算机"
```

---

# 4. 数据类型
```python
student_name = "张三"   # str
student_age = 18       # int
student_height = 1.75  # float
is_passed = True       # bool

print(type(student_name))
print(type(student_age))
```

- 常用类型：`str`、`int`、`float`、`bool`

---

# 4.1 类型转换
```python
age = int("18")       # 字符串 -> 整数
pi_int = int(3.14)    # 3，小数部分丢弃
str(100)              # "100"

bool(0)               # False
bool(100)             # True
bool("")              # False
bool(None)            # False
```

- `True + 1` 结果为 `2`

---

# 5. 输入函数 input
- `input()` 返回字符串
- 数值计算前需要转换类型

```python
name = input("请输入姓名：")
age = int(input("请输入年龄："))
address = input("请输入住址：")

print(f"姓名：{name}, 年龄：{age}, 住址：{address}")
```

---

# 5.1 练习：计算总分
```python
chinese = float(input("语文："))
math = float(input("数学："))
english = float(input("英语："))

total = chinese + math + english
print(f"总分 = {total}")
```

---

# 6. 运算符
```python
print(1 + 2)   # 3
print(10 - 2)  # 8
print(2 * 3)   # 6
print(10 / 3)  # 3.333...
print(10 // 3) # 3
print(10 % 3)  # 1
print(10 ** 2) # 100
```

- 优先级：`()` > `**` > `* / // %` > `+ -`
- 格式化：`f"{10 / 3:.3f}"` → `3.333`

---

# 6.1 比较与赋值
```python
a = 100
a += 100   # a = a + 100

print(10 > 5)   # True
print(10 < 5)   # False
print(10 >= 5)  # True
print(10 == 5)  # False
print(10 != 5)  # True
```

---

# 6.2 练习：购物花销
```python
APPLE_PRICE = 3.5
MILK_PRICE = 5.8

apple_count = float(input("苹果数量："))
milk_count = float(input("牛奶数量："))

result = APPLE_PRICE * apple_count + MILK_PRICE * milk_count - 8
print(f"最终花销：{result:.2f}")
```

---

# 7. 条件判断
```python
score = float(input("请输入分数："))

if score >= 60:
    print("考试通过")
else:
    print("考试不通过")
```

---

# 7.1 多分支判断
```python
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

---

# 7.2 条件嵌套
```python
age = int(input("年龄："))
has_id = bool(int(input("有身份证？0无 1有：")))

if age >= 18 and has_id:
    print("可以进入网吧")
elif age < 18 and not has_id:
    print("年龄和身份证都不满足")
elif age < 18:
    print("年龄不满足")
else:
    print("没有身份证")
```

---

# 7.3 作业：BMI / 奇偶 / 闰年
```python
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("过轻")
elif bmi < 25:
    print("正常")
elif bmi < 30:
    print("超重")
else:
    print("肥胖")
```

```python
if num % 2 == 0:
    print("偶数")
else:
    print("奇数")
```

```python
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("闰年")
else:
    print("平年")
```

---

# 8. range 与 for 循环
```python
range(5)         # 0 1 2 3 4
range(2, 8)      # 2~7
range(1, 11, 2)  # 1 3 5 7 9
range(10, 0, -1) # 10~1
```

```python
for i in range(5):
    print(i, end=" ")
```

---

# 8.1 for 循环累加
```python
result = 0

for i in range(1, 101):
    result += i

print(f"result = {result}")
```

- 计算 1 到 100 的累加和

---

# 9. 嵌套循环
## 九九乘法表
```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} x {i} = {j * i}", end="\t")
    print()
```

## 打印星星
```python
num = int(input("请输入行数："))

for i in range(1, num + 1):
    print("*" * i)
```

---

# 10. while 循环
```python
condition = 0

while condition < 100:
    print(condition)
    condition += 1

print(f"循环结束，condition = {condition}")
```

- 必须更新退出条件，避免死循环

---

# 10.1 break / continue
```python
while True:
    user_input = input("是否继续 y：")

    if user_input != "y":
        break      # 退出整个循环
    # continue     # 跳过本次，进入下一轮
```

- `break`：结束循环
- `continue`：跳过本次，继续下一轮

---

# 11. 综合案例：密码验证
```python
password = "123456"

while True:
    user_input = input("请输入密码：")

    if user_input == password:
        print("登录成功")
        break
    else:
        print("密码错误，请重新输入")
```

---

# 11.1 综合案例：猜数字
```python
import random

result = random.randint(1, 100)
count = 0

while True:
    guess = int(input("请输入 1~100："))
    count += 1

    if guess == result:
        print(f"猜对了，共猜了 {count} 次")
        break
    elif guess < result:
        print("猜小了")
    else:
        print("猜大了")
```

---

# 总结
- 输出：`print`、f-string、转义字符
- 变量/常量：命名、大小写敏感、关键字
- 类型：`str / int / float / bool` 与类型转换
- 输入：`input()` 返回字符串
- 运算：算术、比较、赋值
- 分支：`if / elif / else`、条件嵌套
- 循环：`for`、`range`、`while`
- 控制：`break / continue`
- 多练：BMI、九九乘法表、猜数字

---

# 谢谢
### 继续练习，编程就是不断试错