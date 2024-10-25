from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='gpColor',
    version='1.0.0',
    description='A Python module to apply ANSI, RGB and HEX colors in terminal output.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Grandpa EJ',
    author_email='aizoro690@gmail.com',
    url='https://github.com/gpbot-org/gpColor',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # :) don't need
    ],
)
