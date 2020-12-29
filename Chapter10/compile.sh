nvcc -ptx -o mandelbrot.ptx mandelbrot.cu
nvcc -Xcompiler -fPIC -shared -o mandelbrot.so mandelbrot.cu