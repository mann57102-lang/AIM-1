import cv2
import matplotlib.pyplot as plt

photo = cv2.imread('sample.jpg')

# Convert BGR to RGB
photo_rgb = cv2.cvtColor(photo, cv2.COLOR_BGR2RGB)
plt.imshow(photo_rgb)
plt.title("Original RGB Photo")
plt.show()

# Convert to Grayscale
gray_photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_photo, cmap='gray')
plt.title("Gray Scale Photo")
plt.show()

# Cropping the image
# Assume we know the region we want: rows 80 to 280, columns 150 to 350
cropped_photo = photo[80:280, 150:350]
cropped_rgb = cv2.cvtColor(cropped_photo, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Selected Cropped Area")
plt.show()
