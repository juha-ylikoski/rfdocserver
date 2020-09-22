import setuptools
from rfdocserver._version import __version__
with open("readme.md", "r") as fh:
    long_description = fh.read()


with open("requirements.txt", "r") as f:
    requirements = f.read().split("\n")

setuptools.setup(
    name="rfdocserver",
    version=__version__,
    author="Juha Ylikoski",
    author_email="juha.ylikoski14@outlook.com",
    description="Web server for hosting robot framework documentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/juha-ylikoski/rfdocserver",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Framework :: Flask"
    ],
    python_requires='>=3.6',
)
