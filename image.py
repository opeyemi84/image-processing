from PIL import Image, ImageFilter

with Image.open('./Images/pikachu.jpg') as img:
# filtered_img = img.filter(ImageFilter.BLUR)
    filtered_img = img.convert('L')

filtered_img.save("grey.png", 'png')

with Image.open('./Images/squirtle.jpg') as nimg:
    grey_img = nimg.convert('L')

resize = grey_img.resize((300,300))
resize.save("ngrey.png", 'png')
# resize.show()