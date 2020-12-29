import logging

from Chapter05 import (
    conway_gpu_streams,
    gpu_mandelbrot_context_sync,
    multi_kernel,
    multi_kernel_events,
    multi_kernel_multi_thread,
    multi_kernel_streams,
    simple_context_create,
    simple_event_example,
    single_thread_example,
)

import os


def test_smoke():
    print(f"PATH={os.environ['PATH']}")
    print(f"CUDA_PATH={os.environ['CUDA_PATH']}")
    logging.info("fire?")
