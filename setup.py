from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import platform

try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    import setuptools

py_version = platform.python_version_tuple()
if py_version < ('2', '7') or py_version[0] == '3' and py_version < ('3', '4'):
    raise RuntimeError('Python version 2.7 or 3.5+ is required.')


setuptools.setup(
        name='tensorflow_serving_api',
        version='1.3',
        packages=setuptools.find_packages(exclude=[
            '*.tests', '*.tests.*', 'tests.*', 'tests',
        ]),
        install_requires=[
            'six',
            'protobuf',
            'grpcio',
            'tensorflow=1.3'
        ],
        license='Apache 2.0',
        classifiers=[
        ],
)