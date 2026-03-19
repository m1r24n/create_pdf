#!/usr/bin/env python3
import subprocess, os, shutil, platform

# edit the following variable based on the system
# CROPSIZE="AxB+C+D"
# AxB : pixel size of the crop area, A = horizontal pixel, B = vertical pixel
# C : horizontal distance for left edge of the screen
# D : vertical distance from top edge of the screen

# change this accordingly
# cropsize for Ubuntu Linux, screensize 2880x1800
CROPSIZE="1890x2138+1423+115"

# cropsize for MacOSX, screensize 1800x1169
# CROPSIZE="1610x1950+1350+245"

# cropsize for Windows 11, screensize 2880x1800
# CROPSIZE="1360x1760+755+22"

IMAGEDIR = "image"
NEWIMAGEDIR = "new"
# UserName=os.environ['USERNAME']
w_stat = 0
UserName=""

OperatingSystem = platform.system().lower()
if OperatingSystem == "linux": 
  UserName=os.environ['USER']
  if "microsoft" in platform.uname().release.lower(): 
    SOURCEDIR=f"/mnt/c/Users/{UserName}/OneDrive/Pictures/Screenshots"
  else:
    SOURCEDIR=f"/home/{UserName}/Pictures/Screenshots"
elif OperatingSystem == "darwin": 
  UserName=os.environ['USER']
  SOURCEDIR=f"/Users/{UserName}/Desktop"
elif OperatingSystem == "windows": 
  UserName=os.environ['USERNAME']
  SOURCEDIR=f"c:/Users/{UserName}/OneDrive/Pictures/Screenshots"
  w_stat = 1

# UserName=os.environ['USERNAME'] if w_stat else os.environ['USER']
   

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


# result = subprocess.run(['ls', IMAGEDIR], capture_output=True, text=True, check=True)
# d1 = [int(i.removeprefix('Screenshot (').removesuffix(').png')) if i else 0 for i in result.stdout.split("\n")]
# d1 = [i if i else 0 for i in result.stdout.split("\n")]
# print(d1)
d1 = os.listdir(IMAGEDIR) 
d1.sort()
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
        cmd1 = f"magick.exe {source} -crop {CROPSIZE} {dest}" if w_stat else f"convert {source} -crop {CROPSIZE} {dest}"
        # cmd1 = f"convert {source} -crop {CROPSIZE} {dest}"
        # cmd1 = f"magick {source} -crop {CROPSIZE} {dest}"
        print(f"running {cmd1}")
        exit_status = os.system(cmd1)
        print(f"exit status {exit_status}")
lp = " ".join(list_of_pages)
# print(lp)
cmd1 =  f"magick.exe {lp} result.pdf" if w_stat else f"convert {lp} result.pdf"
# cmd1 = f"magick {lp} result.pdf"
print("creating pdf")
exit_status=os.system(cmd1)
print(f"exit status {exit_status}")
shutil.rmtree(IMAGEDIR)
shutil.rmtree(NEWIMAGEDIR)
