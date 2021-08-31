

Using these scripts you can download a number of visual geolocalization datasets.
The datasets are downloaded and formatted using a standard format, suitable to be used by our open
source benchmarking software that you can find [here](https://github.com/gmberton/benchmarking_vg).
You can also find more information about our project in the dedicated [website](https://deep-vg-bench.herokuapp.com/).

About the datasets formatting, the adopted convention is that the names of the files with the images are:

@ UTM_easting @ UTM_northing @ UTM_zone_number @ UTM_zone_letter @ latitude @ longitude 
    @ pano_id @ tile_num @ heading @ pitch @ roll @ height @ timestamp @ note @ extension

Note that for many datasets some of these values are empty, and however the only required values are
UTM coordinates (obtained from latitude and longitude).

The directory tree that is generated is as follows:
```
.
└── datasets
    └── dataset_name
        └── images
            ├── train
            │   ├── database
            │   └── queries
            ├── val
            │   ├── database
            │   └── queries
            └── test
                ├── database
                └── queries
```

For training throughout our benchmark we used Pitts and MSLS as dataset, and the others, listed below, only as test 
set to evaluate the generalization capability of the models. This is for many reasons, like the absence
 of a time machine that is necessary to train robust models.

The list of datasets that you can download with this code is the following:
- Pitts30k
- Pitts250k
- Mapillary SLS*
- Eysham - as test set only
- San Francisco - as test set only
- Tokyo 24/7 - as test set only
- St Lucia - as test set only
- SVOX - as test set only

*: For Mapillary SLS, you need to first log in into their website, download it [here](https://www.mapillary.com/dataset/places),
 then extract the zip files and run 
 `$ python format_mapillary.py`

To download each dataset, simply run the corresponding python script, that will download,
unpack and format the file according to the structure above.

## Pitts30k

To download Pitts30k, simply run `$ python download_pitts30k.py`
Pitts30k is about 2 GB, but you need at least 21 GB of free space as it is a computed
subset of Pitts250k; unnecessary data will be automatically deleted after the formatting is completed.

## Pitts250k

To download Pitts250k, simply run `$ python download_pitts250k.py`

## Mapillary SLS

For Mapillary SLS, you need to first log in into their website, download it [here](https://www.mapillary.com/dataset/places),
 then extract the zip files, and place it in a folder `datasets` inside the repository root and name it
`mapillary_sls`.
Then you can run:

 `$ python format_mapillary.py`

## Eynsham

To download Eynsham, simply run `$ python download_eynsham.py`

## San Francisco

To download San Francisco, simply run `$ python download_san_francisco.py`


## St Lucia

To download St Lucia, simply run `$ python download_st_lucia.py`

## SVOX

To download SVOX, simply run `$ python download_svox.py`

## Tokyo 24/7

To download Tokyo 24/7, simply run `$ python download_tokyo247.py`
