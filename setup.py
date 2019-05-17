from setuptools import setup, find_packages

print(find_packages())

setup(
    name='eigengdb',
    version='1.0',
    packages=find_packages(),
    install_requires=['numpy'],
    author="David Millard",
    author_email="dmillard@usc.edu",
    description='GDB pretty printers for eigen types',
    license="MPL2",
    keywords="eigen gdb",
    url="https://github.com/dmillard/eigengdb",
    project_urls={
        "Source Code": "https://github.com/dmillard/eigengdb",
        "Bug Tracker": "https://github.com/dmillard/eigengdb/issues",
    })
