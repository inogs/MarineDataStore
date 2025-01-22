import argparse
def argument():
    parser = argparse.ArgumentParser(description = '''
    extract time series of a copernicus product variable
    ''', formatter_class=argparse.RawTextHelpFormatter)


    parser.add_argument(   '--datestart','-s',
                                type = str,
                                required = True,
                                help = '''date in yyyymmdd format''')
    parser.add_argument(   '--dateend','-e',
                                type = str,
                                required = True,
                                help = '''date in yyyymmdd format ''')
    parser.add_argument(   '--outdir','-o',
                                type = str,
                                required = True,
                                help = 'path for the output')
    parser.add_argument(   '--longitude','-n',
                                type = str,
                                required = True,
                                help = '''longitude of the point''')
    parser.add_argument(   '--latitude','-t',
                                type = str,
                                required = True,
                                help = '''latitude of the point''')
    parser.add_argument(   '--depth','-d',
                                type = str,
                                required = True,
                                help = '''depth''')
    parser.add_argument(   '--dataset','-p',
                                type = str,
                                required = True,
                                help = '''name of the copernicus marine dataset, 
                                          e.g. cmems_mod_med_phy-sal_anfc_4.2km_P1D-m''')
    parser.add_argument(   '--variable','-v',
                                type = str,
                                required = True,
                                help = '''name of the variable''')
    return parser.parse_args()

args = argument()


print('importing copernicus..')
import copernicusmarine
print('.. done')
import numpy as np
import pylab as pl
from datetime import datetime, timedelta
from bitsea.commons import netcdf4


longitude = float(args.longitude)
latitude = float(args.latitude)
depth = float(args.depth)

datestart = datetime.strptime(args.datestart,'%Y%m%d')
date__end = datetime.strptime(args.dateend,  '%Y%m%d')

dataset = args.dataset
variable = args.variable


A= copernicusmarine.subset(dataset_id=dataset,
                        start_datetime=datestart.strftime('%Y-%m-%d'),
                        end_datetime=date__end.strftime('%Y-%m-%d'),
                        minimum_longitude=longitude,
                        maximum_longitude=longitude,
                        minimum_latitude=latitude,
                        maximum_latitude=latitude,
                        minimum_depth=depth,
                        maximum_depth=depth,
                        force_download=True,
                        variables=[variable])


#M2d           = netcdf4.readfile(A.name, variable)[:,0,0]               
#times_days = netcdf4.readfile(A.name, 'time') # days - Here we can have a warning
#Dref = datetime(1900,1,1,0,0,0)

#TIMELIST= [Dref + timedelta(days=s) for s in times_days.astype(np.float64) ]

#fig,ax=pl.subplots()

#ax.plot(TIMELIST, M2d[:,0])
#ax.grid()
#fig.show()


