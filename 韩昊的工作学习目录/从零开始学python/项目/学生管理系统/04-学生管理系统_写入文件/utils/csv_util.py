"""
@Author  : 韩昊
@Company : *********
@Date    :
@Desc    :目前系统只处理学生信息 用单独的student.csv保存数据
         1. init      数据文件初始化
         2. load_data 从文件加载数据
         3. save_data 保存数据到文件
@Version : 1.0
"""
#导入csv模块，用于内置模块
import csv
#导入os模块 用于文件操作
import os
# 导入KYES
from config import kyes


#定义一个全局变量 设置csv文件的路径
CSV_FILE_PATH = "db/student.csv" #相对路径

#定义表头
HEADERS = [kyes.STU_ID, kyes.STU_NAME]

#1 . init 数据文件初始化
def init_csv_file():
    #如果文件存在则返回，不存在则创建它
    if os.path.exists(CSV_FILE_PATH):
        return
    #不存在则创建
    with open(CSV_FILE_PATH, 'w', encoding='utf-8-sig',newline='') as f:
        #绑定表头
        writer =csv.DictWriter(f,fieldnames=HEADERS)
        #写入表头
        writer.writeheader()

#2  . load_data 从文件加载数据
def load_data():
    # 1. 初始化csv文件,确保文件创建
    init_csv_file()
    # 2 . 定义一个空列表用于保存读取到的每一行
    student_list = []
    # 3 . 以只读模式打开
    with open(CSV_FILE_PATH, 'r', encoding='utf-8-sig',newline='') as f:
        #4 . 创建一个字典读取对象
        reader = csv.DictReader(f)
        #5 .遍历每一行数据
        for row in reader:
            #6 .将每一行数据加入到列表中
            student_list.append(row)
    # 7 . 返回学生列表
    return student_list

# 3 .save_data 保存数据到文件
# 把所有学生信息保存到csv文件中 ， 覆盖写入
def save_data(student_list):
    #1 以覆盖写入模式打开 写入每行数据
    with open(CSV_FILE_PATH, 'w', encoding='utf-8-sig',newline='') as f:
        #创建一个字典
        writer =csv.DictWriter(f,fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(student_list)
