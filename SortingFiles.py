import shutil
import os

path = '/Users/abelp/Downloads/'
os.chdir(path)

for file in os.listdir():
    filepath = os.path.join(path, file)
    if (file != 'desktop.ini') and (os.path.isfile(filepath)):
        filename, file_extension = os.path.splitext(filepath)
        if not os.path.exists(os.path.join(path, file_extension)):
            os.makedirs(file_extension)
        dest_directory = os.path.join(path, file_extension)
        print(dest_directory)
        shutil.move(filepath, dest_directory )

