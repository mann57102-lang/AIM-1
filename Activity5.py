import cv2
import matplotlib.pyplot as plt

# Step 1: Load the Image
photo_path = 'sample.jpg'  # User-provided image path
photo = cv2.imread(photo_path)

# Convert BGR to RGB for correct color display with matplotlib
photo_rgb = cv2.cvtColor(photo, cv2.COLOR_BGR2RGB)

# Get image dimensions
img_height, img_width, _ = photo_rgb.shape

# Step 2: Draw Two Rectangles Around Interesting Regions
# Rectangle 1: Top-left corner
box1_width, box1_height = 120, 120
corner1 = (30, 30)  # Fixed 30 pixels padding from top-left
end1 = (corner1[0] + box1_width, corner1[1] + box1_height)
cv2.rectangle(photo_rgb, corner1, end1, (255, 255, 0), 3)  # Yellow rectangle

# Rectangle 2: Bottom-right corner
box2_width, box2_height = 180, 120
corner2 = (img_width - box2_width - 30, img_height - box2_height - 30)
end2 = (corner2[0] + box2_width, corner2[1] + box2_height)
cv2.rectangle(photo_rgb, corner2, end2, (255, 0, 255), 3)  # Magenta rectangle

# Step 3: Draw Circles at the Centers of Both Rectangles
point1_x = corner1[0] + box1_width // 2
point1_y = corner1[1] + box1_height // 2
point2_x = corner2[0] + box2_width // 2
point2_y = corner2[1] + box2_height // 2

cv2.circle(photo_rgb, (point1_x, point1_y), 12, (0, 255, 0), -1)  # Filled green circle
cv2.circle(photo_rgb, (point2_x, point2_y), 12, (0, 255, 0), -1)  # Filled green circle

# Step 4: Draw Connecting Lines Between Centers of Rectangles
cv2.line(photo_rgb, (point1_x, point1_y), (point2_x, point2_y), (0, 255, 0), 3)

# Step 5: Add Text Labels for Regions and Centers
text_font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(photo_rgb, 'Area 1',
            (corner1[0], corner1[1] - 10),
            text_font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

cv2.putText(photo_rgb, 'Area 2',
            (corner2[0], corner2[1] - 10),
            text_font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

cv2.putText(photo_rgb, 'Point 1',
            (point1_x - 40, point1_y + 35),
            text_font, 0.6, (0, 255, 0), 2, cv2.LINE_AA)

cv2.putText(photo_rgb, 'Point 2',
            (point2_x - 40, point2_y + 35),
            text_font, 0.6, (0, 255, 0), 2, cv2.LINE_AA)

# Step 6: Add Bi-Directional Arrow Representing Height
arrow_start = (img_width - 40, 30)  # Start near the top-right
arrow_end = (img_width - 40, img_height - 30)  # End near the bottom-right

# Draw arrows in both directions
cv2.arrowedLine(photo_rgb, arrow_start, arrow_end,
                (255, 255, 0), 3, tipLength=0.05)  # Downward arrow

cv2.arrowedLine(photo_rgb, arrow_end, arrow_start,
                (255, 255, 0), 3, tipLength=0.05)  # Upward arrow

# Annotate the height value
height_text_pos = (arrow_start[0] - 140,
                   (arrow_start[1] + arrow_end[1]) // 2)

cv2.putText(photo_rgb, f'Image Height: {img_height}px',
            height_text_pos, text_font, 0.8,
            (255, 255, 0), 2, cv2.LINE_AA)

# Step 7: Display the Annotated Image
plt.figure(figsize=(10, 7))
plt.imshow(photo_rgb)
plt.title('Image with Areas, Points and Height Arrow')
plt.axis('off')
plt.show()
