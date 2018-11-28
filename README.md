# xwp_cython : X-ray Wave Propagation in Cython

Direct evaluation of fresnel integral in 1D and 2D in cython.

The master branch builds with gcc (assuming avx enabled x86_64 processor) while the intel_avx2 builds with icc (assuming avx2 enabled x86_64 processor). If the intel compiler is installed in a non-standard location (different from /opt/intel), please change the extra_compile_args accordingly.
