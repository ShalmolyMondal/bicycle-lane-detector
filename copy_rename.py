import os
import shutil

# src = r'/Users/shalmolymondal/MyProjects/5GRProject/ozstar/bicycle-marking-detector/brimbank-data/'
# dest = r'/Users/shalmolymondal/MyProjects/5GRProject/ozstar/bicycle-marking-detector/bicycle-lane-brimbank-data-v1'

source = f'{os.getcwd()}/brimbank-data'
dest = f'{os.getcwd()}/bicycle-lane-brimbank-data-v1'
folders = os.listdir(source)

for folder in folders:
  inner_directory = f'{source}/{folder}'

  if (os.path.isdir(inner_directory) == True):
    for file in os.listdir(inner_directory):
      old_name = f'{source}/{folder}/{file}'
      new_name = f'{source}/{folder}/{folder}_{file}'
      os.rename(old_name, new_name)
      shutil.copy(new_name, dest)

# def rename(name,loc):

# for path, subdirs, files in os.walk(src):
#   for name in files:
#     filename = os.path.join(path, name)
#     shutil.copy2(filename, dest)

# print("Files Copied")
