"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from model.clazz import Clazz
from service.clazz_service import ClazzService

def test_add():
    clazz = Clazz(name="测试123班",teacher_name="测试123班班主任")

    clazz = ClazzService.add(clazz)

    assert clazz.id is not None