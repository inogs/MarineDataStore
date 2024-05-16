import argparse
from attr import dataclass
def argument():
    parser = argparse.ArgumentParser(description = '''
    Writes out/ files which names like sal_Lid_NRT.csv
    for every station defined inside the script.
    Looks for salinity and temperature in NRT and Reanalysis Copernicus datasets. 

    ''', formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(   '--outdir', '-o',
                                type = str,
                                default = None,
                                required = True,
                                help = "")
    parser.add_argument(   '--start_time', '-s',
                                type = str,
                                required = True,
                                help = "Date in yyyymmdd format")
    parser.add_argument(   '--end_time', '-e',
                                type = str,
                                required = True,
                                help = "Date in yyyymmdd format")       

    return parser.parse_args()

args = argument()



import copernicusmarine
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass
OUTDIR=Path(args.outdir)
start_time=datetime.strptime(args.start_time,"%Y%m%d")
end_time  =datetime.strptime(args.end_time,  "%Y%m%d")

@dataclass
class Station():
    name:str
    lon:float
    lat:float
    shortname:str
@dataclass
class copernicus_dataset():
        name:str
        MDSdataset:str
        MDSvar:str
        shortvar:str

Dataset_1=copernicus_dataset('NRT','cmems_mod_med_phy-sal_anfc_4.2km_P1D-m','so','sal')
Dataset_2=copernicus_dataset('NRT','cmems_mod_med_phy-tem_anfc_4.2km_P1D-m','thetao','tem')
Dataset_3=copernicus_dataset('REA','med-cmcc-sal-rean-d','so','sal')
Dataset_4=copernicus_dataset('REA','med-cmcc-tem-rean-d','thetao','tem')



Station1= Station('Malamocco', 12.497011, 45.300803, 'Mal')
Station2= Station('Lido',      12.592576, 45.424574, 'Lid')
Station3= Station('Chioggia',  12.475925, 45.179738, 'Chio')

DATASET_LIST=[Dataset_1,Dataset_2, Dataset_3, Dataset_4]
STATION_LIST=[ Station1 , Station2, Station3]

for dataset in DATASET_LIST:
    for station in STATION_LIST:
        filename="%s_%s_%s.csv" %(dataset.shortvar, station.shortname, dataset.name)
        outfile=OUTDIR / filename
        print(outfile)
        model_dataset = copernicusmarine.open_dataset(
            dataset_id = dataset.MDSdataset,
            minimum_longitude = station.lon,
            maximum_longitude = station.lon,
            minimum_latitude = station.lat,
            maximum_latitude = station.lat,
            minimum_depth=0,
            maximum_depth=0,
            start_datetime=start_time,
            end_datetime  =end_time,
            variables = [dataset.MDSvar]
        )
    
        DatetimeList=[ datetime.utcfromtimestamp(int(t)*1.e-9)  for t in model_dataset.time ]
        A=model_dataset[dataset.MDSvar][:,0,0,0].to_numpy()
        nTimes=len(A)
        
        dateformat="%Y-%m-%d::%H:%M:%S"
        f=open(outfile,'wt')
        for i in range(nTimes):
            string="%s\t%g\n" %( DatetimeList[i].strftime(dateformat), A[i]  )
            f.write(string)
        f.close()

