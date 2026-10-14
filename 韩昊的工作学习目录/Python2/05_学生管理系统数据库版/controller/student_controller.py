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
from dto.student_dto import StudentAddDTO, StudentUpdateDTO
from model.student import Student
from service.student_service import StudentService
from core.response import Response
from typing import Annotated

log = logger.get_logger()

router = APIRouter(prefix="/api/student", tags=["学生管理"])


def check_id(
        id: int = Path(..., gt=0, title="ID", description="学生ID", ge=1)
):
    """校验id参数"""
    return id


@router.post("/add")
def add_student(student_dto: StudentAddDTO):
    """新增学生"""
    student = Student(
        stu_num=student_dto.stu_num,
        name=student_dto.name,
        gender=student_dto.gender,
        age=student_dto.age,
        class_id=student_dto.class_id,
        phone=student_dto.phone
    )
    StudentService.add(student)
    log.debug(f"新增学生成功 {student}")
    return Response[Student].success()


@router.post("/post")
def update_student(student_dto: StudentUpdateDTO):
    """更新学生"""
    student = Student(
        id=student_dto.id,
        stu_num=student_dto.stu_num,
        name=student_dto.name,
        gender=student_dto.gender,
        age=student_dto.age,
        class_id=student_dto.class_id,
        phone=student_dto.phone
    )
    StudentService.update(student)
    log.debug(f"更新学生成功 {student}")
    return Response[Student].success()


@router.delete("/delete/{id}")
def delete_student_by_id(id: int = Depends(check_id)):
    """删除学生"""
    StudentService.delete(id)
    log.debug(f"删除学生成功 {id}")
    return Response.success(message="删除成功")


@router.get("/select/{id}")
def select_student_by_id(id: int = Depends(check_id)):
    """根据ID查询学生信息"""
    student = StudentService.select_by_id(id)
    log.debug(f"根据ID查询学生信息成功 {id}")
    return Response[Student].success(data=student)


@router.get("/select_by_name/{name}")
def select_student_by_name(
        name: str = Path(..., min_length=1, title="学生姓名", description="通过姓名查询，可能返回多条")
):
    """根据姓名查询学生信息"""
    student_list = StudentService.select_by_name(name)
    log.debug(f"根据姓名查询学生信息成功 {name}")
    return Response[list[Student]].success(data=student_list)


@router.get("/select_by_stu_num/{stu_num}")
def select_student_by_stu_num(
        stu_num: str = Path(..., min_length=2, title="学生学号", description="通过学号查询学生")
):
    """根据学号查询学生信息"""
    student = StudentService.select_by_stu_num(stu_num)
    log.debug(f"根据学号查询学生信息成功 {stu_num}")
    return Response[Student].success(data=student)


@router.get("/select_by_class/{class_id}")
def select_student_by_class(
        class_id: int = Path(..., gt=0, title="班级ID", description="通过班级ID查询学生列表")
):
    """根据班级ID查询学生信息"""
    student_list = StudentService.select_by_class_id(class_id)
    log.debug(f"根据班级ID查询学生信息成功 {class_id}")
    return Response[list[Student]].success(data=student_list)


@router.get("/page", response_model=Response[PageResult[Student]])
def select_student_by_page(page_req: Annotated[PageRequest, Query()]):
    """分页查询学生信息"""
    page_result = StudentService.select_page(page_req)
    log.debug(f"分页查询学生信息成功 {page_result}")
    return Response[PageResult[Student]].success(data=page_result)