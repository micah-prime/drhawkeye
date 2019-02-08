from inicheck.checkers import GenericCheck
import netCDF4 as nc
import os
import glob
from collections import OrderedDict

class MissingVarCheck(GenericCheck):
    def __init__(self, **kwargs):
        super(MissingVarCheck, self).__init__(**kwargs)

    def cast(self):
        return self.value

    def is_valid(self):
        # path to file with pattern
        pattern = self.config.cfg['output_check']['pattern']
        file = self.config.cfg['output_check']['file']
        pf = os.path.join(pattern, file)
        d_fp = sorted(glob.glob(pf), key=os.path.getmtime)
        d_fp.sort(key=lambda f: os.path.splitext(f))
        print('here')
        # empty dictionary
        self.incomplete = OrderedDict()

        for idd, d in enumerate(d_fp):
            # read in the netcdf and get variables
            ds = nc.Dataset(d, 'r')
            keys = ds.variables.keys()
            ds.close()

            # checks keys against list of vars
            mv = [v for v in self.config.cfg['output_check']['netcdf_vars'] if v not in keys]
            if len(mv) > 0:
                self.incomplete[d] = mv

        if len(self.incomplete) > 0:
            self.message=('Variables missing from netcdfs.\n{}'.format('\n'.join(self.incomplete)))
            return False, self.message
        else:
            return True, self.message
