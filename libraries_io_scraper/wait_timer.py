from time import perf_counter, sleep
import functools

from loguru import logger  # type: ignore


def wait_a_second(func):  # pragma: no cover
    @functools.wraps(func)
    def wrapper_wait_a_second(*args, **kwargs):
        logger.debug("Entering time manager.")
        start = perf_counter()

        return_value = func(*args, **kwargs)

        elapsed = perf_counter() - start
        logger.debug(f"Time elapsed: {elapsed}s.")

        if (remaining := 10 - elapsed) > 0:
            logger.debug(f"{remaining} remaining to prevent excessive requests.")
            sleep(remaining)

        logger.debug("Function executed.")
        logger.debug("Exiting time manager.")
        return return_value

    return wrapper_wait_a_second
