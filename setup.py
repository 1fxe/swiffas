from setuptools import setup

setup(name='swiffas',
      version='0.1',
      description='SWF parser and AVM2 (Actionscript 3) bytecode parser',
      url='https://github.com/1fxe/swiffas',
      author='Alex Hixon',
      author_email='alex@alexhixon.com',
      license='MIT',
      packages=['swiffas'],
      install_requires=[
      	'bitstring'
      ],
      zip_safe=False)
