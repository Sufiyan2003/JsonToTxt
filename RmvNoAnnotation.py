import os


# this path contains the bigger set of files which we need to filter
path = "C:/Users/RA/Desktop/python/target"

# this contais the files that are to remain
to_remain = "C:/Users/RA/Desktop/python/lookup"


# need to check if the name is present in that file or not
target_files = os.listdir(path)
lookup_files = os.listdir(to_remain)

for i in range(len(target_files)):
    check_file = target_files[i]
    print(check_file)
    if check_file not in lookup_files:
        path_to_file = os.path.join(path, check_file)
        os.remove(path_to_file)