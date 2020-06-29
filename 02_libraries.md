# Libraries and the Flask web framework

- [Libraries and the Flask web framework](#libraries-and-the-flask-web-framework)
  - [Packages](#packages)
    - [Virtual Environments](#virtual-environments)
      - [Creating a virtual enviroment](#creating-a-virtual-enviroment)

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

### Virtual Environments

By default, all Python packages are installed in a common location on your machine. However, this can lead to problems when working on multiple projects that require different versions of the same package.

The [**Python virtual environment**](https://docs.python.org/3/tutorial/venv.html) is a self-contained
directory within the project directory that contains a dedicated Python installation for a particular version of Python, plus any packages needed by that project. Different projects can have their own virtual environments with the specific versions of the packages they need, and each virtual environment is isolated
from the others, so there are no conflicts.

#### Creating a virtual enviroment

`python -m venv env`

This will create a virtual environment in a subdirectory called env. You then need to tell your terminal to
use that environment for this project by activating the environment. On Windows machines, you do this
using the following command:

`env\Scripts\activate.bat`

On Linux or macOS, run:

`env/bin/activate`