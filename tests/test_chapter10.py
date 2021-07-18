import logging

from Chapter10 import (
    cuda_driver,
    mandelbrot_driver,
    mandelbrot_ptx,
    mandelbrot_ctypes
)

import os


def test_smoke():
    print(f"PATH={os.environ['PATH']}")

    logging.info("fire?")
