"""
@Author  : hanhao
@Company : 未来元启
@Date    : 2026/10/9 10:18
@Desc    : 
@Version : 1.0
"""
from dao.clazz_dao import ClazzDao
from model.clazz import Clazz
from core.exceptions import ValidationError, BusinessException, AlreadyExistsError
from core import logger
from datetime import datetime

# 日志对象
log = logger.get_logger()


class ClazzService:
    """班级业务类"""

    @staticmethod
    def add(clazz: Clazz) -> Clazz:
        """新增班级记录"""
        # 校验
        if clazz is None:
            log.warning("班级信息不能为空.")
            raise ValidationError("班级信息不能为空.")
        if clazz.name is None or clazz.name.strip() == "":
            log.warning("班级名称不能为空.")
            raise ValidationError("班级名称不能为空.", field="name")
        if clazz.teacher_name is None or clazz.teacher_name.strip() == "":
            log.warning("班级教师名称不能为空.")
            raise ValidationError("班级教师名称不能为空.", field="teacher_name")

        # 唯一性校验：班级名不能重复
        if ClazzDao.select_by_name(clazz.name) is not None:
            log.warning("班级名称已存在.")
            raise AlreadyExistsError("班级", field="name", value=clazz.name)

        # 设置创建和更新时间
        now = datetime.now()
        clazz.create_time = now
        clazz.update_time = now

        # 调用DAO（DAO内部自行 commit/rollback/close）
        row = ClazzDao.insert(clazz)

        # 判断结果
        if row <= 0:
            log.warning("新增班级记录失败.")
            raise BusinessException("新增班级记录失败.")
        log.info("新增班级记录成功. 班级：%s", clazz)
        return clazz

    @staticmethod
    def update(clazz: Clazz) -> int:
        """更新班级记录"""
        if clazz is None or clazz.id is None:
            raise ValidationError("更新时必须传入班级 ID", field="id")

        # 如果传入了新班级名，检查是否和其他班级冲突
        if clazz.name is not None and clazz.name.strip() != "":
            exist = ClazzDao.select_by_name(clazz.name)
            if exist is not None and exist.id != clazz.id:
                raise AlreadyExistsError("班级", field="name", value=clazz.name)

        clazz.update_time = datetime.now()
        row = ClazzDao.update(clazz)
        if row == 0:
            log.warning("更新班级失败，未找到 id=%s", clazz.id)
        return row

    @staticmethod
    def delete(id: int) -> int:
        """删除班级"""
        if id is None:
            raise ValidationError("删除时必须传入班级 ID", field="id")
        row = ClazzDao.delete(id)
        if row == 0:
            log.warning("删除班级失败，未找到 id=%s", id)
        return row

    @staticmethod
    def get_by_id(id: int) -> Clazz:
        """按主键查询班级"""
        return ClazzDao.select_by_id(id)

    @staticmethod
    def get_by_name(name: str) -> Clazz:
        """按名称查询班级"""
        return ClazzDao.select_by_name(name)

    @staticmethod
    def list_all() -> list[Clazz]:
        """查询全部班级"""
        return ClazzDao.select_all()


if __name__ == '__main__':
    clazz = Clazz()
    clazz.name = "测试1班"
    clazz.teacher_name = "测试班主任"
    ClazzService.add(clazz)
    print("新增班级ID:", clazz.id)