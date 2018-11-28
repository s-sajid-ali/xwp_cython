## xwp_cython : X-ray Wave Propagation in Cython

This is an auxiliary repo to the [xwp](https://github.com/s-sajid-ali/xwp) repo. 

Currently implemented  :
- Direct evaluation of fresnel integral in 1D and 2D in cython.
    - 1D : parallelized version
    - 2D : 2loop and 4loop versions. 
  
#### Requirements:
Numpy, Cython and a working C compiler that supports OpenMP

#### Compiling: 
The master branch builds with `gcc` (assuming `avx`enabled `x86_64` processor) while the intel_avx2 builds with `icc` (assuming `avx2` enabled `x86_64` processor). If the intel compiler is installed in a non-standard location (different from /opt/intel), please change the extra_compile_args accordingly.

Compiling with gcc can be done in the usual way by invoking `python setup.py install`\
Compiling with icc requires `LDSHARED="icc -shared" CC=icc python setup.py install` 
