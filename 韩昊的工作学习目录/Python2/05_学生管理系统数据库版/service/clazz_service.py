"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/10/9 10:18
@Version : 1.0
"""
from core.page_request import PageRequest
from core.page_result import PageResult
from dao.clazz_dao import ClazzDao
from model.clazz import Clazz
from core.exceptions import ValidationError, BusinessException
from core import logger
from datetime import datetime
from utils.db_util import DBUtil

log = logger.get_logger()


class ClazzService:
    """班级业务类"""

    @staticmethod
    def add(clazz: Clazz) -> Clazz:
        """新增班级记录"""
        if clazz is None:
            log.warning("班级信息不能为空.")
            raise ValidationError("班级信息不能为空.")
        if clazz.name is None or clazz.name.strip() == "":
            log.warning("班级名称不能为空.")
            raise ValidationError("班级名称不能为空.")
        if clazz.teacher_name is None or clazz.teacher_name.strip() == "":
            log.warning("班级教师名称不能为空.")
            raise ValidationError("班级教师名称不能为空.")

        now = datetime.now()
        clazz.create_time = now
        clazz.update_time = now

        with DBUtil.session_dml() as _:
            row = ClazzDao.insert(clazz)

        if row <= 0:
            log.warning("新增班级记录失败.")
            raise BusinessException("新增班级记录失败.")
        log.info(f"新增班级记录成功. 班级：{clazz}")
        return clazz

    @staticmethod
    def update(clazz: Clazz) -> Clazz:
        """更新班级记录"""
        if clazz is None:
            log.warning("班级信息不能为空.")
            raise ValidationError("班级信息不能为空.")
        if clazz.id is None:
            log.warning("班级ID不能为空.")
            raise ValidationError("班级ID不能为空.")

        clazz.update_time = datetime.now()

        with DBUtil.session_dml() as _:
            row = ClazzDao.update(clazz)

        if row <= 0:
            log.warning("更新班级记录失败.")
            raise BusinessException("更新班级记录失败.")
        log.info(f"更新班级记录成功. 班级：{clazz}")
        return clazz

    @staticmethod
    def delete(id: int) -> bool:
        """删除班级记录"""
        if id is None:
            log.warning("班级ID不能为空.")
            raise ValidationError("班级ID不能为空.")

        with DBUtil.session_dml() as _:
            row = ClazzDao.delete(id)

        if row <= 0:
            log.warning("删除班级记录失败.")
            raise BusinessException("删除班级记录失败.")
        log.info(f"删除班级记录成功. 班级ID：{id}")
        return True

    @staticmethod
    def select_by_id(id: int) -> Clazz:
        """根据ID查询班级记录"""
        if id is None:
            log.warning("班级ID不能为空.")
            raise ValidationError("班级ID不能为空.")

        with DBUtil.session_readonly() as _:
            clazz = ClazzDao.select_by_id(id)

        return clazz

    @staticmethod
    def select_by_name(name: str) -> Clazz:
        """根据名称查询班级记录"""
        if name is None:
            log.warning("班级名称不能为空.")
            raise ValidationError("班级名称不能为空.")

        with DBUtil.session_readonly() as _:
            clazz = ClazzDao.select_by_name(name)

        return clazz

    @staticmethod
    def select_count() -> int:
        """获取班级记录数"""
        with DBUtil.session_readonly() as _:
            count = ClazzDao.select_count()

        return count

    @staticmethod
    def select_page(page_req: PageRequest) -> PageResult[Clazz]:
        """获取班级记录分页列表"""
        if page_req is None:
            log.warning("分页请求不能为空.")
            raise ValidationError("分页请求不能为空.")

        with DBUtil.session_readonly() as _:
            count = ClazzDao.select_count()
            if count <= 0:
                return PageResult.empty(page_req)

            clazz_list = ClazzDao.select_page(
                page_req.order_by,
                page_req.sort,
                page_req.offset,
                page_req.page_size
            )
            result = PageResult.of(page_req, count, clazz_list)
            return result