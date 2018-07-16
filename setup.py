try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from codecs import open

setup(
    name="cfman",
    description="Like man pages, but for HTTP status codes",
    version="v1.0.3",
    install_requires=["pyyaml", "urwid"],
    packages=["cfman"],
    entry_points={"console_scripts": ["cfman = cfman.cfman:main"]},
    include_package_data=True,
    python_requires=">=3",
    url="https://github.com/shobrook/cfman",
    author="shobrook",
    author_email="shobrookj@gmail.com",
    license="MIT"
)
