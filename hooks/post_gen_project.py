#!/usr/bin/env python
import os
import shutil
import pathlib

PROJECT_DIRECTORY = pathlib.Path(os.path.realpath(os.path.curdir))


def remove_file(filepath):
    filepath = PROJECT_DIRECTORY / filepath
    os.remove(filepath)


def remove_folder(filepath):
    filepath = PROJECT_DIRECTORY / filepath
    shutil.rmtree(filepath)

if __name__ == '__main__':

    if '{{ cookiecutter.add_sqlalchemy_dependencies }}' != 'y':
        remove_folder(pathlib.Path('dependencies'))

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file(pathlib.Path('AUTHORS.rst'))
        remove_file(pathlib.Path('docs/authors.rst'))

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file(pathlib.Path('LICENSE'))
