from setuptools import setup, Extension

setup(
    #...
    ext_modules=[Extension('library', ['library.cpp'],),],
)