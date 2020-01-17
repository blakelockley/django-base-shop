# Base Shop

Base Shop is a lightweight Django app that provides an extendable data model to be used in online shops.

> Base Shop is currently in early stages of development and is likely to radically change without notice.

As online shops have many differing needs and requirements a single data model does not offer a sound solution. The philosophy of _Base Shop_ is to provide a solid infrastructure that can extended for the needs of any online shop using Django.

Base Shop provides a collection of "base" models that are intended to be extended by end users of the package, or used as is. The primary models provided include "BaseProduct", "BaseOrder", "BaseCheckoutDetails" along with more concrete models designed to interact seamlessly with user extended versions of the previously mentioned models.

## Package

```
pipenv run python setup.py sdist bdist_wheel
pipenv run python -m twine upload dist/*
```
