import logging
import os
import platform
from pprint import pprint

from Chapter01 import mandelbrot0


def test_smoke():
    pprint(os.environ)
    print(f"PATH={os.environ['PATH']}")
    print(platform.system())
    logging.info("fire?")


def test_simple_mandelbrot():
    mandel = mandelbrot0.simple_mandelbrot(512, 512, -2, 2, -2, 2, 256, 2.5)
    assert mandel.shape == (512, 512)
