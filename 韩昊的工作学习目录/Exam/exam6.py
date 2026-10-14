"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
class Employee:
    def __init__(self,name,position,salary):
        self.__name = name
        self.__position = position
        self.__salary = salary
    #打印员工的信息 包括姓名 职位 薪资
    def show_info(self):
        print(f"姓名:{self.__name}、职位:{self.__position}、薪资:{self.__salary}")

    def update_salary(self,new_salary):
        if new_salary < 0:
            raise ValueError("薪资不能 为负数！")
        self.__salary = new_salary
        print(f"薪资修改成功,{self.__name}的薪资为:{self.__salary}")

    def get_salary(self):
        return self.__salary
class Management:
    def __init__(self):
        self.employees = [] #用于存储员工对象

    def add_employees(self,employee):
        self.employees.append(employee)
        print(f"成功添加员工:{employee._Employee__name}") #在类外 Python不会编译成_Emplotyy__name,故若直接写__name,会报错

    #查询所有员工
    def show_all_employees(self):
        print(f"\n--- 所有员工信息 ---")
        if not self.employees:
            print("暂无员工")
        for emp in self.employees:
            emp.show_info()

    #查询所有高新员工(薪资＞ 10000)
    def show_high_salary_employee(self):
        print(f"\n--- 高薪员工(薪资 > 10000) --- ")
        found = False
        for emp in self.employees:
            if emp.get_salary() > 10000:
                emp.show_info()
                found = True
        if not found:
            print("没有高薪员工")
if __name__ == "__main__":
    manager = Management()

    emp1 = Employee("张三","热力学工程师",10000)
    emp2 = Employee("李四", "电气工程师", 12000)
    emp3 = Employee("王五", "软件测试员", 8000)
    emp4 = Employee("赵六", "电焊工", 7500)

    #添加员工
    print("--- 添加员工 ---")
    manager.add_employees(emp1)
    manager.add_employees(emp2)
    manager.add_employees(emp3)
    manager.add_employees(emp4)

    manager.show_all_employees()

    manager.show_high_salary_employee()

    try:
        emp1.update_salary(-500)
    except ValueError as e:
        print(f"捕获异常成功")

    #正常修改员工薪资
    emp2.update_salary(10000)
    emp2.show_info()


