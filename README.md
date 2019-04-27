# REDA -- Data testing repository

This repository contains test data for all devices that can be imported. The
repository is separated from the main code to reduce the directory size.

## Usage

To run all tests, in the root directory (containing the README.md file), run::

	pytest

In order to run subsets of the tests, run **pytest** in the corresponding
subdirectory.

## Creating new tests

This is still in flux, see the Syscal tests for the most up-to-date tests.

Tests can be run in grouping directories (i.e., directories that do not contain
test data, but group data sets in multiple subdirectories). This is useful to
apply certain tests to all data sets, and at this moment should be the
preferred way to write tests.

**However, at this point we still need to properly document this test approach,
and until then specific tests can be written in each test directory:**

Use a unique filename for the test script, starting with **test_**.

To prevent problems with file paths, use the following boilerplate code for
individual tests: ::

	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	import os

	import reda

	basepath = os.path.dirname(__file__) + os.sep


	def test_loading_normal():
		ert = reda.ERT()
		ert.import_syscal_bin(basepath + 'data_normal.bin')

## Checklist for new data sets

Each data set included in the repository should be tested with respect to the
following properties/functionality:

* import into reda
* check expected number of data points
* plot relevant histograms
* (if applicable) plot relevant pseudosections

