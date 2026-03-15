# VPR Datasets Downloader

This repo is made to automatically download Visual Place Recognition (VPR) datasets in a simple and standardized way.
This is useful because all VPR datasets use different ways of storing the labels (some in csv files, some in matlab files, some in the filename), making it very inconvenient to train and test on different datasets.
Furthermore, some datasets (e.g. Pitts30k) require some pre-processing, and small changes in the pre-processing can lead to changes in results.
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
- Eynsham - as test set only
- San Francisco Landmark - as test set only
- Tokyo 24/7* - as test set only
- St Lucia - as test set only
- SVOX - as test set only
- Nordland - as test set only
- AmsterTime - as test set only
- SPED - as test set only
- Baidu - as test set only

For most datasets, simply run the corresponding python script, that will download,
unpack and format the file according to the structure above.
Some datasets are available via rsync from `rsync://vandaldata.polito.it/sf_xl/VPR-datasets-downloader/`
(run commands from within the `datasets/` directory of this repository).

*: for Pitts30k, Pitts250k and Tokyo 24/7 the images should be downloaded by asking permission to the respective authors. Then they can be formatted with this codebase

*\*: for Mapillary SLS, you need to first log in into their website, download it [here](https://www.mapillary.com/dataset/places),
 then extract the zip files and run
 `$ python format_mapillary.py`

#### Pitts30k

For Pitts30k, first download the data under datasets/pitts30k/raw_data, then simply run `$ python format_pitts30k.py`

<details>
<summary>Cite / BibTex</summary>

```bibtex
@article{Torii_2015_pitts,
    author  = {Torii, Akihiko and Sivic, Josef and Okutomi, Masatoshi and Pajdla, Tomas},
    title   = {Visual Place Recognition with Repetitive Structures},
    journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
    year    = {2015}
}
```

</details>

#### Pitts250k

For Pitts250k, first download the data under datasets/pitts250k/raw_data, then simply run `$ python format_pitts250k.py`

<details>
<summary>Cite / BibTex</summary>

```bibtex
@article{Torii_2015_pitts,
    author  = {Torii, Akihiko and Sivic, Josef and Okutomi, Masatoshi and Pajdla, Tomas},
    title   = {Visual Place Recognition with Repetitive Structures},
    journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
    year    = {2015}
}
```

</details>

#### Mapillary SLS

For Mapillary SLS, you need to first log in into their website, download it [here](https://www.mapillary.com/dataset/places),
 then extract the zip files, and place it in a folder `datasets` inside the repository root and name it
`mapillary_sls`.
Then you can run:

 `$ python format_mapillary.py`

<details>
<summary>Cite / BibTex</summary>

```bibtex
@inproceedings{Warburg_2020_msls,
    author    = {Warburg, Frederik and Hauberg, Soren and Lopez-Antequera, Manuel and Gargallo, Pau and Kuang, Yubin and Civera, Javier},
    title     = {Mapillary Street-Level Sequences: A Dataset for Lifelong Place Recognition},
    booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    month     = {June},
    year      = {2020}
}
```

</details>

#### Eynsham

To download Eynsham, run from the `datasets/` directory:
```
rsync -rhz --info=progress2 --ignore-existing rsync://vandaldata.polito.it/sf_xl/VPR-datasets-downloader/eynsham .
```


<details>
<summary>Cite / BibTex</summary>
If using Eynsham, two papers should be cited: the first is the data collection work; the second performed the sampling, formatting, and data curation that produced the version available here.

```bibtex
@inproceedings{Cummins_2009_eynsham,
    author    = {Cummins, Mark and Newman, Paul},
    title     = {Highly scalable appearance-only SLAM - {FAB-MAP} 2.0},
    booktitle = {Robotics: Science and Systems},
    year      = {2009}
}

@inproceedings{Berton_CVPR_2022_benchmark,
    author    = {Berton, Gabriele and Mereu, Riccardo and Trivigno, Gabriele and Masone, Carlo and Csurka, Gabriela and Sattler, Torsten and Caputo, Barbara},
    title     = {Deep Visual Geo-Localization Benchmark},
    booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    month     = {June},
    year      = {2022}
}
```

</details>

#### San Francisco Landmark

To download San Francisco Landmark, simply run `$ python download_san_francisco.py`

<details>
<summary>Cite / BibTex</summary>

```bibtex
@inproceedings{Chen_2011_san_francisco,
    author    = {Chen, David M. and Baatz, Georges and K{\"o}ser, Kevin and Tsai, Sam S. and Vedantham, Ramakrishna and Pylv{\"a}n{\"a}inen, Timo and Roimela, Kimmo and Chen, Xin and Bach, Jeff and Pollefeys, Marc and Girod, Bernd and Grzeszczuk, Radek},
    title     = {City-scale landmark identification on mobile devices},
    booktitle = {IEEE Conference on Computer Vision and Pattern Recognition},
    year      = {2011},
    pages     = {737--744}
}
```

</details>

#### St Lucia

To download St Lucia, run from the `datasets/` directory:
```
rsync -rhz --info=progress2 --ignore-existing rsync://vandaldata.polito.it/sf_xl/VPR-datasets-downloader/st_lucia .
```


<details>
<summary>Cite / BibTex</summary>
If using St Lucia, two papers should be cited: the first is the data collection work; the second performed the sampling, formatting, and data curation that produced the version available here.

```bibtex
@article{Milford_2008_st_lucia,
    author  = {Milford, Michael J. and Wyeth, Gordon F.},
    title   = {Mapping a Suburb With a Single Camera Using a Biologically Inspired SLAM System},
    journal = {IEEE Transactions on Robotics},
    volume  = {24},
    pages   = {1038--1053},
    year    = {2008}
}

@inproceedings{Berton_CVPR_2022_benchmark,
    author    = {Berton, Gabriele and Mereu, Riccardo and Trivigno, Gabriele and Masone, Carlo and Csurka, Gabriela and Sattler, Torsten and Caputo, Barbara},
    title     = {Deep Visual Geo-Localization Benchmark},
    booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    month     = {June},
    year      = {2022}
}
```

</details>

#### SVOX

To download SVOX, simply run `$ python download_svox.py`

<details>
<summary>Cite / BibTex</summary>

```bibtex
@inproceedings{Berton_2021_svox,
    author    = {Berton, Gabriele and Paolicelli, Valerio and Masone, Carlo and Caputo, Barbara},
    title     = {Adaptive-Attentive Geolocalization From Few Queries: A Hybrid Approach},
    booktitle = {IEEE/CVF Winter Conference on Applications of Computer Vision},
    month     = {January},
    year      = {2021},
    pages     = {2918--2927}
}
```

</details>

#### Nordland

To download Nordland, run from the `datasets/` directory:
```
rsync -rhz --info=progress2 --ignore-existing rsync://vandaldata.polito.it/sf_xl/VPR-datasets-downloader/nordland .
```

The images are arranged to have GPS/UTM labels compatible with the benchmarking code. We used the splits used by the [Patch-NetVLAD paper](https://arxiv.org/abs/2103.01486).

<details>
<summary>Cite / BibTex</summary>

```bibtex
@inproceedings{Sunderhauf_2013_nordland,
    author    = {S{\"u}nderhauf, Niko and Neubert, Peer and Protzel, Peter},
    title     = {Are we there yet? Challenging {SeqSLAM} on a 3000 km journey across all four seasons},
    booktitle = {Proc. of Workshop on Long-Term Autonomy, }#icra,
    year      = {2013}
}
```

</details>

#### Tokyo 24/7

For Tokyo 24/7, first download the data under datasets/tokyo247/raw_data, then simply run `$ python format_tokyo247.py`. Queries are automatically downloaded.

<details>
<summary>Cite / BibTex</summary>

```bibtex
@article{Torii_2018_tokyo247,
    author  = {Torii, Akihiko and Arandjelovi{\'c}, Relja and Sivic, Josef and Okutomi, Masatoshi and Pajdla, Tomas},
    title   = {24/7 Place Recognition by View Synthesis},
    journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
    volume  = {40},
    number  = {2},
    pages   = {257--271},
    year    = {2018}
}
```

</details>

#### Baidu

To download Baidu, run from the `datasets/` directory:
```
rsync -rhz --info=progress2 --ignore-existing rsync://vandaldata.polito.it/sf_xl/VPR-datasets-downloader/baidu .
```

<details>
<summary>Cite / BibTex</summary>
If using Baidu, two papers should be cited: the first is the data collection work; the second performed the sampling, formatting, and data curation that produced the version available here.

```bibtex
@inproceedings{Sun_2017_baidu,
    author    = {Sun, Xun and Xie, Yuanfan and Luo, Pei and Wang, Liang},
    title     = {A Dataset for Benchmarking Image-Based Localization},
    booktitle = {IEEE Conference on Computer Vision and Pattern Recognition},
    pages     = {5641--5649},
    year      = {2017}
}

@inproceedings{Berton_2025_MegaLoc,
    author    = {Berton, Gabriele and Masone, Carlo},
    title     = {MegaLoc: One Retrieval to Place Them All},
    booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops},
    year      = {2025}
}
```

</details>


## Cite / BibTex
If you use this codebase, please cite [our benchmark](https://github.com/gmberton/deep-visual-geo-localization-benchmark) for which this code was built, and the respective paper for the datasets.
```bibtex
@inproceedings{Berton_CVPR_2022_benchmark,
    author    = {Berton, Gabriele and Mereu, Riccardo and Trivigno, Gabriele and Masone, Carlo and Csurka, Gabriela and Sattler, Torsten and Caputo, Barbara},
    title     = {Deep Visual Geo-Localization Benchmark},
    booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    month     = {June},
    year      = {2022}
}
```
