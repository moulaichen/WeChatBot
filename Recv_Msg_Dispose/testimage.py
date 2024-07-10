from PIL import Image
import imagehash


def is_same_image(image1_path, image2_path):
    # 打开图像
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # 计算图像的哈希值
    hash1 = imagehash.phash(image1)
    hash2 = imagehash.phash(image2)

    # 比较哈希值，允许一定的误差
    return hash1 - hash2 == 0


# 示例用法
image1_path = 'D:/APP/PyCharmWorkSpace/WeChatBot/Cache/Pic_Cache/85d2c0e44b934d8e17cbdb9acea0d0c.jpg'
image2_path = 'D:/APP/PyCharmWorkSpace/WeChatBot/Cache/Pic_Cache/2c1531186ec1f4e61496d19ddb4d9b0.jpg'
print(is_same_image(image1_path, image2_path))
