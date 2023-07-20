======================
Cookiecutter PyProject
======================

Cookiecutter_ template for a Python package.

Features
--------

* Testing setup with ``unittest`` and ``python setup.py test`` or ``pytest``
* bump2version_: Pre-configured version bumping with a single command
* Command line interface using Typer

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter http://gitlab.dokku2.woosterbrush.com/zachmyers/cookiecutter-python-package.git

Then:

* Create a repo and put it there.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Add a `requirements.txt` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.

.. _bump2version: https://github.com/c4urself/bump2version
.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
