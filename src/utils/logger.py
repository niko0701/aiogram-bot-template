import logging
import sys
from pathlib import Path
from config import BASE_DIR


class ColoredFormatter(logging.Formatter):
    """Colored formatter for console output"""

    # ANSI colors
    COLORS = {
        "DEBUG": "\033[36m",  # Cyan
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "CRITICAL": "\033[35m",  # Magenta
    }
    RESET = "\033[0m"

    def format(self, record):
        # Add color to log level
        if record.levelname in self.COLORS:
            record.levelname = (
                f"{self.COLORS[record.levelname]}{record.levelname}{self.RESET}"
            )
        return super().format(record)


def setup_logger(
    name: str,
    level: int = logging.INFO,
    log_to_file: bool = True,
    log_to_console: bool = True,
    logs_dir: str = str(BASE_DIR / "logs"),
) -> logging.Logger:
    """
    Creates configured logger for module

    Args:
        name: Module name (e.g., 'admin', 'user', 'database')
        level: Logging level
        log_to_file: Whether to write logs to file
        log_to_console: Whether to output logs to console
        logs_dir: Directory for log files

    Returns:
        Configured logger
    """

    # Create logger with module name
    logger = logging.getLogger(f"bot.{name}")
    logger.setLevel(level)

    # Avoid handler duplication
    if logger.handlers:
        return logger

    # Create logs directory if it doesn't exist
    if log_to_file:
        Path(logs_dir).mkdir(exist_ok=True)

    file_format = logging.Formatter(
        fmt="%(asctime)s | %(name)s | %(levelname)s | %(funcName)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler
    if log_to_console:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)

        # Use colored formatter for console
        colored_formatter = ColoredFormatter(
            fmt="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
            datefmt="%H:%M:%S",
        )
        console_handler.setFormatter(colored_formatter)
        logger.addHandler(console_handler)

    # File handler for specific module
    if log_to_file:
        file_handler = logging.FileHandler(f"{logs_dir}/{name}.log", encoding="utf-8")
        file_handler.setLevel(level)
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)

        # General file with all logs
        general_handler = logging.FileHandler(f"{logs_dir}/bot.log", encoding="utf-8")
        general_handler.setLevel(level)
        general_handler.setFormatter(file_format)
        logger.addHandler(general_handler)

    return logger


def setup_root_logger(level: int = logging.INFO):
    """Setup root logger for third-party libraries"""

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Limit logging from third-party libraries
    logging.getLogger("aiogram").setLevel(logging.WARNING)
