
# pip install matplotlib
# pip install opencv-python
# pip install glob2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.pylab as plt
import glob
import cv2

cat_files = glob.glob("cats/*.jpeg")
# print(cat_files)

img_mpl = plt.imread(cat_files[4])
img_cv2 = cv2.imread(cat_files[0])

# plt.imsave(blurred)
# cv2.imwrite(blurred)

# print(type(img_mpl), type(img_cv2)) # numpy.ndarray
# print(img_mpl.shape, img_cv2.shape) # (360, 543, 3) (360, 543, 3)
# print(img_mpl.dtype, img_cv2.dtype) # uint8 uint8
# print(img_mpl.max()) # 255
# print(img_mpl.flatten())

# img_cv2.resize(img_cv2, (1000, 1000), interpolation=cv2.INTER_CUBIC)
# img_cv2.resize(img_cv2, None, fx=0.25, fy=0.25)

# pd.Series(img_mpl.flatten()).plot(kind='hist', bins=50, title='Distribution of Pixel Values')

# Display image
# fig, ax = plt.subplots(figsize=(5,5))
# ax.imshow(img_mpl)
# ax.axis('off')

# # Display RGB channels
# fig, ax = plt.subplots(1, 3, figsize=(10, 5))
# ax[0].imshow(img_mpl[...,0], cmap="Reds")
# ax[1].imshow(img_mpl[:,:,1], cmap="Greens")
# ax[2].imshow(img_mpl[:,:,2], cmap="Blues")
# ax[0].set_title('reds')
# ax[0].axis('off')
# ax[1].set_title('greens')
# ax[1].axis('off')
# ax[2].set_title('blues')
# ax[2].axis('off')
# plt.show()

# CV2 reads as BGR
# PLT reads as RGB
# Convert from BGR to RGB
# img_cv2_rgb = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)
# img_cv2_rgb = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2GRAY)
# fig, ax = plt.subplots(1, 2)
# ax[0].imshow(img_cv2)
# ax[1].imshow(img_cv2_rgb)
# ax[0].axis('off')
# ax[1].axis('off')

# Sharpen Image
# kernel_sharpen = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
# sharpened = cv2.filter2D(img_cv2, -1, kernel_sharpen)
# fix, ax = plt.subplots(figsize=(8, 8))
# ax.imshow(sharpened)
# ax.axis('off')
# ax.set_title('Sharpened Image')

# Blur Image
kernel_3x3 = np.ones((3, 3), np.float32) / 9
blurred = cv2.filter2D(img_cv2, -1, kernel_3x3)
fix, ax = plt.subplots(figsize=(8, 8))
ax.imshow(blurred)
ax.axis('off')
ax.set_title('Blurred Image')


# plt.imsave(blurred)
# cv2.imwrite(blurred)

plt.show()


print("done")