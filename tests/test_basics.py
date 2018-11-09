#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from docnado import docnado
from pytest_testdirectory import testdirectory

"""Tests for `docnado` package."""


class TestRunDocnadoWithArguments():

    def test_Docnado_new(self, testdirectory):
        """
        User passes new
        """
        output = testdirectory.run('docnado --new')
        assert output.returncode == 0
        assert testdirectory.contains_dir('docs')
        assert testdirectory.contains_dir('style')
        assert testdirectory.contains_file('logo.png')

    def test_Docnado_help(self, testdirectory):
        """
        User passes help
        """
        output = testdirectory.run('docnado --help')
        assert output.stdout.match('*show this help message and exit*')
        assert output.returncode == 0
