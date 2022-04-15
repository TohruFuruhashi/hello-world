import shutil
import os

# set your path
filePath = 'file path'
copiedFilePath= 'copied file path'

try:
    shutil.copy(filePath, copiedFilePath)
except OSError as e:
    print("Couldn't copy file !")

os.system("pause")
