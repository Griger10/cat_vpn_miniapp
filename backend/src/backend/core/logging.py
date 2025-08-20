import logging


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] #%(levelname)-8s %(filename)s:"
               "%(lineno)d - %(name)s - %(message)s",
    )
