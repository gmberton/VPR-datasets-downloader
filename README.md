

Using these scripts you can download a number of visual geolocalization datasets.
The datasets are downloaded and formatted using a standard format.
The format implies that the names of the files with the images are:

@ UTM_easting @ UTM_northing @ UTM_zone_number @ UTM_zone_letter @ latitude @ longitude 
    @ pano_id @ tile_num @ heading @ pitch @ roll @ height @ timestamp @ note @ extension

Note that for many datasets some of these values are empty, and the only required values are
UTM coordinates (obtained from latitude and longitude).

The directory tree that is generated is as follows:
```
.
└── datasets
    └── dataset_name
        └── images
            ├── test
            │   ├── database
            │   └── queries
            ├── train
            │   ├── database
            │   └── queries
            └── val
                ├── database
                └── queries
```
The list of datasets that you can download with this code is the following:
- Pitts30k
- Pitts250k
- Mapillary SLS*
- Eysham
- San Francisco
- Tokyo 24/7
- St Lucia
- SVOX

NB: For Mapillary SLS, you need to first log in into their website, download it [here](https://www.mapillary.com/dataset/places),
 then extract the zip files and run 
 `$ python format_mapillary.py`

To download each dataset, simply run the corresponding python script, that will download,
unpack and format the file according to the structure above.

## Pitts30k

To download Pitts30k, simply run `$ python download_pitts30k.py`
Pitts30k is about 2 GB, but you need at least 21 GB of free space as it is a computed
subset of Pitts250k. After downloading you can delete the directory raw_data

## Pitts250k

To download Pitts250k, simply run `$ python download_pitts250k.py`

## Eynsham

To download Eynsham, simply run `$ python download_eynsham.py`

## San Francisco

To download San Francisco, simply run `$ python download_san_francisco.py`

## Mapillary SLS

For Mapillary SLS, you need to first log in into their website, download it [here](https://www.mapillary.com/dataset/places),
 then extract the zip files and run 
 `$ python format_mapillary.py`

## St Lucia

To download St Lucia, simply run `$ python download_st_lucia.py`

## SVOX

To download SVOX, simply run `$ python download_svox.py`

## Tokyo 24/7

To download Tokyo 24/7, simply run `$ python download_tokyo247.py`
