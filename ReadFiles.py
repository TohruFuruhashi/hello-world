import glob

readFiles = glob.glob(workDir)

for readFilePath in readFiles:

    try:
        readFile = open(readFilePath, 'r', encoding='UTF-8')
    except OSError as e:
        print("Couldn't read the file !!")
        quit()

    for data in readFile:
        print(data)

    readFile.close()
