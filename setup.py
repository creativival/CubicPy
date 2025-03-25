from setuptools import setup, find_packages
from cubicpy import __version__

setup(
    name="cubicpy",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "cubicpy": ["models/*.egg", "examples/*.py"],
    },
    install_requires=[
        "panda3d>=1.10.15",
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "cubicpy=cubicpy.cli:main",
        ],
    },
    author="creativival",
    description="A Python library for creating 3D basic shape models and animations with Physics.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/creativival/CubicPy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Education",
        "Topic :: Education :: Computer Aided Instruction (CAI)",
    ],
    python_requires=">=3.9",
)