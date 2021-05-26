from setuptools import setup
from setuptools.extension import Extension
from Cython.Distutils.build_ext import new_build_ext
import numpy as np

ext_modules = [
    Extension('xwp_cython.prop1d',
              sources=['xwp_cython/prop1d.pyx'],
              extra_compile_args=['-O3', '-fopenmp', '-march=native'],
              extra_link_args=['-lomp'],
              language='c'),

    Extension('xwp_cython.prop2d_2loop',
              sources=['xwp_cython/prop2d_2loop.pyx'],
              extra_compile_args=['-O3', '-fopenmp', '-march=native'],
              extra_link_args=['-lomp'],
              language='c'),

    Extension('xwp_cython.prop2d_4loop',
              sources=['xwp_cython/prop2d_4loop.pyx'],
              extra_compile_args=['-O3', '-fopenmp', '-march=native'],
              extra_link_args=['-lomp'],
              language='c')
]

if __name__ == "__main__":
    setup(
        name='xwp_cython',
        packages=[
            'xwp_cython',
        ],
        cmdclass={'build_ext': new_build_ext},
        ext_modules=(ext_modules),
        include_dirs=[np.get_include()],
        description='X-ray wave propagation techniques in cython',
        url='https://github.com/s-sajid-ali/xwp_cython',
        author='Sajid Ali',
        author_email='sajidsyed2021@u.northwestern.edu',
        zip_safe=False
    )
