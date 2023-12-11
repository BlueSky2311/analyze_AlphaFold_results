import os
import shutil
import re

def get_subfolders(input_folder, output_folder):
    # create an empty list to store the subfolder names
    subfolders = []
    # loop through all the files and directories in the input folder
    for entry in os.scandir(input_folder):
        # check if the entry is a directory
        if entry.is_dir():
            # check if the output folder is a subfolder of the input folder
            if os.path.commonprefix([input_folder, output_folder]) == input_folder:
                # check if the entry is the same as the output folder
                if os.path.samefile(entry.path, output_folder):
                    # skip the output folder
                    continue
            # append the entry name to the subfolder list
            subfolders.append(entry.name)
    # return the subfolder list
    return subfolders

# specify the input folder path
input_folder = r"C:\Users\darkh\Desktop\test"
# specify the output folder path
output_folder = r"C:\Users\darkh\Desktop\test\output"
# get the subfolders from the input folder
subfolders = get_subfolders(input_folder, output_folder)

# loop through each subfolder
for subfolder in subfolders:
    # join the input folder and the subfolder name to get the full path
    subfolder_path = os.path.join(input_folder, subfolder)
    # loop through all the files in the subfolder
    for file in os.listdir(subfolder_path):
        # check if the file has the .pdb extension
        if file.endswith(".pdb"):
            # join the subfolder path and the file name to get the full file path
            file_path = os.path.join(subfolder_path, file)
            # copy the file to the output folder
            shutil.copy(file_path, output_folder)
# get the list of files in the output folder
output_files = os.listdir(output_folder)
# define the pattern to match the file names
pattern = ".*_rank_001_.*"
# loop through the output files
for file in output_files:
    # check if the file name does not match the pattern
    if not re.search(pattern, file):
        # join the output folder and the file name to get the full file path
        file_path = os.path.join(output_folder, file)
        # delete the file
        os.remove(file_path)
