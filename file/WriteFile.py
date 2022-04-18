import os

filePath = "c:\\work\\test.txt"

try:
    file = open(filePath, 'w', encoding='UTF-8')
except OSError as e:
    print("ファイルを書き込めませんでした。")
    quit()

file.write("test")

file.close()
