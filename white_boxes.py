import cv2
import numpy as np
import os

# Inpaints small white and black areas from images, saves the modified image.
def inpaint_areas(image_path, output_path, white_threshold=200, black_threshold=25, min_area=200, inpaint_radius=7):
    # Read image from file
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error loading image: {image_path}")
        return

    # Thresholding to create masks for inpainting
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, white_thresh = cv2.threshold(gray, white_threshold, 255, cv2.THRESH_BINARY)
    _, black_thresh = cv2.threshold(gray, black_threshold, 255, cv2.THRESH_BINARY_INV)
    combined_mask = cv2.bitwise_or(white_thresh, black_thresh)

    # Find and fill contours larger than min_area
    contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros_like(gray)
    for cnt in contours:
        if cv2.contourArea(cnt) > min_area:
            cv2.drawContours(mask, [cnt], -1, 255, thickness=cv2.FILLED)
    
    # Inpainting and saving the result
    mask = cv2.GaussianBlur(mask, (inpaint_radius, inpaint_radius), 0)
    inpainted_image = cv2.inpaint(image, mask, inpaint_radius, flags=cv2.INPAINT_TELEA)
    cv2.imwrite(output_path, inpainted_image)

# Processes each image in the source directory, applying inpainting and saving to the destination directory.
def process_directory(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for subdir, dirs, files in os.walk(source_dir):
        for img_file in files:
            if img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(subdir, img_file)
                relative_path = os.path.relpath(subdir, source_dir)
                class_output_dir = os.path.join(dest_dir, relative_path)
                if not os.path.exists(class_output_dir):
                    os.makedirs(class_output_dir)
                output_path = os.path.join(class_output_dir, img_file)
                inpaint_areas(img_path, output_path)

source_dir = 'C:/Users/antos/Desktop/fixing_image/white_boxes'#set the root where the images are divided for class folders
dest_dir = 'C:/Users/antos/Desktop/fixing_image/white_boxes_fixed'#create a folder where images are fixed and divided for class folders
process_directory(source_dir, dest_dir)