"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import pymysql
from dotenv import load_dotenv

#创建 查询学生信息
load_dotenv()


def get_student_by_sno(sno: str):
    # 建立数据库链接
    conn=pymysql.connect(host="localhost",
                    port=3306,
                    user="root",
                    password="123456",
                    database='20260926_db',
                    charset='utf8mb4',
                )

    sql = (f"select id, name, sno, age, gender, enroll_date, class_id "
           f"from student where sno=%s")
    cursor = conn.cursor()
    cursor.execute(sql, (sno,))
    user=cursor.fetchone()
    cursor.close()
    conn.close()
    return user


if __name__ == '__main__':
    user = get_student_by_sno("100001")
    print(user)
    print(type(user))