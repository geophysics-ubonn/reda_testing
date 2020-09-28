#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import reda

basepath = os.path.dirname(__file__) + os.sep


def test_load_mat():
    sip = reda.SIP()
    sip.import_sip04(basepath + '20200916_1K_schlossA.mat')


def test_load_csv():
    sip2 = reda.SIP()
    sip2.import_sip04(basepath + '20200916_1K_schlossA.csv')
