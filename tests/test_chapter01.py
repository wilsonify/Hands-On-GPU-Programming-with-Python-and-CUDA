import logging
import os
import platform

from Chapter01 import mandelbrot0


def test_smoke():
    print(f"PATH={os.environ['PATH']}")
    print(f"CUDA_PATH={os.environ['CUDA_PATH']}")
    print(platform.system())
    logging.info("fire?")


def test_simple_mandelbrot():
    mandel = mandelbrot0.simple_mandelbrot(512, 512, -2, 2, -2, 2, 256, 2.5)
    assert mandel.shape == (512, 512)
