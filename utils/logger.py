import logging


def get_logger():

    logger = logging.getLogger("playwright_framework")

    if not logger.handlers:

        logger.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.propagate = False        # Prevent Log duplication

    return logger