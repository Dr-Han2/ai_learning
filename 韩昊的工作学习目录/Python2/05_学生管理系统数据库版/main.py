"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import uvicorn
from fastapi import FastAPI
from core import logger
from core.exception_handler import ExceptionHandlerRegister

from controller import user_controller, clazz_controller, student_controller, course_controller, socre_controller
