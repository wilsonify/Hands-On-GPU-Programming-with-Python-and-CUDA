import logging

from Chapter03 import (
    deviceQuery,
    gpu_mandelbrot0,
    simple_element_kernel_example0,
    simple_scankernel0,
    simple_scankernel1,
    time_calc0
)

import os


def test_smoke():
    print(f"PATH={os.environ['PATH']}")
    print(f"CUDA_PATH={os.environ['CUDA_PATH']}")
    logging.info("fire?")
