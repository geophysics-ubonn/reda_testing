#!/usr/bin/env python
import reda
ert1 = reda.ERT()
ert1.import_syscal_bin(
    'data.bin',
    check_meas_nums=False,
)
print(ert1.electrode_positions)

ert2 = reda.ERT()
ert2.import_syscal_bin(
    'data.bin',
    check_meas_nums=False,
    elecs_transform_reg_spacing_x=(1, 2.5),
)
print(ert2.electrode_positions)

ert3 = reda.ERT()
ert3.import_syscal_bin(
    'data.bin',
    check_meas_nums=False,
    assume_regular_electrodes_x=(48, 1.0),
    # elecs_transform_reg_spacing_x=(1, 2.5),
)
print(ert3.electrode_positions)

ert_rec = reda.ERT()
ert_rec.import_syscal_bin(
    'data.bin',
    check_meas_nums=False,
    assume_regular_electrodes_x=(48, 1.0),
    elecs_transform_reg_spacing_x=(1, 2.5),
    reciprocals=48,
)
print(ert_rec.electrode_positions)
