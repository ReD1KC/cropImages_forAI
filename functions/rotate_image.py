# Function for image rotation
def rotate_image(image, angle):
    (h, w) = image.shape[:2]

    center = (w / 2, h / 2)

    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated