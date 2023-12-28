
import shutil
from pathlib import Path
from zipfile import ZipFile

import util

URL = "https://surfdrive.surf.nl/files/index.php/s/sbZRXzYe3l0v67W/download?path=%2F&files=SPEDTEST.zip"

zip_filepath = Path("datasets", "sped", "raw_data", "sped.zip")
zip_filepath.parent.mkdir(exist_ok=True, parents=True)
util.download_heavy_file(URL, zip_filepath)

zf = ZipFile(zip_filepath, 'r')
zf.extractall(zip_filepath.parent)
zf.close()

database_paths = sorted((zip_filepath.parent / "SPEDTEST" / "ref").glob("*.jpg"))
queries_paths = sorted((zip_filepath.parent / "SPEDTEST" / "query").glob("*.jpg"))

database_folder = Path("datasets", "sped", "images", "test", "database")
queries_folder  = Path("datasets", "sped", "images", "test", "queries")
database_folder.mkdir(exist_ok=True, parents=True)
queries_folder.mkdir(exist_ok=True, parents=True)

assert len(database_paths) == len(queries_paths)
for db_path, q_path in zip(database_paths, queries_paths):
    db_path = Path(db_path)
    q_path = Path(q_path)
    assert db_path.name == q_path.name
    mock_utm_east = int(db_path.stem) * 1000
    new_image_name = f"@0@{mock_utm_east}@@@@@{db_path.stem}@@@@@@@@.jpg"
    new_db_path = Path(database_folder, new_image_name)
    new_q_path = Path(queries_folder, new_image_name)
    _ = shutil.move(db_path, new_db_path)
    _ = shutil.move(q_path, new_q_path)

shutil.rmtree(zip_filepath.parent)


