import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="darshellclock",
    version="0.0.2",
    python_requires='>=3.6.0',
    author="Adrien Rebuzzi",
    author_email="darokin42@gmail.com",
    description="Terminal ASCII clock",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/darokin/darshellclock",
    #packages=setuptools.find_packages(),
    packages=['darshellclock'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'darshellclock = darshellclock.__main__:main'
        ]
    },
    install_requires=[
        'windows-curses >= 2.0;platform_system=="Windows"'
    ]
)
