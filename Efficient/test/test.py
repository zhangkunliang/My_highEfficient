import numpy as np
import pandas as pd
import os  # 导入模块

path = r'/Users/zhangkunliang/ms/PE-PP'
testpath = r'/Users/zhangkunliang/ms/test'
testpath1 = r'/Users/zhangkunliang/ms/test1.mdf'


# import pandas as pd
# df_txt =  pd.read_table('PolyC2H4.mdf',nrows=120)
# print(df_txt)
def To2(x, n):
    """
    :param x: the value you want to convert
    :param n: keep n bits
    :return: binary value
    """

    X = x
    N = n
    m = bin(X)
    m = m.lstrip('0b')
    a = []
    L = []
    if len(m) < N:
        for i in range(N - len(m)):
            a.append('0')
        a = ''.join(a)
        k = a + m
    else:
        k = m
    for j in range(len(k)):
        L.append(k[j])
    return L


# print(To2(65535,16))

def write(s):
    with open(testpath1 + '/' + s + '/' + s + '.car', 'w') as copyfile:
        copyfile.write("hao" + " " * 3 + "meme")
    copyfile.close()


# write('1111111111111101')


def write_headFile():
    # listdir = os.listdir(testpath1)
    with open(r'/Users/zhangkunliang/PycharmProjects/Efficient/Auto/data/PolybaseP.car', 'r') as headFile:
        head_f = headFile.readlines()  # 读取文件内容行数
        to_list = list('0000000000000011')  # 将文件名转为数组
        with open(testpath1 + '/' + '0000000000000011' + '/' + '0000000000000011' + '.car', 'w') as copyfile:
            i = 0
            while i < 159:
                line = head_f[i]
                if i < 9 or i > 152:  # 读取文件边界内容
                    copyfile.write(line)
                    i = i + 1  # 步长为1
                else:
                    for j in range(0, len(list('0000000000000011'))):
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
                                # print(value_1)
                                if temp[0] == 'H2':
                                    temp[0] = 'H3'
                                elif temp[0] == 'H3':
                                    temp[0] = 'H4'
                                if l1 == 11 + j * 9:
                                    temp1 = head_f[l1].strip().split()
                                    temp2 = head_f[l1-1].strip().split()
                                    if float(temp2[1]) >= 10:
                                        value1_1 = 6
                                    else:
                                        value1_1 = 7
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
                                        'H' + ' ' * 3 +
                                        temp1[8] + '\n'
                                    )
                                    print(value1_1)
                                copyfile.write(
                                    temp[0] + ' ' * value_1 +
                                    temp[1] + ' ' * 4 +
                                    temp[2] + ' ' * value_3 +
                                    temp[3] + ' ' * 1 +
                                    temp[4] + ' ' * 1 +
                                    temp[5] + ' ' * value_5 +
                                    temp[6] + ' ' * 6 +
                                    temp[7] + ' ' * 3 +
                                    temp[8] + '\n'
                                )
                            i = i + 9  # 步长为9
                        elif to_list[j] == '1':
                            # 读取9行数据
                            for k in range(i, i + 9):
                                copyfile.write(head_f[k])
                            i = i + 9  # 步长为9

            copyfile.close()
        print("%s已读入" % dir)
        # headFile.close()


def write_zero():
    with open(r'/Users/zhangkunliang/PycharmProjects/Efficient/Auto/data/PolybaseP.car', 'r') as headFile:
        head_f = headFile.readlines()  # 读取文件内容行数
        to_list = list('0000000000000011')
        with open(testpath1 + '/' + '0000000000000011' + '/' + '0000000000000011' + '.car', 'w') as copyfile:
            for j in range(0, len(list('0000000000000011'))):
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
                        if float(temp[3]) > 0:
                            value_3 = 4
                        else:
                            value_3 = 3
                        if float(temp[5]) >= 10:
                            value_5 = 5
                        else:
                            value_5 = 6
                        # print(value_1)
                        if temp[0] == 'H2':
                            temp[0] = 'H3'
                        elif temp[0] == 'H3':
                            temp[0] = 'H4'
                        if l1 == 11 + j * 9:
                            temp1 = head_f[l1].strip().split()
                            temp1[0] = 'H2'
                            temp1[1] = head_f[l1 - 1].strip().split()[1]
                            temp1[2] = head_f[l1 + 2].strip().split()[2]
                            copyfile.write(
                                temp1[0] + ' ' * value_1 +
                                temp1[1] + ' ' * 4 +
                                temp1[2] + ' ' * value_3 +
                                temp1[3] + ' ' * 1 +
                                'C2H4' + ' ' * 1 +
                                temp1[5] + ' ' * value_5 +
                                'hc' + ' ' * 6 +
                                'H' + ' ' * 3 +
                                temp1[8] + '\n'
                            )
                        copyfile.write(
                            temp[0] + ' ' * value_1 +
                            temp[1] + ' ' * 4 +
                            temp[2] + ' ' * value_3 +
                            temp[3] + ' ' * 1 +
                            temp[4] + ' ' * 1 +
                            temp[5] + ' ' * value_5 +
                            temp[6] + ' ' * 6 +
                            temp[7] + ' ' * 3 +
                            temp[8] + '\n'
                        )

            copyfile.close()


# print(len(list('1111111111111101')))
write_headFile()
# write_zero()
