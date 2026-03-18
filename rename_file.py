#!/usr/bin/env python3
import subprocess, os

def to_str(n):

    if n < 10:
        retval=f"00{n}"
    elif n < 100:
        retval =f"0{n}"
    else:
        retval=f"{n}"
    return retval

# with open("file1.txt") as f1:
#     d1=f1.read()

result = subprocess.run(['ls', 'image'], capture_output=True, text=True, check=True)
d1 = result.stdout.split("\n")
# f1=open("rename_image.sh","w")
# f2=open("convert_to_cweb.sh","w")
#f3.open("crop_png.sh","w")
jpg_file=[]
# webp_file=[]
j = 1
for i in d1:
    if i:
        # rename_png=f"cp \"image/{i}\" new/page_{to_str(j)}.png\n"
        rename_png=f"magick convert \"image/{i}\" -crop  1529x1946+1393+254 new/page_{to_str(j)}.jpg"
        print(f"cropping file \"image/{i}\"")
        exit_status=os.system(rename_png)
        print(f"status {exit_status}")
        jpg_file.append(f"new/page_{to_str(j)}.jpg")
        #webp_file.append(f"webp/page_{to_str(j)}.webp")
        #convert_png=f"cwebp new/page_{to_str(j)}.jpg -o webp/page_{to_str(j)}.webp\n"
        j+=1
        #f1.write(rename_png)
        #f2.write(convert_png)
#f1.close()
# f2.close()
jpg = " ".join(jpg_file)
# webp = " ".join(webp_file)
print("converting image to pdf ")
print("running comannd")
a1=f"magick convert {jpg} result.pdf\n"
print(a1)
exit_status=os.system(a1)
print(f"status {exit_status}")
# with open("convert_to_pdf.sh","w") as f1:
#     a1=f"magick convert {jpg} result.pdf\n"
#     f1.write(a1)


