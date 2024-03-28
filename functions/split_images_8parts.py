from PIL import Image
import os


# Code to cut the image into 8 parts in two rows
def split_image_into_parts (folder_path, parts_folder, rows, cols):
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            img_path = os.path.join(folder_path, filename)
            with Image.open(img_path) as img:
                width, height = img.size
                part_width = width // cols
                part_height = height // rows

                for row in range(rows):
                    for col in range(cols):
                        left = col * part_width
                        upper = row * part_height
                        right = left + part_width
                        lower = upper + part_height

                        part = img.crop((left, upper, right, lower))
                        part_filename = f'{filename}___part_{row}_{col}.jpg'
                        part.save(os.path.join(parts_folder, part_filename))

# Example of how to use the function:
# folder_path = ''
# parts_folder = ''
# rows = 2
# cols = 4

# split_image_into_parts(folder_path, parts_folder, rows, cols)
