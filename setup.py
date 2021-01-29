import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="darshell-clock",
    version="0.0.1",
	python_requires='>=3.6.0',
    author="Adrien Rebuzzi",
    author_email="darokin42@gmail.com",
    description="Terminal ASCII clock",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/darokin/darshell-clock",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)