#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import reda

basepath = os.path.dirname(__file__) + os.sep


def test_loading_normal():
    seit = reda.sEIT()
    seit.import_mpt_das1(basepath + 'SIP3.Data')
