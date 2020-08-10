import shutil
import os

path = '/Users/abelp/Downloads/'
os.chdir(path)
#print(os.listdir())

for file in os.listdir():
    filepath = os.path.join(path, file)
    if (file != 'desktop.ini') and (os.path.isfile(filepath)):
        #print(file)
        filename, file_extension = os.path.splitext(filepath)
        #print(file_extension)
        #print(os.path.exists(os.path.join(path, file_extension)))
        if not os.path.exists(os.path.join(path, file_extension)):
            os.makedirs(file_extension)
