"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/12 15:55
@Version : 1.0
"""
from fastapi import APIRouter, Path, Query, Depends
from core import logger
from core.page_request import PageRequest
from core.page_result import PageResult
from dto.clazz_dto import ClazzAddDTO
from dto.clazz_dto import ClazzUpdateDTO
from model.clazz import Clazz
from service.clazz_service import ClazzService
from core.response import Response
from typing import Annotated

log = logger.get_logger()

router = APIRouter(prefix="/api/clazz", tags=["班级管理"])


@router.post("/add")
def add_clazz(clazz_dto: ClazzAddDTO):
    """新增班级"""
    clazz = Clazz(name=clazz_dto.name, teacher_name=clazz_dto.teacher_name)
    ClazzService.add(clazz)
    log.debug(f"新增班级成功 {clazz}")
    return Response[Clazz].success()


@router.post("/post")
def update_clazz(clazz_dto: ClazzUpdateDTO):
    """更新班级"""
    clazz = Clazz(id=clazz_dto.id, name=clazz_dto.name, teacher_name=clazz_dto.teacher_name)
    ClazzService.update(clazz)
    log.debug(f"更新班级成功 {clazz}")
    return Response[Clazz].success()


def check_id(
        id: int = Path(..., gt=0, title="ID", description="班级ID", ge=1)
):
    """校验id参数"""
    return id


@router.delete("/delete/{id}")
def delete_clazz_by_id(id: int = Depends(check_id)):
    """删除班级"""
    ClazzService.delete(id)
    log.debug(f"删除班级成功 {id}")
    return Response.success(message="删除成功")


@router.get("/select/{id}")
def select_clazz_by_id(id: int = Depends(check_id)):
    """根据ID查询班级信息"""
    clazz = ClazzService.select_by_id(id)
    log.debug(f"根据ID查询班级信息成功 {id}")
    return Response[Clazz].success(data=clazz)


@router.get("/select_by_name/{name}")
def select_clazz_by_name(name: str = Path(..., min_length=2, title="班级名", description="通过班级名查询，最小长度为2个字符")):
    """根据班级名查询班级信息"""
    clazz = ClazzService.select_by_name(name)
    log.debug(f"根据班级名查询班级信息成功 {name}")
    return Response[Clazz].success(data=clazz)


@router.get("/page", response_model=Response[PageResult[Clazz]])
def select_clazz_by_page(page_req: Annotated[PageRequest, Query()]):
    """分页查询班级信息"""
    page_result = ClazzService.select_page(page_req)
    log.debug(f"分页查询班级信息成功 {page_result}")
    return Response[PageResult[Clazz]].success(data=page_result)