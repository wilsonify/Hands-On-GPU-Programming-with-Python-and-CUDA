import logging

from Chapter07 import (
    conv_2d,
    cublas_gemm_flops
)

import os


def test_smoke():
    print(f"PATH={os.environ['PATH']}")

    logging.info("fire?")
