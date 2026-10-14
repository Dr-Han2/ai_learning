"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from sqlalchemy import create_engine,text

engine = create_engine(
    url="mysql+pymysql://root:123456@localhost:3306/20260926_db?charset=utf8mb4",
    pool_size=5, # 初始连接数
    max_overflow=10, # 最大连接数
    pool_timeout=30, # 连接超时时间（秒）, 建立连接时的等待时长
    pool_recycle=3600, # 连接回收时间（秒），连接回收时间，超过这个时间的连接将被回收
    pool_pre_ping=True, # 是否开启连接预检查，开启后会自动检查连接是否有效
    echo=True # 是否开启日志，开启后会打印SQL语句，上生产环境请关闭

)
# 定义一个函数，查询学生信息
def get_student_by_sno(sno) :
    # 获取一个数据库连接
    with engine.connect() as conn:
        # 定义SQL
        sql = text("select * from student where sno = :sno")
        # 绑定占位符并执行SQL
        result = conn.execute(sql, {"sno": sno})
        # 查看结果类型
        print(f"result 的类型是 {type(result)}")
        # 获取结果
        student = result.mappings().first() # 只获取第一条记录
        return student


if __name__ == '__main__':
    student = get_student_by_sno("100001")
    print(student)

