import logging
from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(
    level=logging.ERROR, format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)
