import cv2
import numpy as np
import matplotlib.pyplot as plt

photo = cv2.imread('sample.jpg')
photo_rgb = cv2.cvtColor(photo, cv2.COLOR_BGR2RGB)

# Rotate the image by 30 degrees around its center
(height, width) = photo.shape[:2]
middle = (width//2, height//2)
rotation_matrix = cv2.getRotationMatrix2D(middle, 30, 1.0)    # rotate by 30 degrees
rotated_photo = cv2.warpAffine(photo, rotation_matrix, (width, height))

rotated_rgb = cv2.cvtColor(rotated_photo, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated Photo")
plt.show()

# Increase brightness by adding 70 to all pixel values
# Use cv2.add to avoid negative values or overflow
light_matrix = np.ones(photo.shape, dtype="uint8") * 70
bright_photo = cv2.add(photo, light_matrix)

bright_rgb = cv2.cvtColor(bright_photo, cv2.COLOR_BGR2RGB)
plt.imshow(bright_rgb)
plt.title("Brightened Photo")
plt.show()
