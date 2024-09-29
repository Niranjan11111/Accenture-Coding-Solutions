# def newFileVersion(files):
#     newVersion = 0
#     for file in files:
#         file = file.replace("file_", "")
#         if int(file) > newVersion:
#             newVersion = int(file)
#     return newVersion

files = ["file_20", "file_2", "file_8", "file_70", "file_2", "gfy"]
# print(newFileVersion(files))

# files = ["gcvsbh"]
newFiles = []
if len(files) == 0:
    print(-1) 
else:
    for f in files:
        f = f.replace("file_", "")
        newFiles.append(f)
    maxx = 0
    for f in newFiles:
        if f.isdigit():
            if int(f) > maxx:
                maxx = int(f)
    print(maxx)