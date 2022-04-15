import shutil
import gzip

try:
    with gzip.open(gzipFilePath, mode="rb") as gzipFile:
        with open(decompressedFilePath, mode="wb") as decompressedFile:
            shutil.copyfileobj(gzipFile, decompressedFile)
except OSError as e:
    print("Couldn't decompress the file !!")
