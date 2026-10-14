"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from typing import Literal

import pydantic
from pydantic import BaseModel,Field

class UserModel(BaseModel):
    #定义参数
    id: int = Field(...,gt=0,title="ID标题",description="ID")
    name: str= Field(...,min_length=1,max_length=10,title="名称标题",description="名称")
    age: int= Field(...,ge=0,le=999,title="年龄标题",description="年龄必须要0-999之间")
    gender: Literal["男","女","保密"]= Field("保密", title="性别标题", description="性别")

if __name__=='__main__':
    user1= UserModel(id=1, name="张三", age="20", gender="男")
    print(user1)
