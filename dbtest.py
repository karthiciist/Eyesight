from PIL import Image

im = Image.open(r"C:\Users\ET437GL\Pictures\pan.png")

fullwidth, fullheight = im.size
print(fullwidth)
print(fullheight)

left = 27 # xaxis
top = 126 # yaxis
right = 366 # (fullwidth) - (fullwidth - (width + xaxis))
bottom = 169 # (fullheight) - (fullheight - (height + yaxis))

im1 = im.crop((left, top, right, bottom))

im1.show()