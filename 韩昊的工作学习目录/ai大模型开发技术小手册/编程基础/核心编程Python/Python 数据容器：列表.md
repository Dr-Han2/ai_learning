---
marp: true
paginate: true
theme: default
---

# Python 数据容器：列表
### 从多个变量到高效数据组织
韩昊 · 未来元启

---

# 目录
1. 为什么需要列表
2. 创建列表
3. 访问与修改
4. 添加与删除
5. 查找与切片
6. 遍历与嵌套
7. 综合练习

---

# 1. 不使用数据容器的局限性
- 存储多个学生需要多个变量
- 查找元素需要写很长的 `if / elif`
- 计算平均分也要逐个相加

```python
student1 = "张三"
student2 = "李四"
student3 = "王五"

if student1 == "李四":
    print("找到了")
elif student2 == "李四":
    print("找到了")
elif student3 == "李四":
    print("找到了")
else:
    print("没找到")

score1, score2, score3 = 90, 85, 92
average = (score1 + score2 + score3) / 3
print(f"平均分：{average}")
```

---

# 2. 使用列表
- 一个列表存储所有数据
- `in` 判断元素是否存在
- `sum()` / `len()` 快速计算

```python
students = ["张三", "李四", "王五"]

if "李四" in students:
    print("找到了")
else:
    print("没有找到")

scores = [90, 85, 92]
avg = sum(scores) / len(scores)
print(f"平均分 = {avg}")
```

---

# 3. 创建列表
```python
# 空列表
list0 = []

# 包含初始值
students = ["张三", "李四", "王五"]

# 元素类型不限
list1 = [1, "hello", True, 3.14, "张三"]

# 用 list() 转换
list2 = list("hello")      # ['h', 'e', 'l', 'l', 'o']

# 从 range 创建
list3 = list(range(1, 10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

# 4. 访问列表元素
- 下标从 `0` 开始
- 负数下标从末尾开始
- `len()` 获取长度
- 越界会报 `IndexError`

```python
students = ["张三", "李四", "王五", "赵六"]

print(students[0])        # 张三
print(students[2])        # 王五
print(students[-1])       # 赵六
print(len(students))      # 4

# print(students[50])     # IndexError
```

---

# 5. 添加元素
```python
fruit = []

# 末尾追加
fruit.append("苹果")
fruit.append("香蕉")

# 指定位置插入
fruit.insert(1, "橙子")

# 超出下标最大值会插到末尾
fruit.insert(30, "葡萄")

# 扩展另一个列表
list0 = ["哈密瓜", "橘子"]
fruit.extend(list0)
```

---

# 6. 查找元素
```python
goods = ["电脑", "平板", "耳机", "手机"]

# in / not in
print("手机" in goods)      # True
print("手表" not in goods)  # True

# index() 查找下标
print(goods.index("手机"))  # 3

# 找不到会报 ValueError
# print(goods.index("手表"))
```

---

# 7. 练习：随机组合
```python
import random

people = ["小明", "小红", "班主任", "校长", "大黄狗"]
place = ["操场", "垃圾桶旁"]
tool = ["拖鞋", "铅笔"]
action = ["跳科目三", "肚皮舞"]

people_item = random.choice(people)
place_item = random.choice(place)
tool_item = random.choice(tool)
action_item = random.choice(action)

print(f"{people_item}在{place_item}用{tool_item}{action_item}")
```

---

# 8. 更新列表元素
- 通过下标找到元素后重新赋值
- 修改时同样存在下标越界问题

```python
students = ["张三", "李四", "王五"]

students[1] = "赵六"
print(students)   # ['张三', '赵六', '王五']

# students[100] = "钱七"  # IndexError
```

---

# 9. 删除列表元素
```python
fruits = ["苹果", "梨", "香蕉", "橙子", "香蕉", "芒果"]

# 统计出现次数
print(fruits.count("香蕉"))  # 2

# pop() 删除末尾或指定下标
fruits.pop()                 # 删除末尾
del_item = fruits.pop(0)     # 删除下标 0

# remove() 删除指定值
fruits.remove("香蕉")

# del 删除下标
del fruits[0]

# clear() 清空
fruits.clear()
```

---

# 10. 列表切片
```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums[1:7]     # [1, 2, 3, 4, 5, 6]
nums[:4]      # [0, 1, 2, 3]
nums[-3:]     # [7, 8, 9]
nums[:]       # 全部
nums[::]      # 全部
nums[::-1]    # 反转
nums[-4:-1]   # [6, 7, 8]
```

- 语法：`[起始:结束:步长]`

---

# 11. 遍历列表
```python
employees = ["张三", "李四", "王五", "赵六"]

# 直接遍历
for emp in employees:
    print(emp)

# 同时获取下标和值
for index, emp in enumerate(employees):
    print(index, emp)

# while 循环
index = 0
while index < len(employees):
    print(index, employees[index])
    index += 1
```

---

# 11.1 排序与反转
```python
list1 = [2, 1, 56, 36, 10]
list1.reverse()          # [10, 36, 56, 1, 2]

list2 = [2, 1, 56, 36, 10]
list2.sort()             # [1, 2, 10, 36, 56]

list3 = [2, 1, 56, 36, 10]
list3.sort(reverse=True) # [56, 36, 10, 2, 1]
```

---

# 12. 列表中的列表
```python
list0 = [1, 2, 3, ["苹果", "香蕉"]]

# 取出子列表
item = list0[3]

# 修改子列表元素
list0[3][0] = "梨"

# 学生信息表
students = [
    ["张三", "13366669999", 18],
    ["李四", "13377778888", 19],
    ["王五", "13311112222", 20]
]
```

---

# 13. 综合练习：两数之和
```python
nums = [3, 3]
target = 6
length = len(nums)

for i in range(length):
    for j in range(i + 1, length):
        if nums[i] + nums[j] == target:
            print(f"{i}, {j}")
```

- 外层循环固定第一个数
- 内层循环从下一个开始找第二个数
- 找到和为目标值则输出下标

---

# 总结
- 列表是可变序列，可存储任意类型
- 创建：`[]`、`list()`、`list(range())`
- 访问：下标、负数下标、`len()`
- 添加：`append`、`insert`、`extend`
- 查找：`in`、`not in`、`index`、`count`
- 修改：下标赋值
- 删除：`pop`、`remove`、`del`、`clear`
- 切片：`[start:end:step]`
- 遍历：`for`、`enumerate`、`while`
- 嵌套：列表中可以放列表

---

# 谢谢
### 多练多用，列表是 Python 最常用的容器