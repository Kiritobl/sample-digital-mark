from cv2 import imread
from cv2 import imwrite
import numpy as np

# 加载原始图像
img = imread("./my.png")

# 将水印信息转换为二进制数组
watermark = "what you are going to mask here"
watermark_binary = ''.join(format(ord(c), '08b') for c in watermark)
print(watermark_binary)
# 将LSB设置为0
img = np.bitwise_and(img, 254)

# 在LSB中嵌入水印
watermark_len = len(watermark_binary)
for i in range(watermark_len):
    if watermark_binary[i] == '1':
        img[i // 3, i % 3] |= 1

# 保存带有水印的图像
imwrite("watermarked_image.png", img)
