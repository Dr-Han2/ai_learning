"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#功能要求
#让用户输入：用户名、邮箱、手机号，程序对这些内容进行清洗、校验、格式化输出。 覆盖字符串操作：
import sys

print("用户信息格式化小工具".title().center(30, "="))
#1 任务1 获取用户并清洗姓名
raw_name = input("请输入您的姓名")
if raw_name.strip() == "" or raw_name.isspace():
    print("姓名不能为空")
    sys.exit()
#去掉前后空格,并去掉中间空格,再首字母大写,其余小写
name = raw_name.strip()
name = name.replace(" ", "")
name = name[0].upper() + name[1:].lower()
#判断姓名是否为汉字
_ = name.isalpha()


#邮箱验证
raw_email = input("请输入邮箱:")
#去空格 转小写
email = raw_email.strip().replace(" ", "").lower()

if "@" not in email or "." not in email:
    print("邮箱格式错误,邮箱必须要有@或.")
    sys.exit()

if email.startswith("@") or email.endswith("@"):
    print("邮箱格式错误,@不能出现邮箱头或尾")
    sys.exit()
#@只能出现一次
if email.count("@") > 1:
    print("邮箱格式错误,@只能出现一次")
    sys.exit()
if email.count("@") != 1:
    print("邮箱格式错误,邮箱格式必需有一个@")
    sys.exit()

if email.find("@") > email.find(".") :
    print("邮箱格式错误,@必须在.前")
    sys.exit()

#验证电话号
raw_phone = input("请输入您的手机号")
#去掉所有空格、-、.
phone = raw_phone.replace(" ", "").replace("-", "").replace(".", "").replace(")", "")

#判断是否全为数字
if not phone.isdigit():
    print("手机号格式错误,必须全部是数字")
    sys.exit()
#判断是否为11位
if len(phone) != 11:
    print("手机号错误,必须是11位数字")
    sys.exit()

#手机号打码
masked_phone = phone[:3]+ "****" +phone[-4:]

width = 30

print(" 格式化后信息 ".center(width, "="))
print(f"姓名：{name}")
print(f"邮箱：{email}")
print(f"手机号：{masked_phone}")
print("=" * width)






