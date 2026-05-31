import logging

from app.utils.paths import user_data_dir


def setup_logging():
    log_file = user_data_dir() / "application.log"

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    logging.getLogger(__name__).info("Logging started")
