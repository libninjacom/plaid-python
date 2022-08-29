import logging

logger = logging.getLogger("plaid2")


def enable_debug_logging():
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
