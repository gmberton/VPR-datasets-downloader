
"""
https://arxiv.org/abs/2009.06364
https://vision.cs.tum.edu/data/datasets/4seasons-dataset/download
"""

import os
import shutil
from os.path import join

import util

datasets_root = join(os.curdir, "datasets")
dataset_name = "4seasons"
dataset_path = join(datasets_root, dataset_name)
os.makedirs(dataset_path, exist_ok=True)
os.makedirs(join(dataset_path, "raw_data"), exist_ok=True)

URL_ROOT = "https://vision.cs.tum.edu/webshare/g/4seasons-dataset/dataset/recording_2020-12-22_11-33-15"
for filename in [#"recording_2020-12-22_11-33-15_stereo_images_undistorted.zip",
                 "recording_2020-12-22_11-33-15_imu_gnss.zip",
                 "recording_2020-12-22_11-33-15_reference_poses.zip"]:  # "md5sums.txt"
    url = f"{URL_ROOT}/{filename}"
    util.download_heavy_file(url, join(dataset_path, "raw_data", filename))
    shutil.unpack_archive(join(dataset_path, "raw_data", filename), join(dataset_path, "raw_data"))

