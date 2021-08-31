import os
import re
import utm
import shutil
import torchvision
from glob import glob
from tqdm import tqdm
from PIL import Image
from os.path import join
from scipy.io import loadmat

import util
import map_builder

datasets_folder = join(os.curdir, "datasets")
dataset_name = "tokyo247"
dataset_folder = join(datasets_folder, dataset_name)
raw_data_folder = join(datasets_folder, dataset_name, "raw_data")
os.makedirs(dataset_folder, exist_ok=True)
os.makedirs(raw_data_folder, exist_ok=True)
os.makedirs(join(raw_data_folder, "tokyo247"), exist_ok=True)

filename = "netvlad_v100_datasets.tar.gz"
file_path = join(raw_data_folder, filename)
url = f"https://data.ciirc.cvut.cz/public/projects/2015netVLAD/Pittsburgh250k/{filename}"
util.download_heavy_file(url, file_path)
shutil.unpack_archive(file_path, raw_data_folder)


def copy_images(dst_folder, src_images_paths, utms, is_247):
    os.makedirs(dst_folder, exist_ok=True)
    for src_image_path, (utm_east, utm_north) in zip(tqdm(src_images_paths, desc=f"Copy to {dst_folder}", ncols=100),
                                                     utms):
        src_image_name = os.path.basename(src_image_path)
        latitude, longitude = utm.to_latlon(utm_east, utm_north, 54, 'S')
        pano_id = src_image_name[:22]
        if is_247:
            tile_num = int(re.findall('_012_(\d+)\.png', src_image_name)[0])//30
            timestamp = None
        else:
            tile_num = int(re.findall('_(\d+)_012\.jpg', src_image_name)[0])//30
            timestamp = os.path.basename(os.path.dirname(src_image_path))[1:]  # YYYYMM, such as 201503
        assert 0 <= tile_num < 12
        dst_image_name = util.get_dst_image_name(latitude, longitude, pano_id=pano_id,
                                                 tile_num=tile_num, timestamp=timestamp)
        Image.open(f"{dataset_folder}/raw_data/{src_image_path}").save(f"{dst_folder}/{dst_image_name}")


######## Tokyo24/7
#### Database
for filename in ["03814.tar", "03815.tar", "03816.tar", "03817.tar", "03818.tar",
                 "03819.tar", "03820.tar", "03821.tar", "03822.tar", "03823.tar",
                 "03824.tar", "03825.tar", "03826.tar", "03827.tar", "03828.tar",
                 "03829.tar"]:
    url = f"https://data.ciirc.cvut.cz/public/projects/2015netVLAD/Tokyo247/database_gsv_vga/{filename}"
    file_path = join(raw_data_folder, "tokyo247", filename)
    util.download_heavy_file(url, file_path)
    shutil.unpack_archive(file_path, join(raw_data_folder, "tokyo247"))

# matlab_struct_file_path = f"{dataset_folder}/raw_data/datasets/tokyo247.mat"
matlab_struct_file_path = join(dataset_folder, 'raw_data', 'datasets', 'tokyo247.mat')

mat_struct = loadmat(matlab_struct_file_path)["dbStruct"].item()
# g_images = [f"tokyo247/{f[0].item().replace('.jpg', '.png')}" for f in mat_struct[1]]
g_images = [join('tokyo247', f[0].item().replace('.jpg', '.png')) for f in mat_struct[1]]

g_utms = mat_struct[2].T
dst_folder = join(dataset_folder, 'images', 'test', 'gallery')
# copy_images(f"{dataset_folder}/images/test/gallery", g_images, g_utms, is_247=True)
copy_images(dst_folder, g_images, g_utms, is_247=True)

#### Queries
filename = "247query_subset_v2.zip"
url = f"https://data.ciirc.cvut.cz/public/projects/2015netVLAD/Tokyo247/queries/{filename}"
file_zip_path = join(raw_data_folder, "tokyo247", filename)
util.download_heavy_file(url, file_zip_path)
shutil.unpack_archive(file_zip_path, join(raw_data_folder, "tokyo247"))
src_queries_folder = file_zip_path.replace(".zip", "")
src_queries_paths = sorted(glob(join(src_queries_folder, "*.jpg")))
os.makedirs(join(dataset_folder, "images", "test", "queries"), exist_ok=True)
for src_query_path in tqdm(src_queries_paths, desc=f"Copying to {dataset_folder}/images/test/queries", ncols=100):
    csv_path = src_query_path.replace(".jpg", ".csv")
    with open(csv_path, "r") as file:
        info = file.readline()
    pano_id, latitude, longitude = info.split(",")[:3]
    pano_id = pano_id.replace(",jpg", "")
    dst_image_name = util.get_dst_image_name(latitude, longitude, pano_id=pano_id)
    dst_image_path = join(dataset_folder, "images", "test", "queries", dst_image_name)
    pil_img = Image.open(src_query_path)
    resized_pil_img = torchvision.transforms.Resize(480)(pil_img)
    resized_pil_img.save(dst_image_path)

map_builder.build_map_from_dataset(dataset_folder)

