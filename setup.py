"""
Witcher

This gives use an image of geralt in a specified mood in binary.
"""
from distutils.core import setup

__version__ = "0.0.1"


def install_requires():
    with open('requirements.pip', 'r') as f:
        return f.readlines()


setup(
    author="Glenbotz",
    author_email="glen@something.com",
    description="A witcher tool",
    long_description=__doc__,
    fullname="witcher",
    name="witcher",
    url="https://github.com/glenbot/witcher",
    version=__version__,
    platforms=["Linux"],
    packages=[
        "witcher",
        "witcher.bin"
    ],
    install_requires=install_requires(),
    entry_points={
        'console_scripts': [
            "witcher=witcher.bin.cli:main"
        ]
    }
)
