import os
import shutil

textfolder = f'{os.getcwd()}/labels'
imgfolder = f'{os.getcwd()}/bicycle-lane-brimbank-data-6k'

final = f'{os.getcwd()}/detected-images'

file_text = os.listdir(textfolder)

file_jpeg = os.listdir(imgfolder)

for i in file_jpeg:
  for j in file_text:
    if (i[:-4] == j[:-4]):
      #checking if the file already exists
      if (not (os.path.exists(f'{final}/{j[:-4]}.jpg'))):
        shutil.copy2(f'{imgfolder}/{i}', final)

# for file in os.listdir(final):
#   new_name = f'{final}/{file[:-4]}.jpg'
#   os.rename(f'{final}/{file}', new_name)