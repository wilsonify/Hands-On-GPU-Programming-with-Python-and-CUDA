import logging

from Chapter01 import mandelbrot0
from Chapter03 import (
    deviceQuery,
    gpu_mandelbrot0,
    simple_element_kernel_example0,
    simple_scankernel0,
    simple_scankernel1,
    time_calc0
)
from Chapter04 import *
from Chapter05 import *
from Chapter06 import *
from Chapter07 import *
from Chapter08 import *
from Chapter09 import *
from Chapter10 import *
from Chapter11 import *

import os


def test_smoke():
    logging.info(f"PATH={os.environ['PATH']}")
    logging.info("fire?")
