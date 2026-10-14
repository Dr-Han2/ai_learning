"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 定义一个字典（书籍信息）
book_dict = {
    "id": "b001",
    "title": "Python入门",
    "author": "张三",
    "price": 59.9,
    "count": 50
}
print(f"原始字典 {book_dict}")
#1 使用pop删除字典中的元素
book_count = book_dict.pop("count")
print(f"删除后的字典:{book_dict}")

#2 删除不存在的KEY
book_count = book_dict.pop("count","未知KEY")
print(f"删除的值是:{book_count}")
print(f"删除元素的字典:{book_dict}")

#3 用del删除
del book_dict["price"]
print(f"清空字典后的字典:{book_dict}")

#4  清空字典.clear
book_dict.clear()
print(book_dict)

#5 删除字典 del
del book_dict
#NameError: name 'book_dict' is not defined
#print(book_dict)