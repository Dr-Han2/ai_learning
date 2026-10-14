"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#创建一个类
class Student:
    """
    学生类
    """
    #定义一个属性
    school_name = "中国大学"
    #定义一个方法
    def study(self):
        print("正在学习...")

    #定义考试方法
    def take_exam(self,subject ):
        print(f"正在参加{subject}考试...")

#实例化一个对象(每次实例化都会在类中产生一个新对象)
zhang_san= Student()
li_si =Student()
#查考类型
print(type(zhang_san))
print(type(li_si))
#判断两个对象是否同一个对象
print(zhang_san is li_si)

#查考内存地址
print(f"zhang_san id={id(zhang_san)}")
print(f"li_si id={id(li_si)}")

#访问
print(f"张三的学校是:{zhang_san.school_name}")
#调用方法
zhang_san.study()
zhang_san.take_exam("数学")