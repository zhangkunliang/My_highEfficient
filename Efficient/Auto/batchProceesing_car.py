import numpy as np
import pandas as pd
import os  # 导入模块

path = r'E:\Study\pe-pp\Sequence_num'
test_path = r'E:\Study\pe-pp\test'


def to_bin(value, num):  # 十进制数据，二进制位宽
    bin_chars = ""
    temp = value
    for i in range(num):
        bin_char = bin(temp % 2)[-1]
        temp = temp // 2
        bin_chars = bin_char + bin_chars
    return bin_chars.upper()  # 输出指定位宽的二进制字符串


def create_car_file():
    list = os.listdir(path)
    print(list)
    for l in list:
        # *定义一个变量判断文件是否存在,path指代路径,str(i)指代文件夹的名字*
        isExists = os.path.exists(path + '/' + l + '/' + l + '.car')
        if not isExists:  # 判断如果文件不存在,则创建
            file = open(path + '/' + l + '/' + l + '.car', 'w')
            file.close()
            print("文件创建成功")
        else:
            print("%s 文件已经存在")
            continue  # 如果文件不存在,则继续上述操作,直到循环结束


# create_car_file()

# 把PolybaseP.car复制到每个子目录下的car文件中
def write_headFile():
    listdir = os.listdir(test_path)
    with open(r'./data/PolybaseP.car', 'r') as headFile:
        head_f = headFile.readlines()  # 读取文件内容行数
        # print(len(head_f))
        # print(head_f)
        # print(len(head_f))
        for dir in listdir:
            sequence = dir
            with open(test_path + '/' + sequence + '/' + sequence + '.car', 'w') as copyfile:
                for i in range(0, 159):
                    line = head_f[i]
                    copyfile.write(line)
                    # copyfile.close()
            print("%s已读入" % dir)
        # headFile.close()


def write_File(sequence):
    # listdir = os.listdir(testpath1)
    with open(r'./data/PolybaseP.car', 'r') as headFile:
        head_f = headFile.readlines()  # 读取文件内容行数
        to_list = list(sequence)  # 将文件名转为数组
        with open(path + '/' + sequence + '/' + sequence + '.car', 'w') as copyfile:
            i = 0
            while i < 159:
                line = head_f[i]
                d = {'C1': '  -0.053', 'C2': '  -0.106',
                     'C3': '  -0.159', 'C4': '  -0.159',
                     'H1': '   0.053', 'H2': '   0.053',
                     'H3': '   0.053', 'H4': '   0.053',
                     'H5': '   0.053', 'H6': '   0.053',
                     'H7': '   0.053', 'H8': '   0.053'}
                if i < 9 or i > 152:  # 读取文件边界内容
                    copyfile.write(line)
                    i = i + 1  # 步长为1
                else:
                    for j in range(0, len(list(sequence))):
                        if to_list[j] == '0':
                            for l1 in range(9 + j * 9, 14 + j * 9):
                                temp = head_f[l1].strip().split()
                                # print(temp)
                                # print(temp[6])
                                temp[4] = 'C2H4'
                                if temp[7] == 'C':
                                    temp[6] = 'e2'
                                elif temp[7] == 'H':
                                    temp[6] = 'hc'
                                # print(temp[6])
                                if float(temp[1]) >= 10:
                                    value_1 = 6
                                else:
                                    value_1 = 7
                                if float(temp[3]) >= 0:
                                    value_3 = 4
                                else:
                                    value_3 = 3
                                if float(temp[5]) >= 10:
                                    value_5 = 5
                                else:
                                    value_5 = 6
                                # if float(temp[8]) < 0:
                                #     value_6 = 2
                                # else:
                                #     value_6 = 3
                                # print(value_1)
                                if temp[0] == 'H2':
                                    temp[0] = 'H3'
                                elif temp[0] == 'H3':
                                    temp[0] = 'H4'
                                if l1 == 11 + j * 9:
                                    temp1 = head_f[l1].strip().split()
                                    temp2 = head_f[l1 - 1].strip().split()
                                    if float(temp2[1]) >= 10:
                                        value1_1 = 6
                                    else:
                                        value1_1 = 7
                                    # if float(temp2[8]) < 0:
                                    #     value1_6 = 2
                                    # else:
                                    #     value1_6 = 3
                                    temp1[0] = 'H2'
                                    temp1[1] = head_f[l1 - 1].strip().split()[1]
                                    temp1[2] = head_f[l1 + 2].strip().split()[2]
                                    copyfile.write(
                                        temp1[0] + ' ' * value1_1 +
                                        temp1[1] + ' ' * 4 +
                                        temp1[2] + ' ' * value_3 +
                                        temp1[3] + ' ' * 1 +
                                        'C2H4' + ' ' * 1 +
                                        temp1[5] + ' ' * value_5 +
                                        'hc' + ' ' * 6 +
                                        'H' +
                                        d.get(temp1[0]) + '\n'
                                    )
                                    # print(value1_1)
                                copyfile.write(
                                    temp[0] + ' ' * value_1 +
                                    temp[1] + ' ' * 4 +
                                    temp[2] + ' ' * value_3 +
                                    temp[3] + ' ' * 1 +
                                    temp[4] + ' ' * 1 +
                                    temp[5] + ' ' * value_5 +
                                    temp[6] + ' ' * 6 +
                                    temp[7] +
                                    d.get(temp[0]) + '\n'
                                )
                            i = i + 9  # 步长为9
                        elif to_list[j] == '1':
                            # 读取9行数据
                            for k in range(i, i + 9):
                                copyfile.write(head_f[k])
                            i = i + 9  # 步长为9

            copyfile.close()

        # headFile.close()


def main():
    for i in range(0, 65536):
        sequence = to_bin(i, 16)
        write_File(sequence)
        print("%s已读入" % sequence)
        # print(to_bin(i,16))


main()

# write_headFile()
# 使用正则表达式\s+跳过空格，跳过前五行，忽略列名
# df = pd.read_table(r"./data/PolybaseP.car", sep='\\s+', skiprows=5, header=None)
# print(df)
# df.to_csv(r"./data/1.car", index=False)
