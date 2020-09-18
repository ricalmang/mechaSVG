import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mechaSVG",
    version="0.0.5",
    author="Ricardo Almir Angnes",
    author_email="ricardo_almir@hotmail.com",
    description="mechaSVG is a python & tk application for creating good-looking energy profile diagrams as Scalable Vector Graphics.",
    long_description=long_description,
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