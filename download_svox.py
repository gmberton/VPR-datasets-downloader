
import os
from os.path import join
from google_drive_downloader import GoogleDriveDownloader as gdd

datasets_folder = join(os.curdir, "datasets")
gdd.download_file_from_google_drive(file_id='16iuk8voW65GaywNUQlWAbDt6HZzAJ_t9',
                                    dest_path=join(datasets_folder, 'svox.zip'),
                                    unzip=True)

os.remove(join(datasets_folder, 'svox.zip'))
