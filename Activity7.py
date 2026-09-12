import cv2
import numpy as np

def change_color(image, effect):
    """Apply the selected color effect to the image."""
    
    # Create a copy so the original image remains unchanged
    result_image = image.copy()

    if effect == "red_effect":
        # Remove blue and green channels for red effect
        result_image[:, :, 1] = 0  # Green channel to 0
        result_image[:, :, 0] = 0  # Blue channel to 0

    elif effect == "blue_effect":
        # Remove red and green channels for blue effect
        result_image[:, :, 1] = 0  # Green channel to 0
        result_image[:, :, 2] = 0  # Red channel to 0

    elif effect == "green_effect":
        # Remove blue and red channels for green effect
        result_image[:, :, 0] = 0  # Blue channel to 0
        result_image[:, :, 2] = 0  # Red channel to 0

    elif effect == "boost_red":
        # Increase the intensity of the red channel
        result_image[:, :, 2] = cv2.add(
            result_image[:, :, 2], 60
        )  # Increase red channel

    elif effect == "reduce_blue":
        # Decrease the intensity of the blue channel
        result_image[:, :, 0] = cv2.subtract(
            result_image[:, :, 0], 60
        )  # Decrease blue channel

    return result_image


# Load the image
photo_path = 'sample.jpg'  # Provide your image path
photo = cv2.imread(photo_path)

if photo is None:
    print("Error: Unable to find image!")
else:
    selected_effect = "original"  # Default effect

    print("Press the following keys to apply effects:")
    print("x - Red Effect")
    print("y - Blue Effect")
    print("z - Green Effect")
    print("u - Increase Red Intensity")
    print("v - Decrease Blue Intensity")
    print("e - Exit")

    while True:
        # Apply the selected effect
        output_image = change_color(photo, selected_effect)

        # Display the processed image
        cv2.imshow("Color Effect", output_image)

        # Wait for key press
        pressed_key = cv2.waitKey(0) & 0xFF

        # Map key presses to effects
        if pressed_key == ord('x'):
            selected_effect = "red_effect"

        elif pressed_key == ord('y'):
            selected_effect = "blue_effect"

        elif pressed_key == ord('z'):
            selected_effect = "green_effect"

        elif pressed_key == ord('u'):
            selected_effect = "boost_red"

        elif pressed_key == ord('v'):
            selected_effect = "reduce_blue"

        elif pressed_key == ord('e'):
            print("Closing program...")
            break

        else:
            print("Invalid key! Please use 'x', 'y', 'z', 'u', 'v', or 'e'.")


cv2.destroyAllWindows()
