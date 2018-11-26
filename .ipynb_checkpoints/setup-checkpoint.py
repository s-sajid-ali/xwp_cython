from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np 

ext_modules=[
        Extension('prop1d_cython',
        sources=['xwp_cython/prop1d_cython.pyx'],
        extra_compile_args=['-O3','-fopenmp','-xcore-avx2','-I/opt/intel/compilers_and_libraries_2018.3.222/linux/compiler/lib/intel64/libimf.a'],
        language='c'),
    
        Extension('prop2d_cython_2_loop',
        sources=['xwp_cython/prop2d_cython_2_loop.pyx'],
        extra_compile_args=['-O3','-fopenmp','-xcore-avx2','-I/opt/intel/compilers_and_libraries_2018.3.222/linux/compiler/lib/intel64/libimf.a'],
        language='c'),
    
        Extension('prop2d_cython_4_loop_serial',
        sources=['xwp_cython/prop2d_cython_4_loop_serial.pyx'],
        extra_compile_args=['-O3','-fopenmp','-xcore-avx2','-I/opt/intel/compilers_and_libraries_2018.3.222/linux/compiler/lib/intel64/libimf.a'],
        language='c'),
        
        Extension('prop2d_cython_4_loop_parallel',
        sources=['xwp_cython/prop2d_cython_4_loop_parallel.pyx'],
        extra_compile_args=['-O3','-fopenmp','-xcore-avx2','-I/opt/intel/compilers_and_libraries_2018.3.222/linux/compiler/lib/intel64/libimf.a'],
        language='c')
        ]

if __name__ == "__main__":
    setup(

    name = 'xwp_cython',
    packages=['xwp_cython'],
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules,
    include_dirs=[np.get_include()],
    
    description='X-ray wave propagation techniques in cython',
    url='https://github.com/s-sajid-ali/xwp_cython',
    author='Sajid',
    author_email='sajidsyed2021@u.northwestern.edu',
    zip_safe=False
        
    )
