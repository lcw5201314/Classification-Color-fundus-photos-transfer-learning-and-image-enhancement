import cv2
import os
from PIL import Image
import matplotlib.pyplot as plt

image_size = 224  # 设定尺寸
source_path = "./2Jan/1/"  # 源文件路径
#target_path = "./1/rotate45/"  # 输出目标文件路径
#target_path = "./1/rotate90/"  # 输出目标文件路径
#target_path = "./1/rotate135/"  # 输出目标文件路径
#target_path = "./1/rotate225/"  # 输出目标文件路径
#target_path = "./1/rotate270/"  # 输出目标文件路径
target_path = "./2Jan/1_G_Channel/"

if not os.path.exists(target_path):
    os.makedirs(target_path)

image_list = os.listdir(source_path)  # 获得文件名

i = 0
for file in image_list:
    i = i + 1
    #RGB = Image.open(source_path + file)
    RGB = cv2.imread(source_path + file, -1)  # 传入一张彩色图片
    b, g, r = cv2.split(RGB)  # 分离颜色通道
    #image_source = cv2.imread(source_path + file)  # 读取图片
    #im2 = image.rotate(270)
    #g.save(target_path+file)  # 重命名并且保存
    cv2.imwrite(target_path+file, g)  # 保存蓝色RGB图像
print("批量处理完成")