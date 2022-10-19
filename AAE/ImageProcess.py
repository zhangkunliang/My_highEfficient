# -*- coding: utf-8 -*-
import os
import random
from PIL import Image
import numpy as np

path = r'D:\ProgramFiles\PycharmProject\Autogui\AAE\images'


# 在0~2**36内随机生成数据集
def generate(num):
    # 保存随机数
    data = []
    # 保存二进制数
    data_bin = []
    for i in range(0, num):
        ran = random.randint(0, 2 ** 36)
        data.append(ran)
        data_bin.append(bin(ran)[2:].zfill(36))
    print(data)
    print(data_bin)
    for index in range(0, num):
        if not os.path.exists(path + '/' + '(' + str(data[index]) + ')' + data_bin[index] + '.txt'):
            f = open(path + '/' + '(' + str(data[index]) + ')' + data_bin[index] + '.txt', 'w')
            # 写入矩阵
            for j in range(0, 6):  # 行数
                for k in range(0, 6):  # 列数
                    f.write(data_bin[index][j * 6 + k])
                    f.write(" ")
                # 下一行
                f.write('\n')
            f.close()


# generate(2000)


def readfile(filename):
    with open(filename, 'r') as f:
        list1 = []
        for line in f.readlines():
            line_str = line.strip()
            for element in line_str:
                if element != " ":
                    list1.append(int(element))
        return list1


if __name__ == '__main__':
    listdir = os.listdir(path)
    len_dir = len(os.listdir(path))
    print(listdir)
    for index in range(0, len_dir):
        list_result = readfile(path + '/' + listdir[index])
        # 测试的txt中，只有0和1，目标是把1显示为“黑色”，0显示为“白色”；
        # 所以将列表中的1替换为0，而0替换为255
        for i in range(0, len(list_result)):
            if list_result[i] == 1:
                list_result[i] = 0
            else:
                list_result[i] = 255
        # 再利用numpy将列表包装为数组
        array1 = np.array(list_result)
        # 进一步将array包装成矩阵
        data = np.matrix(array1)

        # print(data)
        # 重新reshape一个矩阵为一个方阵
        data = np.reshape(data, (6, 6))
        # 在一维上复制#个
        data = data.repeat(28, axis=0)
        # 在二维上复制#个
        data = data.repeat(28, axis=1)
        print(data)
        # 调用Image的formarray方法将矩阵数据转换为图像PIL类型的数据
        new_map = Image.fromarray(data.astype('uint8'))  # 不加上unit8则保存图片会出现全黑
        # 显示图像
        # new_map.show()
        new_map.save(path + '/' + listdir[index].split('.')[0] + '.png')
