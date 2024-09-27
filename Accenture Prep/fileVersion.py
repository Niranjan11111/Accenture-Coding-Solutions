def newFileVersion(files):
    newVersion = 0
    for file in files:
        file = file.replace("file_", "")
        if int(file) > newVersion:
            newVersion = int(file)
    return newVersion

files = ["file_20", "file_2", "file_8", "file_70", "file_2"]
print(newFileVersion(files))