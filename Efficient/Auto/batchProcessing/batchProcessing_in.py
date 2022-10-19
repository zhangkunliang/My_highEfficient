# coding=utf-8

import os
import shutil

ms_path = r'E:\Study\pe-pp\ms'
path = r'E:\Study\pe-pp\Sequence_num'
test_path = r'E:\Study\pe-pp\test_lammps\Sequence_final'
sort_path = r'E:\Study\pe-pp\Sequence_num_sort_demo'
final_path = r'E:\Study\pe-pp\Sequence_final'
final_path_data = r'E:\Study\pe-pp\Sequence_final_data_2case'


def to_bin(value, num):  # 十进制数据，二进制位宽
    bin_chars = ""
    temp = value
    for i in range(num):
        bin_char = bin(temp % 2)[-1]
        temp = temp // 2
        bin_chars = bin_char + bin_chars
    return bin_chars.upper()  # 输出指定位宽的二进制字符串


def batchProcessinData(sequence):
    os.chdir(final_path + '\\' + sequence)
    # print(os.getcwd())  # 获取当前目录
    # os.system("dir" + " " + test_path+"\\"+"1111111111111111")  # 获取指定目录路径下的文件
    os.system("msi2lmp.exe " + sequence + " -class 2 -frc ../pcff.frc -i")


# def CopyInAndmodification():
#     with open(r'../data/in/TC.in', 'r', encoding='utf-8') as readIn:
#         lines = readIn.readlines()
#         shutil.copy(r'../data/in/TC.in', r'../test')
#         with open(r'../test/TC.in', 'w') as writeIn:
#             line = 0
#             while line < len(lines):
#                 if line == 17:
#                     writeIn.write('read_data ' + '0011111111111111' + '.data' + '\n')
#                     line += 1.txt
#                 else:
#                     writeIn.write(lines[line])
#                     line += 1.txt


def CopyInAndmodification(sequence):
    with open(r'../data/in/TC.in', 'r', encoding='utf-8') as readIn:
        lines = readIn.readlines()
        shutil.copy(r'../data/in/TC.in', final_path_data + '/' + sequence)
        with open(final_path_data + '/' + sequence + '/' + 'TC.in', 'w') as writeIn:
            line = 0
            while line < len(lines):
                if line == 17:
                    writeIn.write('read_data ' + sequence + '.data' + '\n')
                    line += 1
                else:
                    writeIn.write(lines[line])
                    line += 1


# def CopyInAndmodification(sequence):
#     for i in os.listdir(final_path + '/' + sequence):  # 遍历序列文件夹下的文件
#         i = i.split('.')  # 将jpg文件的前缀和后缀分开
#         data_path = (final_path + '/' + sequence + '/' + sequence + '.data')
#         shutil.copy(data_path, final_path_data + '/' + sequence)  # 复制文件


def main():
    for i in range(0, 65536):
        sequence = to_bin(i, 16)
        CopyInAndmodification(sequence)
        print("%s已读入" % sequence)
        # print(to_bin(i,16))


# main()
# CopyInAndmodification()
main()
