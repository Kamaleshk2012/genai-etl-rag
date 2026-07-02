import logging as lg

def setup_logging():
    lg.basicConfig(
        level=lg.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

logger = lg.getLogger(__name__)