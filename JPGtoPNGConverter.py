import sys 
import os
from PIL import Image

# Step 1: grab the first and second argument 
# (first, the image folder that has the jpg and secondly the new folder to store the converted files)
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)


# Step 2: check if new folder exists, if not create it so as to store the new image files

# Step 3: loop through the image folder
# covert the images in the folder to png
# save converted images to the new folder created