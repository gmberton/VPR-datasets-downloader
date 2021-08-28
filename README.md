

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
            │   ├── gallery
            │   └── queries
            ├── train
            │   ├── gallery
            │   └── queries
            └── val
                ├── gallery
                └── queries
```
To download Pitts30k, simply run `$ python d_pitts30k.py`
Pitts30k is about 2 GB, but you need at least 21 GB of free space. After downloading you can delete the directory raw_data

For Mapillary SLS you should download it from [here](https://www.mapillary.com/dataset/places), then extract the zip files and run `$ python format_mapillary.py`

