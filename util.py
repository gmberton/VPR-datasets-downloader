
import os
import re
import utm
import cv2
import math


def get_distance(coords_A, coords_B):
    return math.sqrt((float(coords_B[0])-float(coords_A[0]))**2 + (float(coords_B[1])-float(coords_A[1]))**2)


def is_valid_timestamp(timestamp):
    """Return True if it's a valid timestamp, in format YYYYMMDD_hhmmss,
        with all fields from left to right optional.
    >>> is_valid_timestamp('')
    True
    >>> is_valid_timestamp('201901')
    True
    >>> is_valid_timestamp('20190101_123000')
    True
    """
    return bool(re.match("^(\d{4}(\d{2}(\d{2}(_(\d{2})(\d{2})?(\d{2})?)?)?)?)?$", timestamp))


def format_coord(num, left=2, right=5):
    """Return the formatted number as a string with (left) int digits 
            (including sign '-' for negatives) and (right) float digits.
    >>> format_coord2(1.1, 3, 3)
    '001.100'
    >>> format_coord2(-0.12345, 3, 3)
    '-00.123'
    >>> format_coord2(-0.123, 5, 5)
    '-0000.12300'
    """
    return f'{float(num):0={left+right+1}.{right}f}'

import doctest
doctest.testmod()  # Automatically execute unit-test of format_coord()


def format_location_info(latitude, longitude):
    easting, northing, zone_number, zone_letter = utm.from_latlon(float(latitude), float(longitude))
    easting = format_coord(easting, 7, 2)
    northing = format_coord(northing, 7, 2)
    latitude = format_coord(latitude, 3, 5)
    longitude = format_coord(longitude, 4, 5)
    return easting, northing, zone_number, zone_letter, latitude, longitude


def get_dst_image_name(latitude, longitude, pano_id=None, tile_num=None, heading=None,
                       pitch=None, roll=None, height=None, timestamp=None, note=None, extension=".jpg"):
    easting, northing, zone_number, zone_letter, latitude, longitude = format_location_info(latitude, longitude)
    tile_num  = f"{int(float(tile_num)):02d}" if tile_num  is not None else ""
    heading   = f"{int(float(heading)):03d}"  if heading   is not None else ""
    pitch     = f"{int(float(pitch)):03d}"    if pitch     is not None else ""
    timestamp = f"{timestamp}"                if timestamp is not None else ""
    note      = f"{note}"                     if note      is not None else ""
    assert is_valid_timestamp(timestamp), f"{timestamp} is not in YYYYMMDD_hhmmss format"
    if roll is None: roll = ""
    else: raise NotImplementedError()
    if height is None: height = ""
    else: raise NotImplementedError()
    
    return f"@{easting}@{northing}@{zone_number:02d}@{zone_letter}@{latitude}@{longitude}" + \
           f"@{pano_id}@{tile_num}@{heading}@{pitch}@{roll}@{height}@{timestamp}@{note}@{extension}"


class VideoReader:
    def __init__(self, video_name, size=None):
        if not os.path.exists(video_name):
            raise FileNotFoundError(f"{video_name} does not exist")
        self.video_name = video_name
        self.size = size
        self.vc = cv2.VideoCapture(f"{video_name}")
        self.frames_per_second = self.vc.get(cv2.CAP_PROP_FPS)
        self.frame_duration_millis = 1000 / self.frames_per_second
        self.frames_num = int(self.vc.get(cv2.CAP_PROP_FRAME_COUNT))
        self.video_length_in_millis = int(self.frames_num * 1000 / self.frames_per_second)

    def get_time_at_frame(self, frame_num):
        return int(self.frame_duration_millis * frame_num)

    def get_frame_num_at_time(self, time):
        # time can be str ('21:59') or int in milliseconds
        millis = time if type(time) == int else self.str_to_millis(time)
        return min(int(millis / self.frame_duration_millis), self.frames_num)

    def get_frame_at_frame_num(self, frame_num):
        self.vc.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        frame = self.vc.read()[1]
        if frame is None: return None  # In case of corrupt videos
        if self.size is not None:
            frame = cv2.resize(frame, self.size[::-1], cv2.INTER_CUBIC)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame

    @staticmethod
    def str_to_millis(time_str):
        return (int(time_str.split(":")[0]) * 60 + int(time_str.split(":")[1])) * 1000

    @staticmethod
    def millis_to_str(millis):
        if millis < 60*60*1000:
            return f"{math.floor((millis//1000//60)%60):02d}:{millis//1000%60:02d}"
        else:
            return f"{math.floor((millis//1000//60//60)%60):02d}:{math.floor((millis//1000//60)%60):02d}:{millis//1000%60:02d}"

    def __repr__(self):
        H, W = int(self.vc.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(self.vc.get(cv2.CAP_PROP_FRAME_WIDTH))
        return (f"Video '{self.video_name}' has {self.frames_num} frames, " +
                f"with resolution {H}x{W}, " +
                f"and lasts {self.video_length_in_millis // 1000} seconds "
                f"({self.millis_to_str(self.video_length_in_millis)}), therefore "
                f"there's a frame every {int(self.frame_duration_millis)} millis")

    def __del__(self):
        self.vc.release()

