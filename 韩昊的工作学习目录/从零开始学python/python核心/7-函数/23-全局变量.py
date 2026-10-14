"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# 定义一个全局变量，表示公司名
company_name = "xxxx科技有限公司"
# 定义一个全局变量，表示基本工资
base_salary = 5000

print(company_name, base_salary)

# 在函数中访问全局变量
def get_company_info():
    print(f"公司名：{company_name}")
    print(f"基本工资：{base_salary}")

# 调用函数
get_company_info()

# 直接给全局变量赋值
base_salary = 10000
# 调用函数
get_company_info()

# 在函数中修改全局变量
def update_global_variable():
    # 不使用global关键字，表示定义了一个与全局同名的局部变量
    # 如果要修改全局变量，必须用global声明
    global base_salary
    # 这时修改的才是全局变量
    base_salary = 20000
    print(f"全局变量base_salary已修改为：{base_salary}")

# 调用打印函数
print("*" * 30)
update_global_variable()
get_company_info()