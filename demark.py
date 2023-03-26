import cv2
import numpy as np

# 读取带有水印的图像
img = cv2.imread('watermarked_image.png', cv2.IMREAD_UNCHANGED)

# 提取水印信息
for watermark_len in range(1000):
    watermark_binary = ''
    for i in range(watermark_len):
        if np.any(img[i // 3, i % 3] & 1 == 1):
            watermark_binary += '1'
        else:
            watermark_binary += '0'

    # 将二进制字符串转换为水印文本
    watermark = ''
    for i in range(0, len(watermark_binary), 8):
        watermark += chr(int(watermark_binary[i:i+8], 2))

    print(watermark)
