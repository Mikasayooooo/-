import pytest


def test_raw_report(testdir):
    """Make sure that our plugin works."""
    # create a temporary pytest test file
    testdir.makepyfile(
        """
        def test_01():
            a = "hello"
            b = "hello"
            assert a == b

        def test_02():
            a = "hello"
            b = "hello world"
            assert a == b
         """
            )

    # run all tests with pytest
    result = testdir.runpytest()

    # check that 1 test passed, 1 test failed.
    result.assert_outcomes(passed=1, failed=1)
    result.stdout.fnmatch_lines(["*.F*", ])

def test_change_on_report(testdir):
    """Make sure that our plugin works."""
    # create a temporary pytest test file
    testdir.makepyfile(
        """
        def test_01():
            a = "hello"
            b = "hello"
            assert a == b

        def test_02():
            a = "hello"
            b = "hello world"
            assert a == b
         """
            )

    # run all tests with pytest
    result = testdir.runpytest("--change", "on")

    # check that 1 test passed, 1 test failed.
    result.stdout.fnmatch_lines(['*√x*', ])


def test_change_off_report(testdir):
    """Make sure that our plugin works."""
    # create a temporary pytest test file
    testdir.makepyfile(
        """
        def test_01():
            a = "hello"
            b = "hello"
            assert a == b

        def test_02():
            a = "hello"
            b = "hello world"
            assert a == b
         """
            )

    # run all tests with pytest
    result = testdir.runpytest("--change", "off")

    # check that 1 test passed, 1 test failed.
    result.stdout.fnmatch_lines(['*.F*', ])


def test_change_default_report(testdir):
    """Make sure that our plugin works."""
    # create a temporary pytest test file
    testdir.makepyfile(
        """
        def test_01():
            a = "hello"
            b = "hello"
            assert a == b

        def test_02():
            a = "hello"
            b = "hello world"
            assert a == b
         """
            )

    # run all tests with pytest
    result = testdir.runpytest("--change")

    # check stderr pytest: error: argument --change: expected one argument
    result.stderr.fnmatch_lines(['*argument --change: expected one argument*', ])


def test_verbose_report(testdir):
    """Make sure that our plugin works."""
    # create a temporary pytest test file
    testdir.makepyfile(
        """
        def test_01():
            a = "hello"
            b = "hello"
            assert a == b

        def test_02():
            a = "hello"
            b = "hello world"
            assert a == b
         """
            )

    # run all tests with pytest
    result = testdir.runpytest("-v")

    # check that 1 test passed, 1 test failed.
    result.stdout.fnmatch_lines(['*::test_01 PASSED*', '*::test_02 FAILED*'])



def test_change_verbose_report(testdir):
    """Make sure that our plugin works."""
    # create a temporary pytest test file
    testdir.makepyfile(
        """
        def test_01():
            a = "hello"
            b = "hello"
            assert a == b

        def test_02():
            a = "hello"
            b = "hello world"
            assert a == b
         """
            )

    # run all tests with pytest
    result = testdir.runpytest("--change", "on", "-v")

    # check that 1 test passed, 1 test failed.
    result.stdout.fnmatch_lines(['*::test_01 passed*', '*::test_02 failed*'])


def test_help(testdir):
    """Make sure that our plugin works."""
    # create a temporary pytest test file
    testdir.makepyfile(
        """
        def test_01():
            a = "hello"
            b = "hello"
            assert a == b
         """
            )

    # run all tests with pytest
    result = testdir.runpytest("--help")

    # check --help
    result.stdout.fnmatch_lines(["*--change=*", ])