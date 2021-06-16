#!/usr/bin/env python
import reda

# seit = reda.sEIT()
# seit.import_eit_fzj(
#     'eit_data_mnu0.mat',
#     'configs.dat',
# )
import reda.importers.eit_fzj as eit_fzj

adc = eit_fzj.get_adc_data('eit_data_mnu0.mat')
emd, md, emd_3p = eit_fzj.get_mnu0_data('eit_data_mnu0.mat', 'configs.dat', return_3p=True)
