"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/7/18 16:18
@Version : 1.0
"""
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from core import logger
from core.exceptions import AppException
from core.response import Response

logger = logger.get_logger()


class ExceptionHandlerRegister:
    """异常处理注册类"""

    @staticmethod
    def register(app: FastAPI):

        @app.exception_handler(AppException)
        def handle_app_exception(request: Request, exc: AppException):
            """捕获自定义业务异常"""
            resp = Response[None](
                code=exc.code,
                message=exc.message,
                data=None
            )
            logger.error(
                msg=f"业务异常 | Path: {request.url.path} | Method: {request.method} | Code: {exc.code} | Message: {exc.message}")
            return JSONResponse(content=resp.model_dump())

        @app.exception_handler(RequestValidationError)
        def handle_validation_exception(request: Request, exc: RequestValidationError):
            """FastAPI 参数校验异常"""
            msg_list = []
            for err in exc.errors():
                loc = err["loc"]
                field = loc[-1]
                err_type = err["type"]
                raw_msg = err["msg"]

                type_map = {
                    "string_too_short": "字符串长度不足",
                    "string_too_long": "字符串长度超出限制",
                    "greater_than": "数值必须大于最小值",
                    "less_than": "数值必须小于最大值",
                    "missing": "该参数必填",
                    "int_parsing": "必须传入整数",
                    "float_parsing": "必须传入数字",
                    "string_pattern_mismatch": "格式不匹配"
                }
                tip = type_map.get(err_type, raw_msg)
                msg_list.append(f"{tip}")

            logger.error(f"FastAPI校验异常| Path: {request.url.path} | Method: {request.method} | Message: {exc}")
            final_msg = "; ".join(msg_list)
            resp = Response.error(code=400, message="校验失败, " + final_msg)
            return JSONResponse(content=resp.model_dump())

        @app.exception_handler(Exception)
        def handle_global_err(request: Request, exc: Exception):
            """捕获未知异常"""
            logger.error(f"捕获全局未知异常: | Path: {request.url.path} | Method: {request.method} | Message: {exc}")
            resp = Response.error(code=500, message="服务器内部错误, 请联系管理员")
            return JSONResponse(content=resp.model_dump())