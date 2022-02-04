import os
from setuptools import find_packages, setup

def read_requirements(file_name):
    try:
        with open(os.path.join(os.path.dirname(__file__), file_name)) as _file:
            return _file.read().splitlines()
    except IOError as e:
        return []

setup(
    name='internalip',
    version='1.0.0',
    license='BSD',
    maintainer='Rafael Cirolini',
    maintainer_email='lcrafael@gmail.com',
    description='API aplication for check and list internal ips.',
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=read_requirements('requirements.txt'),
    tests_require=read_requirements('requirements-dev.txt')
)
