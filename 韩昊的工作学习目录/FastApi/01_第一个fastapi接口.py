"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
#conda install fastapi uvicorn
#1 导入fastapi包
from fastapi import FastAPI


#创建导入的FasAPI实例(对象)
app = FastAPI(
    title ="第一个FastAPI接口",
    description ="This is an example of FastAPI application.",
    version="0.1.0",
)

#定义一个接口
@app.get("/")
def hello():
    """这是一个测试接口"""
    return {"message": "这是我的第一个FastAPI接口"}

