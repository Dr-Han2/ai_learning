"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""


# 类方法
class Student:
    # 学校名
    schlool_name = "中国大学"

    @classmethod
    def update_school_name(cls, name):
        # 校验
        if not name:
            raise ValueError("名字不能为空")
        #更新属性
        cls.schlool_name = name

#修改之前的类属性
print(f"修改之前的类属性{Student.schlool_name}")
#调用修改方法
Student.update_school_name("中国小学")
print(f"修改之后的类属性{Student.schlool_name}")
