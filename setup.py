import setuptools
from pkg_resources import resource_string

setuptools.setup(
    name="mechaSVG",
    version="0.0.8",
    author="Ricardo Almir Angnes",
    author_email="ricardo_almir@hotmail.com",
    description="mechaSVG is a python & tk application for creating good-looking energy profile diagrams as Scalable Vector Graphics.",
    long_description=resource_string(__name__,"mechasvg\supl\README.txt"),
	license="MIT",
    url="https://github.com/ricalmang/mechaSVG",
	keywords = ['chemistry'],
	install_requires = ["openpyxl"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)