# Creating PDF from multiple screenshot image

This script is to create a PDF file from multiple screenshot images.

The script has been tested on Ubuntu Linux, MACOSX,  Windows 11 (using WSL) and Windows 11 (native)

# software required for this script to run (please install these before running the script)
- Python3
- ImageMagick
# Cropsize reference
This is the reference for CROPSIZE variable
![cropsize.jpg](./cropsize.jpg)
# Work flow
1. Determine the CROPSIZE, based on your system (Linux, Windows 11 or MACOSX) and screen resolution
2. Open the application and put it in fullscreen mode.
3. Do a screenshot: 
    - on Ubuntu Linux press ALT-PrtSCR
    - on MACOSX press SHIFT-COMMAND-3
    - on Windows 11 press WindowsKey-PrtScr
4. On the application, go the next page, then repeat step 3
5. repeat Step 3 - 4 until all pages are captured
6. Drop to shell/terminal, and run the script [create_pdf.py](./create_pdf.py)
7. File **result.pdf** is the output for the script.
8. Move file **result.pdf** to other directory and rename it.
9. Repeat 3 - 8 for the next pdf file.


# Caveat
- It is recommended to limit the number of pages per PDF below 100. if the page numbers are too big, the process of converting the images to pdf may fail


