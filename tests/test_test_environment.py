#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from pytest_testdirectory import testdirectory

"""Tests environment to make sure the test setup works"""

class TestTestenvironment():

    def test_run(self, testdirectory):

        testdirectory.run(['python', '--version'])

        testdirectory.run(['python', '--version'], stdout=None, stderr=None)

        r = testdirectory.run('python --version')
        assert r.returncode == 0
        assert r.stdout.match('Python *') or r.stderr.match('Python *')

    def test_print_path_to_tests_directory(self, capsys):
        with capsys.disabled():
            print(sys.path[0])

    def test_Docnado_is_executable(self, testdirectory):
        """
        User passes no args, should fail with SystemExit
        """
        output = testdirectory.run('docnado --help')
        assert output.returncode == 0