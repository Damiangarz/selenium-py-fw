import inspect
import logging
import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    @staticmethod
    def remove_char(line):
        line = line.translate({ord(c): None for c in '\n$, '})
        return line

    @staticmethod
    def remove_dot(line):
        line = line.translate({ord(c): None for c in '.'})
        return line

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger
