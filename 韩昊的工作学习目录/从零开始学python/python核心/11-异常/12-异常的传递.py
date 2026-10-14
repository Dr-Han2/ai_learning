"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 定义函数C：触发除零错误（无异常处理）
def func_c() :
    print("执行func_c：尝试计算10/0")
    result = 10 / 0  # 触发ZeroDivisionError，无处理
#用b调用c
def func_b():
    print("执行func_b,调用func_c")
    func_c()
#用a调用b
def func_a():
    print("执行func_a：调用func_b")
    func_b()
#func_a()

try:
    func_a()
except Exception as e:
    print("主程序:接收到异常",e)
print("主程序结束")