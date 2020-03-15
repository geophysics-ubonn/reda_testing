#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import numpy as np

import reda

basepath = os.path.dirname(__file__) + os.sep


def test_load_one_dataset():
    seit = reda.sEIT()
    seit.import_crtomo(
        directory=basepath + 'data/modV_00_noisy/', timestep=0
    )

    group_frequencies = seit.data.groupby('frequency')
    # nr of frequencies
    assert len(group_frequencies.groups.keys()) == 15
    # nr of data points
    assert np.all(group_frequencies['r'].count() == 1406)
    assert 'timestep' in seit.data.columns
    assert np.all(seit.data['timestep'] == 0)

def test_load_four_datasets():
    seit = reda.sEIT()
    for nr in range(0, 4):
        seit.import_crtomo(
            directory=basepath + 'data/modV_0{}_noisy/'.format(nr), timestep=nr
        )
    assert 'timestep' in seit.data.columns
    group_timesteps = seit.data.groupby('timestep')
    assert len(group_timesteps.groups.keys()) == 4
    assert tuple(group_timesteps.groups.keys()) == (0, 1, 2, 3)

    group_frequencies = seit.data.groupby('frequency')
    # nr of frequencies
    assert len(group_frequencies.groups.keys()) == 15
    # nr of data points
    for ts, item_ts in group_timesteps:
        g_ts_f = item_ts.groupby('frequency')
        assert np.all(g_ts_f['r'].count() == 1406)
