
"""
San Francisco Landmark Dataset
The gallery contains 1.06M images, which in the paper are referred to 
as PCIs (perspective central images). PFIs are ignored, as they are a subset of PCIs.
The query set consists of 803 images taken with different camera phones.
The dataset is not suitable for training, as there is no "time machine".

TODO there's been a change, the original positions are up to 305 meters wrong,
so I used the labels from revisited SF (see survey)
"""

import os
import utm
import math
import shutil
from glob import glob
from tqdm import tqdm
from os.path import join

import util
import map_builder

datasets_folder = join(os.curdir, "datasets")
dataset_name = "san_francisco"
dataset_folder = join(datasets_folder, dataset_name)
raw_data_folder = join(datasets_folder, dataset_name, "raw_data")
os.makedirs(dataset_folder, exist_ok=True)
os.makedirs(raw_data_folder, exist_ok=True)
os.makedirs(join(dataset_folder, "images", "test"), exist_ok=True)

#### Gallery
print("Downloading gallery archives")
filenames = [f"PCIs_{i*1000:08d}_{(i+1)*1000:08d}_3.tar" for i in range(11, 150)]
urls = [f"https://stacks.stanford.edu/file/druid:vn158kj2087/{f}" for f in filenames]
tars_paths = [join(raw_data_folder, f) for f in filenames]
for i, (url, tar_path) in enumerate(zip(urls, tars_paths)):
    if os.path.exists(tar_path.replace("PCIs_", "").replace(".tar", "")):
        continue
    print(f"{i:>3} / {len(filenames)} ) downloading {tar_path}")
    util.download_heavy_file(url, tar_path)
    try:  # Unpacking gallery archives
        shutil.unpack_archive(tar_path, raw_data_folder)
    except shutil.ReadError:
        pass  # Some tars are empty files

print("Formatting gallery files")
dst_gallery_folder = join(dataset_folder, "images", "test", "gallery")
os.makedirs(dst_gallery_folder, exist_ok=True)
src_images_paths = sorted(glob(join(raw_data_folder, "**", "*.jpg"), recursive=True))
for src_image_path in tqdm(src_images_paths, ncols=100):
    _, _, pano_id, latitude, longitude, building_id, tile_num, carto_id, heading, pitch = os.path.basename(src_image_path).split("_")
    pitch = pitch.replace(".jpg", "")
    dst_image_name = util.get_dst_image_name(latitude, longitude, pano_id, tile_num,
                                          heading, pitch, extension=".jpg")
    dst_image_path = join(dst_gallery_folder, dst_image_name)
    _ = shutil.move(src_image_path, dst_image_path)

#### Queries
print("Downloading query archive")
queries_zip_filename = "BuildingQueryImagesCartoIDCorrected-Upright.zip"
url = f"https://stacks.stanford.edu/file/druid:vn158kj2087/{queries_zip_filename}"
queries_zip_path = join(raw_data_folder, queries_zip_filename)
util.download_heavy_file(url, queries_zip_path)

print("Unpacking query archive")
shutil.unpack_archive(queries_zip_path, raw_data_folder)

print("Formatting query files")
dst_queries_folder = join(dataset_folder, "images", "test", "queries")
os.makedirs(dst_queries_folder, exist_ok=True)
poses_file_path = join(raw_data_folder, "reference_poses_598.zip")
util.download_heavy_file("http://www.ok.sc.e.titech.ac.jp/~torii/project/vlocalization/icons/reference_poses_598.zip",
                         poses_file_path)
shutil.unpack_archive(poses_file_path, raw_data_folder)

with open(join(raw_data_folder, "reference_poses_598", "reference_poses_addTM_all_598.txt"), "r") as file:
    lines = file.readlines()[1:]

for line in lines:
    _, image_id, x, y, w, z, utm_east, utm_north, _ = line.split(" ")
    latitude, longitude = utm.to_latlon(float(utm_east), float(utm_north), 10, "S")
    x, y, w, z = float(x), float(y), float(w), float(z)
    yaw = math.atan2(2.0 * (z * x + y * w) , - 1.0 + 2.0 * (x * x + y * y))
    heading = ((((yaw / math.pi) + 1) * 180) + 180) % 360
    dst_image_name = util.get_dst_image_name(latitude, longitude, pano_id=image_id, heading=heading)
    dst_image_path = join(dst_queries_folder, dst_image_name)
    src_image_path = join(raw_data_folder, "BuildingQueryImagesCartoIDCorrected-Upright", f"{image_id}.jpg")
    _ = shutil.copy(src_image_path, dst_image_path)

map_builder.build_map_from_dataset(dataset_folder)
# shutil.rmtree(dataset_folder, "raw_data")

