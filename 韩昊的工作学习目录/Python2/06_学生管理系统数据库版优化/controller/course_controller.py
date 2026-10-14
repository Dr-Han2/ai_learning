"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/13 16:00
@Version : 1.0
"""
from fastapi import APIRouter, Path, Query, Depends
from core import logger
from core.page_request import PageRequest
from core.page_result import PageResult
from dto.course_dto import CourseAddDTO, CourseUpdateDTO
from model.course import Course
from service.course_service import CourseService
from core.response import Response
from typing import Annotated

log = logger.get_logger()

router = APIRouter(prefix="/api/course", tags=["课程管理"])


def check_id(
        id: int = Path(..., gt=0, title="ID", description="课程ID", ge=1)
):
    """校验id参数"""
    return id


@router.post("/add")
def add_course(course_dto: CourseAddDTO):
    """新增课程"""
    course = Course(
        name=course_dto.name,
        hour=course_dto.hour
    )
    CourseService.add(course)
    log.debug(f"新增课程成功 {course}")
    return Response[Course].success()


@router.post("/post")
def update_course(course_dto: CourseUpdateDTO):
    """更新课程"""
    course = Course(
        id=course_dto.id,
        name=course_dto.name,
        hour=course_dto.hour
    )
    CourseService.update(course)
    log.debug(f"更新课程成功 {course}")
    return Response[Course].success()


@router.delete("/delete/{id}")
def delete_course_by_id(id: int = Depends(check_id)):
    """删除课程"""
    CourseService.delete(id)
    log.debug(f"删除课程成功 {id}")
    return Response.success(message="删除成功")


@router.get("/select/{id}")
def select_course_by_id(id: int = Depends(check_id)):
    """根据ID查询课程信息"""
    course = CourseService.select_by_id(id)
    log.debug(f"根据ID查询课程信息成功 {id}")
    return Response[Course].success(data=course)


@router.get("/select_by_name/{name}")
def select_course_by_name(
        name: str = Path(..., min_length=2, title="课程名", description="通过课程名查询，最小长度为2个字符")
):
    """根据课程名查询课程信息"""
    course_list = CourseService.select_by_name(name)
    log.debug(f"根据课程名查询课程信息成功 {name}")
    return Response[list[Course]].success(data=course_list)


@router.get("/page", response_model=Response[PageResult[Course]])
def select_course_by_page(page_req: Annotated[PageRequest, Query()]):
    """分页查询课程信息"""
    page_result = CourseService.select_page(page_req)
    log.debug(f"分页查询课程信息成功 {page_result}")
    return Response[PageResult[Course]].success(data=page_result)