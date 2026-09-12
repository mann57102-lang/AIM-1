import cv2

# Load the pre-trained Haar Cascade Classifier for detecting faces
detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Start video capture from the default webcam (0)
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Unable to access camera.")
    exit()

while True:
    # Capture a frame from the webcam
    success, image = camera.read()

    # Check whether the frame was captured successfully
    if not success:
        print("Error: Could not capture frame")
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    detected_faces = detector.detectMultiScale(
        gray_frame,
        scaleFactor=1.2,
        minNeighbors=6,
        minSize=(40, 40)
    )

    # Draw rectangles around detected faces
    for (left, top, width, height) in detected_faces:
        cv2.rectangle(
            image,
            (left, top),
            (left + width, top + height),
            (0, 255, 0),
            2
        )  # Green rectangle with thickness 2

    # Display the processed frame
    cv2.imshow('Live Face Detector - Press e to Exit', image)

    # Exit when the 'e' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

# Release the webcam and close all windows
camera.release()
cv2.destroyAllWindows()
