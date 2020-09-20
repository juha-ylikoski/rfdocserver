import setuptools
from rf_doc_server._version import __version__
with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="juha-ylikoski",
    version=__version__,
    author="Juha Ylikoski",
    author_email="juha.ylikoski14@outlook.com",
    description="Web server for hosting robot framework documentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/juha-ylikoski/rf-doc-server",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GPL-3.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
