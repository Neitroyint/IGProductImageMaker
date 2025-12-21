import os
import shutil

from data.constants import TEMP_EXT


def wipe_data(path: str) -> None:
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def create_output_dir(paths: list) -> None:
    for dir in paths:
        if not os.path.exists(dir):
            os.mkdir(dir)

def get_all_templates(path: str) -> list:
    files = []
    for f in os.listdir(path):
        if f.lower().endswith(TEMP_EXT):
            files.append(f)
    return files