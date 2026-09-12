import cv2


# Load the image

photo = cv2.imread('sample.jpg')


# Resize the window to a specific size without resizing the image

cv2.namedWindow('My Image', cv2.WINDOW_NORMAL)  # Create a resizable window

cv2.resizeWindow('My Image', 700, 450)  # Set the window size to 700x450


# Display the image in the resized window

cv2.imshow('My Image', photo)

cv2.waitKey(0)  # Wait for a key press

cv2.destroyAllWindows()  # Close the window


# Print image properties

print(f"Image Dimensions: {photo.shape}")  # Height, Width, Channels
