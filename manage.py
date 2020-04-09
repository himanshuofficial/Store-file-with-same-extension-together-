from shutil import move,copytree
from tkinter import filedialog,Tk
from os import listdir,path,makedirs
root = Tk()
root.withdraw()
source = filedialog.askdirectory(title='Please select directory where all the random files are stored')
directories = listdir(source)
for files in directories:
   
    file,ext = path.splitext(files)
    ext = ext[1:]
    if ext == ' ':
        continue
    if path.exists(source+'/'+ext):
        
        move(source+'/'+files,source+'/'+ext+'/'+file)
    
    else:
        makedirs(source+'/'+ext)
        move(source+'/'+files,source+'/'+ext+'/'+file)
         
