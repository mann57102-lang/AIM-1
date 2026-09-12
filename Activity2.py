import cv2


# Load the image

photo = cv2.imread('sample.jpg')


# Convert the image to grayscale

gray_photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)


# Resize the grayscale image to 300x300

scaled_photo = cv2.resize(gray_photo, (300, 300))


# Display the resized grayscale image in a single window

cv2.imshow('Grayscale Photo', scaled_photo)


# Wait for a key press

pressed_key = cv2.waitKey(0)  # Wait indefinitely for a key press


# Check if the "S" key was pressed

if pressed_key == ord('s'):

    # Save the processed image when "S" is pressed

    cv2.imwrite('gray_scaled_photo.jpg', scaled_photo)

    print("Image saved as gray_scaled_photo.jpg")

else:

    print("Image not saved")


# Close the window

cv2.destroyAllWindows()


# Print processed image properties

print(f"Processed Image Dimensions: {scaled_photo.shape}")
