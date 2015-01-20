#!/usr/bin/env python

# Run doctests in docgen source code.

# Imports {{{1
from __future__ import print_function
from runtests import cmdLineOpts, writeSummary
from textcolors import Colors
import doctest
import sys

# Initialization {{{1
fast, printSummary, printTests, printResults, colorize, parent = cmdLineOpts()

colors = Colors(colorize)
succeed = colors.colorizer('green')
fail = colors.colorizer('red')
error = colors.colorizer('red')
info = colors.colorizer('magenta')
status = colors.colorizer('cyan')


# Test cases {{{1
testcases = ["scripts.py", "README.rst"]


# Run tests {{{1
totalTests = totalFailures = 0
for test in testcases:
    if printTests:
        print(status('Trying:'), test)

    failures, testsRun = doctest.testfile(test)
    totalTests += testsRun
    totalFailures += failures
    if failures:
        print(fail('%s: %d failures in %d tests.' % (test, failures, testsRun)))
    elif printResults:
        print(succeed('%s: all %d tests succeed.') % (test, testsRun))

if printSummary:
    print('%s: %s tests run, %s failures detected.' % (
        fail('FAIL') if failures else succeed('PASS'),
        totalTests, totalFailures
    ))

writeSummary(testsRun, failures)
exit(failures != 0)
