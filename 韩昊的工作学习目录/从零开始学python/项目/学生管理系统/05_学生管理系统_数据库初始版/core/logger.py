"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler
from utils.env_util import EnvUtil

# 获取日志配置
LOG_LEVEL = EnvUtil.LOG_LEVEL
LOG_DIR = EnvUtil.LOG_DIR
LOG_NAME = EnvUtil.LOG_NAME

# ============ 终端颜色支持 ============
class Colors:
    """终端颜色"""
    # 字体颜色
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[93m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_WHITE = '\033[97m'

    # 背景颜色
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_PURPLE = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

    # 样式
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSE = '\033[7m'

    # 重置
    RESET = '\033[0m'


class ColoredFormatter(logging.Formatter):
    """带颜色的日志格式化器"""

    # 级别颜色映射
    LEVEL_COLORS = {
        'DEBUG': Colors.CYAN,
        'INFO': Colors.GREEN,
        'WARNING': Colors.YELLOW,
        'ERROR': Colors.RED,
        'CRITICAL': Colors.BG_RED + Colors.BRIGHT_WHITE + Colors.BOLD,
    }

    def format(self, record):
        """格式化日志记录"""
        # 获取级别颜色
        level_color = self.LEVEL_COLORS.get(record.levelname, Colors.WHITE)

        # 原始格式
        msg = super().format(record)

        # 添加颜色
        return f"{level_color}{msg}{Colors.RESET}"


class Logger:
    """
    高级日志工具（带颜色、自动切割、性能统计）
    """

    _instance = None
    _loggers = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_logger(cls, name=None, log_dir=None, log_level=None,
                   console=True, file=True, color=True):
        """
        获取日志实例

        Args:
            name: 日志名称
            log_dir: 日志目录
            log_level: 日志级别
            console: 是否输出到控制台
            file: 是否输出到文件
            color: 是否使用颜色（仅控制台）

        Returns:
            logging.Logger: 日志实例
        """



        # 设置日志级别
        log_level = log_level or LOG_LEVEL
        # 设置日志目录
        log_dir = log_dir or LOG_DIR
        # 设置日志名称
        name = name or LOG_NAME

        key = f"{name}_{console}_{file}_{color}"
        if key in cls._loggers:
            return cls._loggers[key]

        logger = logging.getLogger(name)
        logger.setLevel(log_level)

        # 清除已有处理器
        if logger.handlers:
            logger.handlers.clear()

        # 控制台处理器
        if console:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(log_level)

            if color:
                formatter = ColoredFormatter(
                    '%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                )
            else:
                formatter = logging.Formatter(
                    '%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                )

            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        # 文件处理器
        if file:
            # 确保目录存在
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            log_file = os.path.join(log_dir, f"{name or 'app'}.log")

            # 按时间切割（每天）
            file_handler = TimedRotatingFileHandler(
                log_file,
                when='midnight',
                interval=1,
                backupCount=30,
                encoding='utf-8'
            )
            file_handler.setLevel(log_level)

            file_formatter = logging.Formatter(
                '%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(funcName)s | %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

        cls._loggers[key] = logger
        return logger


# ============ 便捷函数 ============

_logger = Logger.get_logger()

def get_logger(name=None, **kwargs):
    """获取日志实例"""
    return Logger.get_logger(name, **kwargs)

def debug(msg, *args, **kwargs):
    """调试信息	开发调试，详细信息，生产禁止使用"""
    _logger.debug(msg, *args, **kwargs)

def info(msg, *args, **kwargs):
    """一般信息	程序正常运行状态"""
    _logger.info(msg, *args, **kwargs)

def warning(msg, *args, **kwargs):
    """警告	潜在问题，程序仍可运行"""
    _logger.warning(msg, *args, **kwargs)

def error(msg, *args, **kwargs):
    """错误	功能异常，但程序可继续"""
    _logger.error(msg, *args, **kwargs)

def critical(msg, *args, **kwargs):
    """严重错误	程序可能崩溃，需要立即处理"""
    _logger.critical(msg, *args, **kwargs)

def exception(msg, *args, **kwargs):
    """记录异常（自动包含堆栈信息）"""
    _logger.exception(msg, *args, **kwargs)


if __name__ == "__main__":
    # 测试日志
    print("=" * 60)
    print("测试日志工具")
    print("=" * 60)

    # 获取日志实例
    # log = get_logger("test")
    log = get_logger()

    # 输出不同级别的日志
    log.debug("这是DEBUG级别日志，调试信息，开发调试，详细信息，生产禁止使用")
    log.info("这是INFO级别日志，一般信息，程序正常运行状态")
    log.warning("这是WARNING级别日志，警告，潜在问题，程序仍可运行")
    log.error("这是ERROR级别日志，错误，功能异常，但程序可继续")
    log.critical("这是CRITICAL级别日志，严重错误，程序可能崩溃，需要立即处理")

    # 带参数的日志
    user_id = 123
    user_name = "张三"
    log.info(f"用户登录成功，ID: {user_id}, 名称: {user_name}")

    # 异常日志
    try:
        result = 10 / 0
    except Exception as e:
        log.error(f"计算错误: {e}", exc_info=True)  # 显示栈追踪信息