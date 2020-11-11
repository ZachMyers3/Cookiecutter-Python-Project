#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{% else %}
import unittest
{%- endif %}
import typer
from typer.testing import CliRunner

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}

{%- if cookiecutter.use_pytest == 'y' %}

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI"""
    app = typer.Typer()
    # the function that typer is running
    # is also called command
    app.command()(command)

    runner = CliRunner()
    result = runner.invoke(app, [])
    assert result.exit_code == 0
{%- endif %}
