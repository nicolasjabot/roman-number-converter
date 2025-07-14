# import logging

# # Configure logging with more details
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S'
# )

# def test_logging_levels():
#     logger = logging.getLogger(__name__)
#     logger.debug("A debug message")
#     logger.info("An info message")
#     logger.warning("A warning message")
#     logger.error("An error message")
#     logger.critical("A critical message")

# if __name__ == "__main__":
#     test_logging_levels()

from icecream import ic

def foo(i):
    return i + 333

ic(foo(123))