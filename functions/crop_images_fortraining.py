import cv2
import os
import random


# Function for converting coordinates to absolute coordinates
def convert_coords (coords, img_size):
    _, x_center, y_center, w_norm, h_norm = map(float, coords)
    w_abs = w_norm * img_size[0]
    h_abs = h_norm * img_size[1]
    x_abs = (x_center * img_size[0]) - (w_abs / 2)
    y_abs = (y_center * img_size[1]) - (h_abs / 2)
    return int(x_abs), int(y_abs), int(w_abs), int(h_abs)


# Function for calculating new coordinates relative to the original coordinates
def calculate_new_coords (x, y, w, h, x_min, y_min, img_size):
    x_new_center = x + (w / 2) - x_min
    y_new_center = y + (h / 2) - y_min
    w_new = w
    h_new = h
    # Convert back
    x_new_norm = x_new_center / img_size[0]
    y_new_norm = y_new_center / img_size[1]
    w_new_norm = w_new / img_size[0]
    h_new_norm = h_new / img_size[1]
    return x_new_norm, y_new_norm, w_new_norm, h_new_norm


# Function for writing new coordinates to a txt file
def write_new_coords (new_coords, crop_path):
    txt_filename = crop_path.replace('.jpg', '.txt')
    with open(txt_filename, 'w') as f:
        f.write(' '.join(map(str, new_coords)))


# Function to cut images with different indentations for each marked zone
def crop_images_with_padding (img_path, coords_list, output_folder, img_size, padding_range=(10, 30)):
    img = cv2.imread(img_path)

    for i, line in enumerate(coords_list):
        coords = line.split(' ')
        x, y, w, h = convert_coords(coords, img_size)
        # Cut three images with different indentations for each zone
        for j in range(3):
            padding_x = random.randint(*padding_range)
            padding_y = random.randint(*padding_range)

            shift_x = random.randint(-padding_x // 2, padding_x // 2)
            shift_y = random.randint(-padding_y // 2, padding_y // 2)

            x_min = max(x - padding_x + shift_x, 0)
            y_min = max(y - padding_y + shift_y, 0)
            x_max = min(x + w + padding_x + shift_x, img_size[0])
            y_max = min(y + h + padding_y + shift_y, img_size[1])

            crop_img = img[y_min:y_max, x_min:x_max]

            crop_path = os.path.join(output_folder, f'crop_{i}_{j}_{os.path.basename(img_path)}')
            cv2.imwrite(crop_path, crop_img)

            # Calculate new coordinates for the cut image
            new_img_size = (x_max - x_min, y_max - y_min)
            new_coords = calculate_new_coords(x, y, w, h, x_min, y_min, new_img_size)

            # Save the new coordinates to a txt file
            write_new_coords(new_coords, crop_path)

# Example of how to use the function:
# img_size = (,)
# img_folder = ''
# coords_list = []
# output_folder = ''
# padding_range = (,)

# for filename in os.listdir(img_folder):
# if filename.endswith('.jpg'):
# img_path = os.path.join(img_folder, filename)
# crop_images_with_padding(img_path, coords_list, output_folder, img_size, padding_range)
