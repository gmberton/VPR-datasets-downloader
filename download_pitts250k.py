"""
Pitts250k dataset from Pittsburgh.
"""
import os
import re
import utm
import shutil
from tqdm import tqdm
from os.path import join
from scipy.io import loadmat

import util
import map_builder

datasets_folder = join(os.curdir, "datasets")
dataset_name = "pitts250k"
dataset_folder = join(datasets_folder, dataset_name)
raw_data_folder = join(datasets_folder, dataset_name, "raw_data")
os.makedirs(dataset_folder, exist_ok=True)
os.makedirs(raw_data_folder, exist_ok=True)

for filename in ["000.tar", "001.tar", "002.tar", "003.tar", "004.tar", "005.tar",
                 "006.tar", "007.tar", "008.tar", "009.tar", "010.tar",
                 "groundtruth.tar", "netvlad_v100_datasets.tar.gz",
                 "pose.txt", "queries_real.tar", "readGt.m"]:
    url = f"https://data.ciirc.cvut.cz/public/projects/2015netVLAD/Pittsburgh250k/{filename}"
    util.download_heavy_file(url, join(raw_data_folder, filename))
    if filename.endswith(".tar") or filename.endswith(".tar.gz"):
        shutil.unpack_archive(join(raw_data_folder, filename), raw_data_folder)


def copy_images(dst_folder, src_images_paths, utms):
    os.makedirs(dst_folder, exist_ok=True)
    for src_image_path, (utm_east, utm_north) in zip(tqdm(src_images_paths, desc=f"Copy to {dst_folder}"),
                                                     utms):
        src_image_name = os.path.basename(src_image_path)
        latitude, longitude = utm.to_latlon(utm_east, utm_north, 17, "T")
        pitch = int(re.findall('pitch(\d+)_', src_image_name)[0])-1
        yaw =   int(re.findall('yaw(\d+)\.', src_image_name)[0])-1
        note = re.findall('_(.+)\.jpg', src_image_name)[0]
        tile_num = pitch*24 + yaw
        dst_image_name = util.get_dst_image_name(latitude, longitude, pano_id=src_image_name.split("_")[0],
                                                tile_num=tile_num, note=note)

        src_path = os.path.join(dataset_folder, 'raw_data', src_image_path)
        dst_path = os.path.join(dst_folder, dst_image_name)
        # shutil.copyfile(f"{dataset_folder}/raw_data/{src_image_path}", f"{dst_folder}/{dst_image_name}")
        shutil.move(src_path, dst_path)


for dataset in ["train", "val", "test"]:
    # matlab_struct_file_path = f"{dataset_folder}/raw_data/datasets/pitts250k_{dataset}.mat"
    matlab_struct_file_path = os.path.join(dataset_folder, "raw_data", "datasets", f"pitts250k_{dataset}.mat")
    mat_struct = loadmat(matlab_struct_file_path)["dbStruct"].item()
    # Gallery
    g_images = [f[0].item() for f in mat_struct[1]]
    g_utms = mat_struct[2].T
    # copy_images(f"{dataset_folder}/images/{dataset}/gallery", g_images, g_utms)
    copy_images(os.path.join(dataset_folder, 'images', dataset, 'database'), g_images, g_utms)
    # Queries
    # q_images = [f"queries_real/{f[0].item()}" for f in mat_struct[3]]
    q_images = [os.path.join("queries_real", f"{f[0].item()}") for f in mat_struct[3]]

    q_utms = mat_struct[4].T
    copy_images(f"{dataset_folder}/images/{dataset}/queries", q_images, q_utms)
    copy_images(os.path.join(dataset_folder, 'images', dataset, 'queries'), q_images, q_utms)

map_builder.build_map_from_dataset(dataset_folder)
shutil.rmtree(raw_data_folder)
