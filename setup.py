import setuptools
import os

here = os.path.dirname(os.path.abspath(__file__))

long_description = (here / 'README.md').read_text(encoding='utf-8')

setuptools.setup(
    name="testreverseautoslitcode",
    version="0.1.34",
    author="Jessica Sullivan",
    author_email="jsulli27@nd.edu",
    description="Test Compiling of Code",
    long_description =  long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/jsulli27/LRIS-X-Y-to-WCS",
    project_urls={
        "Bug Tracker": "https://github.com/jsulli27/LRIS-X-Y-to-WCS/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "testreverseautoslitcode"},
    packages=setuptools.find_packages(where="testreverseautoslitcode"),
    install_requires=[
    "python = ^3.7",
    "astropy = ^4.3.post1",
    "matplotlib = ^3.4.2",
    "panstamps = ^0.6.1",
    "pytest-shutil = ^1.7.0",
    "numpy = ^1.21.1",
    "astroquery = ^0.4.3",
    "regions = ^0.5",
    "PyQt5",
    "shapely",
    ],
    python_requires=">=3.6",
)
