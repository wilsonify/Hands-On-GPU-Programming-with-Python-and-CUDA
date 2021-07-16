from pprint import pprint

import pycuda
import pycuda.driver as drv

capability_to_cores_per_mp_map = {
    3.0: 128,
    5.0: 128,
    5.1: 128,
    5.2: 128,
    6.0: 64,
    6.1: 128,
    6.2: 128
}

drv.init()

print('CUDA device query (PyCUDA version) \n')

print('Detected {} CUDA Capable device(s) \n'.format(drv.Device.count()))

for i in range(drv.Device.count()):
    gpu_device = drv.Device(i)
    """
    The following will give us all remaining device attributes as seen
    in the original deviceQuery.
    We set up a dictionary as such so that we can easily index
    the values using a string descriptor.
    Cores per multiprocessor is not reported by the GPU!
    We must use a lookup table based on compute capability.
    See the following:
    http://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#compute-capabilities
    """

    compute_capability = float('%d.%d' % gpu_device.compute_capability())
    cuda_cores_per_mp = capability_to_cores_per_mp_map[compute_capability]
    total_memory = gpu_device.total_memory() // (1024 ** 2)
    device_attributes_tuples = iter(gpu_device.get_attributes().items())
    device_attributes = {}

    for k, v in device_attributes_tuples:
        device_attributes[str(k)] = v
    num_mp = device_attributes['MULTIPROCESSOR_COUNT']
    device_attributes["Device #"] = gpu_device.name()
    device_attributes["Compute Capability"] = compute_capability
    device_attributes["Total Memory (MB)"] = total_memory
    device_attributes["Multiprocessors"] = num_mp
    device_attributes["CUDA Cores / Multiprocessor"] = cuda_cores_per_mp
    device_attributes["CUDA Cores"] = num_mp * cuda_cores_per_mp
    pprint(device_attributes)
