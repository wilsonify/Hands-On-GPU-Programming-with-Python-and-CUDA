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
    print(f"CUDA_PATH={os.environ['CUDA_PATH']}")
    logging.info("fire?")
