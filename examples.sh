#! /bin/bash


#  "ls like" commands

rm -f copernicusmarineout.txt
copernicusmarine get -i cmems_mod_med_bgc-bio_anfc_4.2km_P1D-m --filter "*${DAY}_d-OGS*" --disable-progress-bar --create-file-list copernicusmarineout.txt > /dev/null 2>&1
for I in $( cat copernicusmarineout.txt) ; do echo $I | cut -d "/" -f 9 ; done
rm -f copernicusmarineout.txt

aws s3 ls --endpoint-url https://s3.waw3-1.cloudferro.com --no-sign-request s3://mdl-native-12/native/MEDSEA_ANALYSISFORECAST_BGC_006_014/cmems_mod_med_bgc-bio_anfc_4.2km_P1D-m_202211/2024/08/



# file download

#examples of copernicusmarine get 
#Sat CHL NRT
copernicusmarine get -nd  -o $PWD/ -s files  -i cmems_obs-oc_med_bgc-plankton_nrt_l3-multi-1km_P1D --force-download --show-outputnames  --force-dataset-version 202211 --overwrite


#Sat CHL DT
copernicusmarine get -nd  -o $PWD/ -s files  -i cmems_obs-oc_med_bgc-plankton_my_l3-multi-1km_P1D  --force-download --show-outputnames  --overwrite --filter '*202402*'

# download of a single file
aws s3 cp --endpoint-url https://s3.waw3-1.cloudferro.com --no-sign-request s3://mdl-native-12/native/MEDSEA_ANALYSISFORECAST_BGC_006_014/cmems_mod_med_bgc-bio_anfc_4.2km_P1D-m_202211/2024/08/20240801_d-OGS--BIOL-MedBFM4-MED-b20240806_an-sv08.00.nc .



#examples of copernicusmarine subset
copernicusmarine subset --request-file example.json