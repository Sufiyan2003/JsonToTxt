import os


# This is to remove any file extension in case you want to use it for any type of file
# if you want to filter out files of different types then you will need to edit this code
def RemoveFileExtension(FileName):
    position = FileName.find('.')
    OnlyFileName = FileName[:position]
    return OnlyFileName


def RemoveFileExtensionForArray(FileArray):
    for i in range(len(FileArray)):
        FileArray[i] = RemoveFileExtension(FileArray[i])
    return FileArray

# this path contains the bigger set of files which we need to filter
path = "path/to/target"

# this contais the files that are to remain
to_remain = "path/to/lookup"


# need to check if the name is present in that file or not
target_files = RemoveFileExtensionForArray(os.listdir(path))
lookup_files = RemoveFileExtensionForArray(os.listdir(to_remain))

for i in range(len(target_files)):
    check_file = (target_files[i])
    print(check_file)
    if check_file not in lookup_files:
        path_to_file = os.path.join(path, check_file)
        os.remove(path_to_file)
