#!/usr/bin/env python3
import subprocess, os, shutil

# edit the following variable based on the system
# CROPSIZE="AxB+C+D"
# AxB : pixel size of the crop area, A = horizontal pixel, B = vertical pixel
# C : horizontal distance for left edge of the screen
# D : vertical distance from top edge of the screen
# cropsize for MacOSX, screensize 1800x1169
CROPSIZE="1700x1950+936+247"
SOURCEDIR="/Users/irzan/Desktop"
# for windows 11
# cropsize for Windows 11, screensize 2880x1800
# SOURCEDIR="/mnt/c/Users/irzan/OneDrive/Pictures/Screenshots"
# CROPSIZE="1360x1760+755+22"

IMAGEDIR = "image"
NEWIMAGEDIR = "new"
if not os.path.exists(IMAGEDIR):
    os.makedirs(IMAGEDIR)
if not os.path.exists(NEWIMAGEDIR):
    os.makedirs(NEWIMAGEDIR)

files = [ i for i in os.listdir(SOURCEDIR) if "Screenshot" in i]
# print(files)
for i in files:
    source1 = os.path.join(SOURCEDIR,i)
    print(f"moving {source1}")
    if os.path.isfile(source1):
        shutil.move(source1,IMAGEDIR)


result = subprocess.run(['ls', IMAGEDIR], capture_output=True, text=True, check=True)
# d1 = [int(i.removeprefix('Screenshot (').removesuffix(').png')) if i else 0 for i in result.stdout.split("\n")]
d1 = [i if i else 0 for i in result.stdout.split("\n")]
print(d1)
p = 1
list_of_pages = []
# d1.sort()
for i in d1:
    if  i:
        #print(f"value if i {i}")
        page_name = f"page_{p}.jpg"
        list_of_pages.append(f"{NEWIMAGEDIR}/{page_name}")
        p+=1
        source = f"\"{IMAGEDIR}/{i}\""
        dest = f"{NEWIMAGEDIR}/{page_name}"
        cmd1 = f"convert {source} -crop {CROPSIZE} {dest}"
        # cmd1 = f"magick {source} -crop {CROPSIZE} {dest}"
        print(f"running {cmd1}")
        exit_status = os.system(cmd1)
        print(f"exit status {exit_status}")
lp = " ".join(list_of_pages)
# print(lp)
cmd1 = f"convert {lp} result.pdf"
# cmd1 = f"magick {lp} result.pdf"
print("creating pdf")
exit_status=os.system(cmd1)
print(f"exit status {exit_status}")
shutil.rmtree(IMAGEDIR)
shutil.rmtree(NEWIMAGEDIR)