from setuptools import setup, find_packages

setup(
    name='termatplotlib',
    version='0.1.0',
    packages=find_packages(),
    author='RK RIAD & RK STUDIO 585',
    author_email='rkstudio585@github.com',
    description='A lightweight and elegant Python library for rendering stunning ASCII plots directly in your terminal. Visualize your data with beautiful scatter, line, and bar charts, bringing the power of matplotlib to your command line.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rkstudio585/termatplotlib',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
