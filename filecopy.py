from itertools import chain
from datetime import datetime, timezone

import os
import time
import shutil
import pathlib

FILE_PATTERN = [
    '*.png',
    '*.jpeg',
    '*.jpg',
    '*.mp4'
]
SOURCE_DIR = '.' # CURRENT DIRECTORY
COPY_DESTINATION = os.path.join('/tmp') # changes based on OS # c:/PHOTOS # /tmp, etc
file_copy_status = {
    'success': 0,
    'failure': 0
}


def do_copy_work():
    """
    Copy the file from source to destination according to YYYY-MM directory
    :return:
    """
    t1 = time.perf_counter()
    try:
        path_lib_obj = pathlib.Path('.')
        # Collect all the files
        files = chain(*[path_lib_obj.glob(f'**/{file_pattern}') for file_pattern in FILE_PATTERN])
        if not files:
            return f'Sorry no files to copy with the pattern : {FILE_PATTERN}'
        for file in files:
            try:
                if not file.is_file():
                    print(f'file not found: {file}')
                    file_copy_status['failure'] += 1
                    continue
                # Get the absolute path of the file
                source_file_abs_path = file.resolve()
                # Get the last changed timestamp of file
                last_changed_time = datetime.fromtimestamp(file.stat().st_atime) # tz=timezone.utc
                # Create a folder name from timestamp of file
                folder_name = last_changed_time.strftime('%Y-%m')
                destination_folder_name = os.path.join(COPY_DESTINATION, folder_name)
                destination_file_name = os.path.join(destination_folder_name, file.name)
                # print(f'destination_folder_name: {destination_folder_name}')
                # Check directory present, otherwise create it
                if not os.path.isdir(destination_folder_name):
                    os.makedirs(destination_folder_name)
                    print(f'Directory created [{destination_folder_name}]')
                shutil.copyfile(source_file_abs_path, destination_file_name)
                file_copy_status['success'] += 1
                print(f'file [{source_file_abs_path}] successfully copied to [{destination_file_name}]')
            except Exception as e:
                print(f'Failed to copy the file {file}', e)
                file_copy_status['failure'] += 1
    except Exception as e:
        print(f'Exception in running this function: {e}')
    finally:
        t2 = time.perf_counter()
        total_time = round(t2 - t1, 2)
        print(f'Total Time Taken to copy all the files: {total_time} seconds')

    return file_copy_status


if __name__ == '__main__':
    print(do_copy_work())

