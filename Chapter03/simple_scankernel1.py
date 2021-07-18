import numpy as np

from pycuda import gpuarray
from pycuda.scan import InclusiveScanKernel

if __name__ == "__main__":
    from pycuda import autoinit

    assert '_finish_up' in dir(autoinit)

    seq = np.array([1, 100, -3, -10000, 4, 10000, 66, 14, 21], dtype=np.int32)
    seq_gpu = gpuarray.to_gpu(seq)
    max_gpu = InclusiveScanKernel(np.int32, "a > b ? a : b")
    print(max_gpu(seq_gpu).get()[-1])
    print(np.max(seq))
