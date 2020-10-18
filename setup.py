import setuptools

with open('README.md', 'r') as fp:
    long_description = fp.read()

PACKAGE_NAME = "pyipextract"
PACKAGE_DIR = "src"

setuptools.setup(
    name=PACKAGE_NAME,
    version="1.0.2",
    author="c0d3monk",
    author_email="akr.optimus@gmail.com",
    description="A Python utility to validate or extract IPv4 addresses from strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/c0d3monk/pyipextract",
    packages=[PACKAGE_NAME],
    package_dir={PACKAGE_NAME: PACKAGE_DIR},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license='Apache License 2.0',
)
