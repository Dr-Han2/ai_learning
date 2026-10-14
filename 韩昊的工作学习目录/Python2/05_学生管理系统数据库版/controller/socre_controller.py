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
from dto.socre_dto import ScoreAddDTO, ScoreUpdateDTO
from model.socre import Score
from service.socre_service import ScoreService
from core.response import Response
from typing import Annotated

log = logger.get_logger()

router = APIRouter(prefix="/api/score", tags=["成绩管理"])


def check_id(
        id: int = Path(..., gt=0, title="ID", description="成绩ID", ge=1)
):
    """校验id参数"""
    return id


@router.post("/add")
def add_score(score_dto: ScoreAddDTO):
    """录入成绩"""
    score = Score(
        stu_id=score_dto.stu_id,
        course_id=score_dto.course_id,
        score=score_dto.score,
        exam_time=score_dto.exam_time
    )
    ScoreService.add(score)
    log.debug(f"录入成绩成功 {score}")
    return Response[Score].success()


@router.post("/post")
def update_score(score_dto: ScoreUpdateDTO):
    """修改成绩"""
    score = Score(
        id=score_dto.id,
        score=score_dto.score,
        exam_time=score_dto.exam_time
    )
    ScoreService.update(score)
    log.debug(f"修改成绩成功 {score}")
    return Response[Score].success()


@router.delete("/delete/{id}")
def delete_score_by_id(id: int = Depends(check_id)):
    """删除成绩"""
    ScoreService.delete(id)
    log.debug(f"删除成绩成功 {id}")
    return Response.success(message="删除成功")


@router.get("/select/{id}")
def select_score_by_id(id: int = Depends(check_id)):
    """根据ID查询成绩信息"""
    score = ScoreService.select_by_id(id)
    log.debug(f"根据ID查询成绩信息成功 {id}")
    return Response[Score].success(data=score)


@router.get("/select_by_student/{stu_id}")
def select_score_by_student(
        stu_id: int = Path(..., gt=0, title="学生ID", description="通过学生ID查询成绩")
):
    """根据学生ID查询成绩信息"""
    score_list = ScoreService.select_by_stu_id(stu_id)
    log.debug(f"根据学生ID查询成绩信息成功 {stu_id}")
    return Response[list[Score]].success(data=score_list)


@router.get("/select_by_course/{course_id}")
def select_score_by_course(
        course_id: int = Path(..., gt=0, title="课程ID", description="通过课程ID查询成绩")
):
    """根据课程ID查询成绩信息"""
    score_list = ScoreService.select_by_course_id(course_id)
    log.debug(f"根据课程ID查询成绩信息成功 {course_id}")
    return Response[list[Score]].success(data=score_list)


@router.get("/page", response_model=Response[PageResult[Score]])
def select_score_by_page(page_req: Annotated[PageRequest, Query()]):
    """分页查询成绩信息"""
    page_result = ScoreService.select_page(page_req)
    log.debug(f"分页查询成绩信息成功 {page_result}")
    return Response[PageResult[Score]].success(data=page_result)