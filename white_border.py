import cv2
import numpy as np
import os

def crop_white_borders(image_path, output_path):
    # Read the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Error loading image: {image_path}")
        return
    
    # Invert the image to make the white borders black
    inverted_image = cv2.bitwise_not(image)

    # Apply Otsu's thresholding to the inverted image
    blur = cv2.GaussianBlur(inverted_image, (5, 5), 0)
    _, binary_image = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Assuming the largest contour is the main content area of the X-ray
    if contours:
        # Find the largest contour with respect to area, but it should also have a significant size
        largest_contour = max(contours, key=lambda x: cv2.contourArea(x) if cv2.contourArea(x) > 10000 else 0)
        x, y, w, h = cv2.boundingRect(largest_contour)

        # Crop the original image using the bounding rectangle of the largest contour
        cropped_image = image[y:y+h, x:x+w]
        cv2.imwrite(output_path, cropped_image)
        print(f"Cropped image saved to {output_path}")
    else:
        print(f"No significant contours found in image {image_path}")

def process_images_in_folders(source_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    # Walk through all files in the directory that contains the subdirectories
    for subdir, dirs, files in os.walk(source_folder):
        for img_file in files:
            img_path = os.path.join(subdir, img_file)
            relative_path = os.path.relpath(subdir, source_folder)
            class_output_dir = os.path.join(dest_folder, relative_path)
            if not os.path.exists(class_output_dir):
                os.makedirs(class_output_dir)
            output_path = os.path.join(class_output_dir, img_file)
            
            if img_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                crop_white_borders(img_path, output_path)

source_folder = 'C:/Users/antos/Desktop/fixing_image/white_borders'  #set the root where the images are divided for class folders
dest_folder = 'C:/Users/antos/Desktop/fixing_image/white_border_fixed' #create a folder where images are fixed and divided for class folders
process_images_in_folders(source_folder, dest_folder)