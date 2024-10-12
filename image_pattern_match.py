import cv2
import os

# Path to the directory containing the database images
database_dir = 'Image_Pattern_Gallery'

# Load the pattern image
pattern_img = cv2.imread('source_pattern_1.jpg', 0)

# Function to find the best match
def find_best_match(database_dir, pattern_img):
    best_match = None
    best_val = 0

    for image_name in os.listdir(database_dir):
        image_path = os.path.join(database_dir, image_name)
        img = cv2.imread(image_path, 0)

        # Ensure the image was loaded correctly
        if img is None:
            continue

        # Use matchTemplate to find the pattern in the current image
        result = cv2.matchTemplate(img, pattern_img, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        # Update the best match if the current one is better
        if max_val > best_val:
            best_val = max_val
            best_match = (image_name, max_loc)

    return best_match, best_val

# Find the best match
best_match, best_val = find_best_match(database_dir, pattern_img)

if best_match:
    print(f"Best match found in {best_match[0]} with a similarity score of {best_val}")
else:
    print("No match found")
