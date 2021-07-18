import logging

from Chapter11 import (
    atomic,
    dynamic_hello, # Minimum compute capability for dynamic parallelism is 3.5
    dynamic_quicksort, # Minimum compute capability for dynamic parallelism is 3.5
    performance_sum_ker,
    ptx_assembly,
    shfl_sum,
    shfl_xor,
    sum_ker,
    vectorized_memory,
)

import os


def test_smoke():
    print(f"PATH={os.environ['PATH']}")

    logging.info("fire?")
