import cv2
import numpy as np

def maximize_channels(image_path, output_path):
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        print("Image not found")
        return

    # 转换到HSV色彩空间
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定义蓝色的范围
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])

    # 创建掩码以只获取蓝色区域
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 对掩码进行膨胀和腐蚀操作，平滑边缘
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=1)

    # 使用高斯模糊对掩码边缘进行平滑
    mask = cv2.GaussianBlur(mask, (7, 7), 0)

    # 找到每个像素RGB通道的最大值，并将其应用到所有通道
    max_channel = np.max(image, axis=2)
    image[:, :, 0] = np.where(mask > 0, max_channel, image[:, :, 0])
    image[:, :, 1] = np.where(mask > 0, max_channel, image[:, :, 1])
    image[:, :, 2] = np.where(mask > 0, max_channel, image[:, :, 2])

    # 保存修改后的图像
    cv2.imwrite(output_path, image)
    print("Image saved to", output_path)

# 调用函数
maximize_channels("/Users/binciluo/Downloads/IMG_0090.jpg", "output_image.jpg")
