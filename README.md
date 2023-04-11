# VPR Datasets Downloader

This repo is made to automatically download Visual Place Recognition (VPR) datasets in a simple and standardized way.
This is useful because all VPR datasets use different ways of storing the labels (some in csv files, some in matlab files, some in the filename), making it very inconvenient to train and test on different datasets.
Furthermore, some datasets (e.g. Pitts30k and Nordland) require some pre-processing, and small changes in the pre-processing can lead to changes in results.
The goal of this codebase is therefore to ensure that researchers and practitioners in VPR can use the same standardized datasets for their experiments.

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

<details>
    <summary>Cite / BibTex</summary>
<pre>
@article{Torii_2015_pitts,
    author = {A. {Torii} and J. {Sivic} and M. {Okutomi} and T. {Pajdla}},
    journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence}, 
    title = {Visual Place Recognition with Repetitive Structures}, 
    year = {2015}
}
</pre>
</details>

#### Pitts250k

For Pitts250k, first download the data under datasets/pitts250k/raw_data, then simply run `$ python format_pitts250k.py`

<details>
    <summary>Cite / BibTex</summary>
<br>
<pre>
@article{Torii_2015_pitts,
    author = {A. {Torii} and J. {Sivic} and M. {Okutomi} and T. {Pajdla}},
    journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence}, 
    title = {Visual Place Recognition with Repetitive Structures}, 
    year = {2015}
}
</pre>
</details>

#### Mapillary SLS

For Mapillary SLS, you need to first log in into their website, download it [here](https://www.mapillary.com/dataset/places),
 then extract the zip files, and place it in a folder `datasets` inside the repository root and name it
`mapillary_sls`.
Then you can run:

 `$ python format_mapillary.py`

<details>
    <summary>Cite / BibTex</summary>
<br>
<pre>
@inproceedings{Warburg_2020_msls,
    author={Warburg, Frederik and Hauberg, Soren and Lopez-Antequera, Manuel and Gargallo, Pau and Kuang, Yubin and Civera, Javier},
    title={Mapillary Street-Level Sequences: A Dataset for Lifelong Place Recognition},
    booktitle={IEEE Conference on Computer Vision and Pattern Recognition},
    month={June},
    year={2020}
}
</pre>
</details>

#### Eynsham

To download Eynsham, simply run `$ python download_eynsham.py`

<details>
    <summary>Cite / BibTex</summary>
<br>
<pre>
@inproceedings{Cummins_2009_eynsham,
    title={Highly scalable appearance-only SLAM - {FAB-MAP} 2.0},
    author={M. Cummins and P. Newman},
    booktitle={Robotics: Science and Systems},
    year={2009}
}
</pre>
</details>

#### San Francisco

To download San Francisco, simply run `$ python download_san_francisco.py`

<details>
    <summary>Cite / BibTex</summary>
<br>
<pre>
@inproceedings{Chen_2011_san_francisco,
    author={D. M. {Chen} and G. {Baatz} and K. {Köser} and S. S. {Tsai} and R. {Vedantham} and T. {Pylvänäinen} and K. {Roimela} and X. {Chen} and J. {Bach} and M. {Pollefeys} and B. {Girod} and R. {Grzeszczuk}},
    booktitle={IEEE Conference on Computer Vision and Pattern Recognition},
    title={City-scale landmark identification on mobile devices}, 
    year={2011},
    pages={737-744},
    doi={10.1109/CVPR.2011.5995610}
}
</pre>
</details>

#### St Lucia

To download St Lucia, simply run `$ python download_st_lucia.py`

<details>
    <summary>Cite / BibTex</summary>
<br>
<pre>
@article{Milford_2008_st_lucia,
    title={Mapping a Suburb With a Single Camera Using a Biologically Inspired SLAM System},
    author={Michael Milford and G. Wyeth},
    journal={IEEE Transactions on Robotics},
    year={2008},
    volume={24},
    pages={1038-1053}
}
</pre>
</details>

#### SVOX

To download SVOX, simply run `$ python download_svox.py`

<details>
    <summary>Cite / BibTex</summary>
<br>
<pre>
@inproceedings{Berton_2021_svox, 
    author = {Berton, Gabriele and Paolicelli, Valerio and Masone, Carlo and Caputo, Barbara},
    title = {Adaptive-Attentive Geolocalization From Few Queries: A Hybrid Approach},
    booktitle = {IEEE Winter Conference on Applications of Computer Vision},
    month = {January},
    year = {2021},
    pages = {2918-2927}
}
</pre>
</details>

#### Nordland

To download Nordland, simply run `$ python download_nordland.py`

The images will be arranged to have GPS/UTM labels compatible with the benchmarking code. More info on it are in the comment on top of the `download_nordland.py` script. We used the splits used by the [Patch-NetVLAD paper](https://arxiv.org/abs/2103.01486).

<details>
    <summary>Cite / BibTex</summary>
<br>
<pre>
@inproceedings{Sunderhauf_2013_nordland,
    title = {Are we there yet? Challenging {SeqSLAM} on a 3000 km journey across all four seasons},
    author = {N. S{\"u}nderhauf and P. Neubert and P. Protzel},
    booktitle = {Proc. of Workshop on Long-Term Autonomy, }#icra,
    pages = {2013},
    year = {2013}
}
</pre>
</details>

#### Tokyo 24/7

For Tokyo 24/7, first download the data under datasets/tokyo247/raw_data, then simply run `$ python format_tokyo247.py`. Queries are automatically downloaded.

<details>
    <summary>Cite / BibTex</summary>
<br>
<pre>
@article{Torii_2018_tokyo247,
    author = {A. {Torii} and R. {Arandjelović} and J. {Sivic} and M. {Okutomi} and T. {Pajdla}},
    journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence}, 
    title = {24/7 Place Recognition by View Synthesis}, 
    year = {2018},
    volume = {40},
    number = {2},
    pages = {257-271}
}
</pre>
</details>

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
