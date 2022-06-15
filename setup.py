from setuptools import find_packages, setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="IndianPinCodes",
    version="0.0.2",
    author="Lpcodes",
    description="A package for fetching details for the pincode provided",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LpCodes/Pincode-Details",
    project_urls={
        "Bug Tracker": "https://github.com/LpCodes/Pincode-Details/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",)
