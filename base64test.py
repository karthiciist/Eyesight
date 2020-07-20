import base64
import io
import cv2
from imageio import imread
import matplotlib.pyplot as plt

with open("test.txt", "rb") as kid:
    teststring = kid.read()

test_string = teststring.decode()

print(type(test_string))

# reconstruct image as an numpy array
img = imread(io.BytesIO(base64.b64decode(test_string)))

# show image
plt.figure()
plt.imshow(img, cmap="gray")

# finally convert RGB image to BGR for opencv
# and save result
cv2_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imwrite("reconstructed.jpg", cv2_img)
plt.show()







































# import base64
# import io
# import cv2
# from imageio import imread
# import matplotlib.pyplot as plt
#
# filename = "pannum.png"
# with open(filename, "rb") as fid:
#     data = fid.read()
#
# b64_bytes = base64.b64encode(data)
#
# with open("test.txt", "rb") as kid:
#     teststring = kid.read()
#
# #mainstring = str(teststring)
#
# #print(mainstring)
#
# test_string = teststring.decode()
# b64_string = b64_bytes.decode()
#
#
#
# print(test_string)
#
# # reconstruct image as an numpy array
# img = imread(io.BytesIO(base64.b64decode(test_string)))
#
# # show image
# plt.figure()
# plt.imshow(img, cmap="gray")
#
# # finally convert RGB image to BGR for opencv
# # and save result
# cv2_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# cv2.imwrite("reconstructed.jpg", cv2_img)
# plt.show()