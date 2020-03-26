from shutil import move,copytree
from tkinter import filedialog
from os import listdir,path,makedirs
print("Select the path of folder where all mixed files are stored")
source = filedialog.askdirectory()
directories = listdir(source)
# destination = filedialog.askdirectory()
for files in directories:
   
    file,ext = path.splitext(files)
    print(file,ext)
    if ext == ' ':
        continue
    if path.exists(source+'/'+ext):
        
        move(source+'/'+files,source+'/'+ext+'/'+file)
    
    else:
        makedirs(source+'/'+ext)
        move(source+'/'+files,source+'/'+ext+'/'+file)
         
