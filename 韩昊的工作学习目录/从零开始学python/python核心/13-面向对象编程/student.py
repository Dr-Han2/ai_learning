"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import time
class Student:
    def __init__(self,name,student_no,age,gender,
                 score_dict):
        """
        初始化学生信息
        :param name:姓名
        :param student_no:学号
        :param age:年龄
        :param gender:性别
        :param score_dict:成绩字典
        """
        self.name = name
        self.student_no = student_no
        self.age = age
        self.gender = gender
        self.score = score_dict
        #正在上课
    def attend_class(self):
        "正在上课"
        print(f"学生{self.name}正在上课")

    def do_homework(self):
        """做作业"""
        print(f"学生 {self.name} 正在做作业。")

    def take_exam(self):
        """参加考试"""
        print(f"学生 {self.name} 正在参加考试。")
