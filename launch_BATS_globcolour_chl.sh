
# Download OC chl (globcolour) from Copernicus Marine at BATS station
# https://www.st.nmfs.noaa.gov/copepod/time-series/us-10102/#:~:text=The%20Bermuda%20Atlantic%20Time%2Dseries,of%20Ocean%20Sciences%20(BIOS).

LON=-64.5000
LAT=32.1667

START=20000101
END=20231231

DEPTH=0

#{origin}_{group}-{pc}_{area}_{thematic}-{variable}_{type}_{level}-{sensor}-{spatial resolution}_{temporal resolution}
DATASET=cmems_obs-oc_glo_bgc-plankton_my_l3-multi-4km_P1D
VARIABLE=CHL

OUTDIR=$PWD
mkdir -p $OUTDIR
rm $OUTDIR/cmems*nc

python extract_singlepoint_variable.py -s $START -e $END -o $OUTDIR -n $LON -t $LAT -d $DEPTH -p $DATASET -v $VARIABLE
