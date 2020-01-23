import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-base-shop",
    version="0.0.13",
    author="Blake Lockley",
    author_email="bwlockley@gmail.com",
    description="A basic, extendable data model for ecommerce shops using Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blakelockley/django-base-shop",
    packages=setuptools.find_packages(exclude=["test"]),
    install_requires=["django >= 2.1", "pillow == 7.0.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6.5",
)
