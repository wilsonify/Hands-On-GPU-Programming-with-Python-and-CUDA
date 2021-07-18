from subprocess import Popen

import numpy as np
import pycuda
from pycuda import gpuarray
from pycuda.scan import InclusiveScanKernel

if __name__ == "__main__":
    from pycuda import autoinit
    assert '_finish_up' in dir(autoinit)
    popen = Popen(["nvcc", "--version"])
    stdout_data, stderr_data = popen.communicate()
    seq = np.array([1, 2, 3, 4, 5, 6, 7], dtype=np.int16)
    seq_gpu = gpuarray.to_gpu(seq)
    sum_gpu = InclusiveScanKernel(np.int32, "a+b")
    print(sum_gpu(seq_gpu).get())
    print(np.cumsum(seq))
