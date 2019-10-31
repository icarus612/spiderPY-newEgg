from setuptools import setup

setup(name='Maze Runner',
      version='0.1',
      description='Builds mazes and solves them, or any maze you give it.',
      url='http://github.com/icarus612/mazeRunner-PY',
      author='Icarus612',
      author_email='ellishogan95@gmail.com',
      license='MIT',
      install_requires=[
          'json',
          'sys',
          'bs4',
          'requests'
      ],
      zip_safe=False)