import logging

from Chapter04 import (
    conway_gpu,
    conway_gpu_syncthreads,
    conway_gpu_syncthreads_shared,
    naive_prefix,
    simple_scalar_multiply_kernel,
    work_efficient_prefix
)

import os


def test_smoke():
    print(f"PATH={os.environ['PATH']}")
    print(f"CUDA_PATH={os.environ['CUDA_PATH']}")
    logging.info("fire?")
