# {{ cookiecutter.project_name }}

## Description

{{ cookiecutter.project_short_description }}

## Features

* TODO

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and [this](http://gitlab.woosterbrush.com/zachmyers/cookiecutter-python-package) project template.

## Running Development Application

```bash
# install dependencies
$ poetry install
# run cli with script
$ poetry run cli --help
# run application cli interface without script
$ poetry run python {{ cookiecutter.project_slug }}/cli.py --help
```

## Running Tests Using Pytest

```bash
# install dependencies (if needed)
$ poetry install
# run pytest through poetry
$ poetry run pytest
```

## Building CLI Executable

```bash
# run build script, pyinstaller is required
$ ./scripts/build.ps1
```

An executable should then be available at ```./dist/{{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}.exe```

## Publishing Package to Local PyPi

```bash
# add the local pypi repository to poetry
$ poetry config repositories.wbc http://pypi.dokku2.woosterbrush.com/
# build the wheels for publishing
$ poetry build
# publish to pypi specifying our new repository
$ poetry publish -r wbc
```

You can verify the list of packages after deployment [here](http://pypi.dokku2.woosterbrush.com/packages/).
