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
# image1_path = 'D:/WeChatBot/Cache/All_Image_Qun_Cache/1f9aa4b85ad74b565533a1252b5b326b.jpg'
# image2_path = 'D:/WeChatBot/Cache/All_Image_Qun_Cache/494877686b9a2f92c9da78ce4734e864.jpg'
# print(is_same_image(image1_path, image2_path))
