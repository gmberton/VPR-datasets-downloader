
"""
Mapillary Street-level Sequences (MSLS)
IMPORTANT: first you need to download the zip files from https://www.mapillary.com/dataset/places
then run this script to format the dataset.
Well organized dataset for visual geolocalization. Only flaw is that almost all images are
forward views of the car, with very few images sideways.
Other flaw is that it's not dense, but sparse in sequences.
"""

import os
import utm
import shutil
from glob import glob
from tqdm import tqdm

# This dictionary is copied from the original code
# https://github.com/mapillary/mapillary_sls/blob/master/mapillary_sls/datasets/msls.py#L16
default_cities = {
    'train': ["trondheim", "london", "boston", "melbourne", "amsterdam","helsinki",
              "tokyo","toronto","saopaulo","moscow","zurich","paris","bangkok",
              "budapest","austin","berlin","ottawa","phoenix","goa","amman","nairobi","manila"],
    'val': ["cph", "sf"],
    'test': ["miami","athens","buenosaires","stockholm","bengaluru","kampala"]
}

def format_coord(num, left=2, right=5):
    sign = "-" if float(num) < 0 else ""
    num = str(abs(float(num))) + "."
    integer, decimal = num.split(".")[:2]
    left -= len(sign)
    return f"{sign}{int(integer):0{left}d}.{decimal[:right]:<0{right}}"

def format_location_info(latitude, longitude):
    easting, northing, zone_number, zone_letter = utm.from_latlon(float(latitude), float(longitude))
    easting = format_coord(easting, 7, 2)
    northing = format_coord(northing, 7, 2)
    latitude = format_coord(latitude, 3, 5)
    longitude = format_coord(longitude, 4, 5)
    return easting, northing, zone_number, zone_letter, latitude, longitude

#### TODO questa funzione è uguale a quella in util.py
def get_dst_image_name(latitude, longitude, pano_id=None, tile_num=None, heading=None,
                   pitch=None, roll=None, height=None, timestamp=None, note=None, extension=".jpg"):
    easting, northing, zone_number, zone_letter, latitude, longitude = format_location_info(latitude, longitude)
    tile_num  = f"{int(float(tile_num)):02d}" if tile_num  is not None else ""
    heading   = f"{int(float(heading)):03d}"  if heading   is not None else ""
    pitch     = f"{int(float(pitch)):03d}"    if pitch     is not None else ""
    timestamp = f"{timestamp}"                if timestamp is not None else ""
    note      = f"{note}"                     if note      is not None else ""
    if roll is None: roll = ""
    else: raise NotImplementedError()
    if height is None: height = ""
    else: raise NotImplementedError()
    
    return f"@{easting}@{northing}@{zone_number:02d}@{zone_letter}@{latitude}@{longitude}" + \
           f"@{pano_id}@{tile_num}@{heading}@{pitch}@{roll}@{height}@{timestamp}@{note}@{extension}"

# TODO
csv_files_paths = sorted(glob("*/*/postprocessed.csv"))

for csv_file_path in csv_files_paths:
    with open(csv_file_path, "r") as file:
        postprocessed_lines = file.readlines()[1:]
    with open(csv_file_path.replace("postprocessed", "raw"), "r") as file:
        raw_lines = file.readlines()[1:]
    assert len(raw_lines) == len(postprocessed_lines)
    city, folder, _ = csv_file_path.split("/")
    folder = "gallery" if folder == "database" else "queries"
    train_val = "train" if city in default_cities["train"] else "val"
    dst_folder = f"___mio_datasev3/{train_val}/{folder}"
    os.makedirs(dst_folder, exist_ok=True)
    for postprocessed_line, raw_line in zip(tqdm(postprocessed_lines, desc=csv_file_path), raw_lines):
        _, pano_id, lon, lat, _, timestamp, is_panorama = raw_line.split(",")
        if is_panorama == "True\n":
            continue
        timestamp = timestamp.replace("-", "")
        view_direction = postprocessed_line.split(",")[-1].replace("\n", "").lower()
        day_night = "day" if postprocessed_line.split(",")[-2] == "False" else "night"
        note = f"{day_night}_{view_direction}_{city}"
        dst_image_name = get_dst_image_name(lat, lon, pano_id, timestamp=timestamp, note=note)
        src_image_path = f"{os.path.dirname(csv_file_path)}/images/{pano_id}.jpg"
        _ = shutil.copy(src_image_path, f"{dst_folder}/{dst_image_name}")

# TODO clean up
os.symlink(os.path.abspath("___mio_datasev3/val"), "___mio_datasev3/test")

"""
import os
os.symlink(os.path.abspath("val"), "test")
"""

