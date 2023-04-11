# VPR Datasets Downloader

This repo is made to automatically download Visual Place Recognition (VPR) datasets in a simple and standardized way.
This is useful because all VPR datasets use different ways of storing the labels (some in csv files, some in matlab files, some in the filename), making it very inconvenient to train and test on different datasets.
Furthermore, some datasets (e.g. Pitts30k and Nordland) require some pre-processing, and small changes in the pre-processing can lead to changes in results.
The goal of this codebase is therefore to ensure that researchers and practitioners in VPR can use the same standardize datasets for their experiments.

## Overview

The datasets are downloaded and formatted using a standard format: for some of the datasets also the maps are automatically created.
The adopted convention is that the names of the files with the images are:

`@ UTM_east @ UTM_north @ UTM_zone_number @ UTM_zone_letter @ latitude @ longitude @ pano_id @ tile_num @ heading @ pitch @ roll @ height @ timestamp @ note @ extension`

Note that for many datasets some of these values are empty, and however the only required values for VPR are UTM coordinates (obtained from latitude and longitude).

The reason for using the character `@` as a separator, is that commonly used characters such as dash `-` or underscore `_` might be used in the fields, for example in the `pano_id` field.

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

Most datasets are used only for testing, and therefore do not have a train and validation set.

## Available datasets

The list of datasets that you can download with this codebase is the following:
- Pitts30k*
- Pitts250k*
- Mapillary SLS**
- Eysham - as test set only
- San Francisco - as test set only
- Tokyo 24/7* - as test set only
- St Lucia - as test set only
- SVOX - as test set only
- Nordland - as test set only
- AmsterTime - as test set only

To download each dataset, simply run the corresponding python script, that will download,
unpack and format the file according to the structure above.

*: for Pitts30k, Pitts250k and Tokyo 24/7 the images should be downloaded by asking permission to the respective authors. Then they can be formatted with this codebase

*\*: for Mapillary SLS, you need to first log in into their website, download it [here](https://www.mapillary.com/dataset/places),
 then extract the zip files and run 
 `$ python format_mapillary.py`

#### Pitts30k

For Pitts30k, first download the data under datasets/pitts30k/raw_data, then simply run `$ python format_pitts30k.py`

#### Pitts250k

For Pitts250k, first download the data under datasets/pitts250k/raw_data, then simply run `$ python format_pitts250k.py`

#### Mapillary SLS

For Mapillary SLS, you need to first log in into their website, download it [here](https://www.mapillary.com/dataset/places),
 then extract the zip files, and place it in a folder `datasets` inside the repository root and name it
`mapillary_sls`.
Then you can run:

 `$ python format_mapillary.py`

#### Eynsham

To download Eynsham, simply run `$ python download_eynsham.py`

#### San Francisco

To download San Francisco, simply run `$ python download_san_francisco.py`

#### St Lucia

To download St Lucia, simply run `$ python download_st_lucia.py`

#### SVOX

To download SVOX, simply run `$ python download_svox.py`

#### Nordland

To download Nordland, simply run `$ python download_nordland.py`

The images will be arranged to have GPS/UTM labels compatible with the benchmarking code. More info on it are in the comment on top of the `download_nordland.py` script. We used the splits used by the [Patch-NetVLAD paper](https://arxiv.org/abs/2103.01486).

#### Tokyo 24/7

For Tokyo 24/7, first download the data under datasets/tokyo247/raw_data, then simply run `$ python format_tokyo247.py`. Queries are automatically downloaded.

## Cite / BibTex
If you use this codebase, please cite [our benchmark](https://github.com/gmberton/deep-visual-geo-localization-benchmark) for which this code was built, and the respective paper for the datasets.
```
@inProceedings{Berton_CVPR_2022_benchmark,
    author    = {Berton, Gabriele and Mereu, Riccardo and Trivigno, Gabriele and Masone, Carlo and
                 Csurka, Gabriela and Sattler, Torsten and Caputo, Barbara},
    title     = {Deep Visual Geo-localization Benchmark},
    booktitle = {CVPR},
    month     = {June},
    year      = {2022},
}
```
