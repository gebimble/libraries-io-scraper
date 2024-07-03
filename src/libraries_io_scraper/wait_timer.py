import functools
from time import perf_counter, sleep

from loguru import logger  # type: ignore


WAIT_LENGTH = 1  # seconds


def wait_a_second(func):  # pragma: no cover
    @functools.wraps(func)
    def wrapper_wait_a_second(*args, **kwargs):
        start = perf_counter()

        return_value = func(*args, **kwargs)

        elapsed = perf_counter() - start
        logger.debug(f"Time elapsed: {elapsed}s.")

        if (remaining := WAIT_LENGTH - elapsed) > 0:
            logger.debug(
                f"{remaining} remaining to prevent excessive requests."
            )  # noqa: E501
            sleep(remaining)

        return return_value

    return wrapper_wait_a_second
