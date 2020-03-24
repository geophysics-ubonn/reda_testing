#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import reda

basepath = os.path.dirname(__file__) + os.sep


def test_loading_normal():
    cr = reda.CR()
    cr.import_mpt(basepath + 'FD.Data')
