from PIL import Image
import os


# Function to cut a picture by 4 coordinates
def crop_images (folder_path, output_folder, crop_boxes, file_suffixes):
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            img_path = os.path.join(folder_path, filename)
            with Image.open(img_path) as img:
                cropped_img = None
                new_filename = None

                for suffix, crop_box in zip(file_suffixes, crop_boxes):
                    if suffix in filename:
                        cropped_img = img.crop(crop_box)
                        new_filename = filename.replace('.jpg', f'_cropped_{suffix}.jpg')
                        break

                if cropped_img is not None:
                    cropped_img_path = os.path.join(output_folder, new_filename)
                    cropped_img.save(cropped_img_path)

# Example of how to use the function:
# folder_path = ''
# output_folder = ''
# crop_boxes = [(), ()]
# file_suffixes = []

# crop_images(folder_path, output_folder, crop_boxes, file_suffixes)
