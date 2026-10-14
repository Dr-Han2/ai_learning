"""
@Author  : 韩昊
@Company : 未来元启
@Date    : 2026/7/10
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


class Colors:
    """终端颜色"""
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[93m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_WHITE = '\033[97m'

    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_PURPLE = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSE = '\033[7m'

    RESET = '\033[0m'


class ColoredFormatter(logging.Formatter):
    """带颜色的日志格式化器"""

    LEVEL_COLORS = {
        'DEBUG': Colors.CYAN,
        'INFO': Colors.GREEN,
        'WARNING': Colors.YELLOW,
        'ERROR': Colors.RED,
        'CRITICAL': Colors.BG_RED + Colors.BRIGHT_WHITE + Colors.BOLD,
    }

    def format(self, record):
        level_color = self.LEVEL_COLORS.get(record.levelname, Colors.WHITE)
        msg = super().format(record)
        return f"{level_color}{msg}{Colors.RESET}"


class Logger:
    """高级日志工具（带颜色、自动切割、性能统计）"""

    _instance = None
    _loggers = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_logger(cls, name=None, log_dir=None, log_level=None,
                   console=True, file=True, color=True):
        log_level = log_level or LOG_LEVEL
        log_dir = log_dir or LOG_DIR
        name = name or LOG_NAME

        key = f"{name}_{console}_{file}_{color}"
        if key in cls._loggers:
            return cls._loggers[key]

        logger = logging.getLogger(name)
        logger.setLevel(log_level)

        if logger.handlers:
            logger.handlers.clear()

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

        if file:
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            log_file = os.path.join(log_dir, f"{name or 'app'}.log")

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


_logger = Logger.get_logger()


def get_logger(name=None, **kwargs):
    """获取日志实例"""
    return Logger.get_logger(name, **kwargs)


def debug(msg, *args, **kwargs):
    _logger.debug(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    _logger.info(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    _logger.warning(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    _logger.error(msg, *args, **kwargs)


def critical(msg, *args, **kwargs):
    _logger.critical(msg, *args, **kwargs)


def exception(msg, *args, **kwargs):
    _logger.exception(msg, *args, **kwargs)