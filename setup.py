import os
from setuptools import setup

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cateye",
    version = "0.0.2",

    author = "Dirk Gütlin",
    author_email = "dirk.guetlin@gmail.com",
    description = ("Uniform Categorization of Eyetracking in Python."),
    license = "BSD",
    keywords = "Eyetracking classification",
    url = "https://github.com/DiGyt/CatEye",
    packages=['cateye'],
    include_package_data=True,
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
        "numpy>=1.14",
        "scipy",
        "remodnav",
        "nslr @ git+https://github.com/pupil-labs/nslr",
        "nslr_hmm @ git+https://github.com/pupil-labs/nslr-hmm",
    ],
)
