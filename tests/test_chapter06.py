import logging

from Chapter06 import (
    broken_matrix_ker,
    hello_world_gpu,
    matrix_ker,
)

import os


def test_smoke():
    print(f"PATH={os.environ['PATH']}")
    print(f"CUDA_PATH={os.environ['CUDA_PATH']}")
    logging.info("fire?")
