import cv2
import numpy as np

def maximize_channels(image_path, output_path):
    # Read Image
    image = cv2.imread(image_path)
    if image is None:
        print("Image not found")
        return

    # Convert to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Background Color Range
    ## blue
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])

    # Create mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # mask processing
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=1)
    mask = cv2.GaussianBlur(mask, (7, 7), 0)

    # Find max of RGB channels and apply it to all channnels
    max_channel = np.max(image, axis=2)
    image[:, :, 0] = np.where(mask > 0, max_channel, image[:, :, 0])
    image[:, :, 1] = np.where(mask > 0, max_channel, image[:, :, 1])
    image[:, :, 2] = np.where(mask > 0, max_channel, image[:, :, 2])

    # Save
    cv2.imwrite(output_path, image)
    print("Image saved to", output_path)

# 调用函数
maximize_channels("path_to_your_image.jpg", "output_image.jpg")
