import os
import zipfile

file_types = ['.pdf', '.xlsx', '.csv']


def test_zip_unzip_files():
    archive = zipfile.ZipFile('resources/files.zip', 'w')
    for folder, subfolders, files in os.walk('resources'):
        for file in files:
            check_file_types(file, folder, archive)
    close(archive)
    archive = zipfile.ZipFile('resources/files.zip')
    archive.extractall('unpacked/')
    close(archive)


def check_file_types(file, folder, archive):
    if file.endswith(file_types[0]) or file.endswith(file_types[1]) or file.endswith(file_types[2]):
        archive.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), 'resources'),
                      compress_type=zipfile.ZIP_DEFLATED)


def close(archive):
    archive.close()
