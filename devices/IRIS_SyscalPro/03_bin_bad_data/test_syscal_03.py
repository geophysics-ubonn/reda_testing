#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import reda

basepath = os.path.dirname(__file__) + os.sep


def test_loading_normal():
    ert = reda.ERT()
    ert.import_syscal_bin(basepath + 'data_normal.bin')
    # this is an old measurement, accidently downloaded from the Syscal
    assert ert.data.shape[0] == 1

    ert2 = reda.ERT()
    ert2.import_syscal_bin(basepath + 'data_normal.bin', skip_rows=1)
    # real data
    assert ert2.data.shape[0] == 325

def test_loading_reciprocal():
    ert = reda.ERT()
    ert.import_syscal_bin(
        basepath + 'data_reciprocal.bin',
        reciprocals=48,
    )
