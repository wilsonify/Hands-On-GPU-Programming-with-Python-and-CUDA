import logging

from Chapter08 import (
    monte_carlo_pi,
    monte_carlo_integrator
)

import os


def test_smoke():
    print(f"PATH={os.environ['PATH']}")
    print(f"CUDA_PATH={os.environ['CUDA_PATH']}")
    logging.info("fire?")
