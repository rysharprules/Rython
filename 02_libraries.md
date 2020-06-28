# Libraries and the Flask web framework

- [Libraries and the Flask web framework](#libraries-and-the-flask-web-framework)
  - [Packages](#packages)

## Packages

The most popular tool for installing Python packages is [**pip**](https://pip.pypa.io/en/stable/),
which is included with all modern versions of Python. It provides
the core features for finding, downloading, and installing
packages from the [Python Package Index](https://pypi.org/) (**PyPI**) and other
Python package repositories, and is designed to be used from
the command line / terminal.

It's pretty simple to install a package using pip:

`pip install some-package-name`

This will install the latest version of the package (assuming it
exists on PyPI). You can specify an exact version when installing a package, for
example:

`pip install some-package-name==1.4`

Other version specifiers can be found here: https://www.python.org/dev/peps/pep-0440#versionspecifiers

You can install multiple packages with a [requirements.txt](https://pip.pypa.io/en/stable/user_guide/#requirements-files) file:

`pip install -r requirements.txt`