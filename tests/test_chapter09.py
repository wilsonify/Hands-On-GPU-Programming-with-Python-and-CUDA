import logging

from Chapter09 import (
    deep_neural_network
)

import os


def test_smoke():
    print(f"PATH={os.environ['PATH']}")

    logging.info("fire?")
