"""
@Author  : 韩昊
@Company : *******
@Date    :
@Desc    :
@Version : 1.0
"""

weight = float(input('请输入您的体重(单位:kg)'))
height = float(input('请输入您的身高(单位:m)'))

BMI = weight / (height **2)
print(f'您的BMI是:{BMI:.2f}')

if BMI < 18.5:
    level =  '偏瘦'
elif BMI <24:
    level = '正常'
elif BMI < 28:
    level = '超重'
else:
    level = '肥胖'

print(f'您的BMI属于:{level}')