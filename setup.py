from setuptools import setup

setup(
    name='tirt',
    version='0.0.3',
    packages=['tirt'],
    url='https://github.com/inuyasha2012/tirt',
    license='MIT',
    author='inuyasha2012',
    author_email='inuyasha021@163.com',
    description='the simulation of Thurstone Item Response Theory, include fixed forced test and adaptive forced test. ',
    long_description=open('doc/index.rst').read(),
    install_requires=['numpy', 'scipy'],
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ]
)