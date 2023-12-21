import sys

from loguru import logger

from .settings import Role, settings

logger.remove()
max_role_str_len = max(len(role.name) for role in Role)
role_str = f"{settings.role.name.replace('_', ' ').title():>{max_role_str_len}}"

logger_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
    "<blue>{extra[role]}</blue> - <level>{message}</level>"
)
logger.configure(extra={"role": role_str})
logger.add(
    sys.stderr,
    level="INFO",
    format=logger_format,
)
