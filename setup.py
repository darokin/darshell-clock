import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="darshellclock",
    version="0.0.1",
	python_requires='>=3.6.0',
    author="Adrien Rebuzzi",
    author_email="darokin42@gmail.com",
    description="Terminal ASCII clock",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/darokin/darshellclock",
    packages=setuptools.find_packages(),
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
    ],
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/darokin/darshellclock',
    },
)