## xwp_cython : X-ray Wave Propagation in Cython

This is an auxiliary repo to the [xwp](https://github.com/s-sajid-ali/xwp) repo. 

Currently implemented  :
- Direct evaluation of fresnel integral in 1D and 2D in cython.
    - 1D : parallelized version
    - 2D : 2loop and 4loop versions. 
  
#### Requirements:
Listed in `pyproject.toml`, these include : Setuptools, Numpy, Cython and a working C compiler that supports OpenMP

#### Compiling: 
Clone the directory via git clone and run ` CC=compiler-name CFLAGS="-O3 -ffast-math -march=native -mtune=native" pip install . -v`, `pip` will read the `pyproject.toml` to automatically use `setuptools.build_meta` backend to compile the `Cython` sources, create a wheel and install it.

(Note that the master branch builds with `gcc` using the `-march=native` compiler flag. The intel_avx2 is an old branch that hasn't been updated but might be.)

#### Note:
All physical quantities have SI units.

The direct wave propagation is somewhat optimized but much more can be done in terms of memeory reuse (so that the same part of the input wave is not repeatedly flushed from the cache). 

Different integration schemes could give better performance but have not been expreimented here. For example, [quadpy](https://github.com/nschloe/quadpy) contains many schemes for 1D and 2D integrals and handles complex integration as well.
