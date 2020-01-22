import os
targetdir = r"D:\mobilebackup\Rainyfull\videos"

if os.path.isdir(targetdir):
    listfile = os.listdir(targetdir)
    print(listfile)
else:
    print('targetdir is not a dir')