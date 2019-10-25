import logging

DEFAULT_LOGGER_FORMATTER = logging.Formatter(
    fmt = '[tpypipack|%(levelname)8s|%(asctime)s|%(module)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )

DEFAULT_LOGGER_NAME = 'templatepypipackagelogger'


def setup_logger(name=DEFAULT_LOGGER_NAME, formatter=DEFAULT_LOGGER_FORMATTER):
    """
    Creates a logger

    :param name: Name of the logger
    :type name: str, optional
    :param formatter: logging.Formatter object which determines the log string format
    :type formatter: logging.Formatter
    """

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger
