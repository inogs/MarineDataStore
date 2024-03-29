import copernicusmarine
from commons import netcdf4
import pylab as pl
import numpy as np
from datetime import datetime, timedelta


lon=13.62 #12.5082483
lat=45.728# 45.3142467


A= copernicusmarine.subset(dataset_id="cmems_mod_med_phy-sal_anfc_4.2km_P1D-m",
                        start_datetime="2023-01-01",
                        end_datetime="2024-02-22",                   
                        minimum_longitude=lon,
                        maximum_longitude=lon,
                        minimum_latitude=lat,
                        maximum_latitude=lat,
                        minimum_depth=0,
                        maximum_depth=40,
                        force_download=True,
                        variables=["so"])


M2d           = netcdf4.readfile(A.name, "so")[:,:,0,0]               
times_minutes = netcdf4.readfile(A.name, 'time') # minutes - Here we can have a warning
Dref = datetime(1900,1,1,0,0,0)

TIMELIST= [Dref + timedelta(seconds=s*60) for s in times_minutes.astype(np.float64) ]

fig,ax=pl.subplots()

ax.plot(TIMELIST, M2d[:,0])
ax.grid()
fig.show()
