#!/usr/bin/env python
import pytest
import os
import reda

basepath = os.path.dirname(__file__) + os.sep


@pytest.fixture(scope='class')
def loader(request):
    filenames = request.cls.filenames
    ert = reda.ERT()
    ert.import_syscal_txt(basepath + filenames[0])
    if len(filenames) == 2:
        nr_electrodes = request.cls.nr_electrodes
        ert.import_syscal_txt(
            basepath + filenames[1], reciprocals=nr_electrodes)
    request.cls.ert = ert
    yield


@pytest.mark.usefixtures("loader")
class TestClass(object):
    filenames = ['01_txt/data_nor.txt', '01_txt/data_rec.txt']
    nr_electrodes = 48

    def test_data_properties(self):
        assert self.ert.data.shape[0] == 990 * 2
        assert self.ert.has_multiple_timesteps() is False

    def test_histogram(self):
        self.ert.histogram()

    def test_pseudosection(self):
        self.ert.pseudosection()


@pytest.mark.usefixtures("loader")
class TestClass1(object):
    filenames = ['01_txt/data_nor.txt', ]

    def test_data_properties(self):
        assert self.ert.data.shape[0] == 990
        assert self.ert.has_multiple_timesteps() is False
