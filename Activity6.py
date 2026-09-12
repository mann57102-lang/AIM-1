import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_photo(name, photo):
    """Utility function to display an image."""
    plt.figure(figsize=(7, 7))
    
    if len(photo.shape) == 2:  # Grayscale image
        plt.imshow(photo, cmap='gray')
    else:  # Color image
        plt.imshow(cv2.cvtColor(photo, cv2.COLOR_BGR2RGB))
    
    plt.title(name)
    plt.axis('off')
    plt.show()


def edge_filter_activity(photo_path):
    """Interactive activity for edge detection and filtering."""
    
    photo = cv2.imread(photo_path)
    
    if photo is None:
        print("Error: Unable to load image!")
        return

    # Convert to grayscale
    gray_photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    show_photo("Original Gray Photo", gray_photo)

    print("Choose an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")

    while True:
        option = input("Enter your choice (1-6): ")

        if option == "1":
            # Sobel Edge Detection
            sobel_horizontal = cv2.Sobel(
                gray_photo, cv2.CV_64F, 1, 0, ksize=3
            )
            
            sobel_vertical = cv2.Sobel(
                gray_photo, cv2.CV_64F, 0, 1, ksize=3
            )
            
            combined_edges = cv2.bitwise_or(
                sobel_horizontal.astype(np.uint8),
                sobel_vertical.astype(np.uint8)
            )
            
            show_photo("Sobel Edge Result", combined_edges)

        elif option == "2":
            # Canny Edge Detection
            print("Set thresholds for Canny (example: 80 and 180)")
            
            min_threshold = int(input("Enter Lower threshold: "))
            max_threshold = int(input("Enter Upper threshold: "))
            
            canny_edges = cv2.Canny(
                gray_photo,
                min_threshold,
                max_threshold
            )
            
            show_photo("Canny Edge Result", canny_edges)

        elif option == "3":
            # Laplacian Edge Detection
            laplacian_edges = cv2.Laplacian(
                gray_photo,
                cv2.CV_64F
            )
            
            show_photo(
                "Laplacian Edge Result",
                np.abs(laplacian_edges).astype(np.uint8)
            )

        elif option == "4":
            # Gaussian Smoothing
            print("Enter an odd kernel size for Gaussian blur (example: 7)")
            
            blur_size = int(input("Enter kernel size (odd number): "))
            
            smooth_photo = cv2.GaussianBlur(
                photo,
                (blur_size, blur_size),
                0
            )
            
            show_photo("Gaussian Smooth Result", smooth_photo)

        elif option == "5":
            # Median Filtering
            print("Enter an odd kernel size for Median filtering (example: 7)")
            
            filter_size = int(input("Enter kernel size (odd number): "))
            
            median_photo = cv2.medianBlur(
                photo,
                filter_size
            )
            
            show_photo("Median Filter Result", median_photo)

        elif option == "6":
            # Exit
            print("Program closed...")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 6.")


# Provide the path to an image for the activity
edge_filter_activity('sample.jpg')
