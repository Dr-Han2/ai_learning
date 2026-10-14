"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""

#示例1: 生成键1-5, 值为键的平方的字典
# key = n value = n ** 2
dict1 = {i : i**2 for i in range(1,6)}
print(f"dict1={dict1}")

#示例2: 生成键为字母a-e 值为字母大写的字母
print("=" * 30)
print(chr(65))#对应的ASCII码
print(chr(97))

#生成键为字母a-e (97+0,97+1...) A-E(65+0,65+...)
dict2={chr(97+i) : chr(65+i) for i in range(5)}
print(dict2)

#示例3:筛选已有字典中,值大于50的键值对,生成新字典
old_dict ={"a": 30, "b": 60, "c": 40, "d": 70, "e": 80, "f": 90}
dict3 ={key: value for key, value in old_dict.items() if value > 50}
print(dict3)