import logging

from Chapter08 import (
    monte_carlo_pi,
    monte_carlo_integrator
)

import os


def test_smoke():
    print(f"PATH={os.environ['PATH']}")

    logging.info("fire?")
