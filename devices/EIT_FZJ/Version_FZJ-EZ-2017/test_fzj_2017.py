#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import reda

basepath = os.path.dirname(__file__) + os.sep


def test_loading_normal():
    seit = reda.sEIT()
    seit.import_eit_fzj(
        basepath + 'eit_data_mnu0.mat',
        basepath + 'configs_large_dipoles_norrec.dat',
    )
