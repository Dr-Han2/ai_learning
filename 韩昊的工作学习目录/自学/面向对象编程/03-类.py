"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""

class Employee:
    empCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmpCount(self):
        print("Name:",self.name, "Salary:",self.salary)

#实例化对象
emp1 = Employee("ZHANG_SAN",5000)
emp2 = Employee("LI_SI",5000)
emp1.displayCount()
emp2.displayCount()
emp1.displayEmpCount()
emp2.displayEmpCount()
print(emp1.__dict__)#包含一个字典
print(emp2.__dict__)
