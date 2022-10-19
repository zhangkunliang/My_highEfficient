# coding=utf-8

import os
import shutil

ms_path = r'E:\Study\pe-pp\ms'
path = r'E:\Study\pe-pp\Sequence_num'
test_path = r'E:\Study\pe-pp\test_lammps\Sequence_final'
sort_path = r'E:\Study\pe-pp\Sequence_num_sort_demo'
final_path = r'E:\Study\pe-pp\Sequence_final'
final_path_data = r'E:\Study\pe-pp\Sequence_final_data_1case'


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


# def modification():
#     with open(r'../data/data/1111111111111000.data', 'r') as readData:
#         lines = readData.readlines()
#         with open(r'../data/data/1111111111111000.data', 'w') as writeData:
#             line = 0
#             while line < len(lines):
#                 if line == 14:
#                     writeData.write('     0.157852332    71.357852332 xlo xhi' + '\n')
#                     writeData.write('     -16.071436287    24.071436287 ylo yhi' + '\n')
#                     writeData.write('     -15.220521633    25.220521633 zlo zhi' + '\n')
#                     line += 3
#                 else:
#                     writeData.write(lines[line])
#                     line += 1

def modification(sequence):
    with open(final_path_data + '/' + sequence + '/' + sequence + '.data', 'r') as readData:
        lines = readData.readlines()
        with open(final_path_data + '/' + sequence + '/' + sequence + '.data', 'w') as writeData:
            line = 0
            while line < len(lines):
                if line == 14:
                    writeData.write('     0.157852332    71.357852332 xlo xhi' + '\n')
                    writeData.write('     -21.071436287    29.071436287 ylo yhi' + '\n')
                    writeData.write('     -15.220521633    25.220521633 zlo zhi' + '\n')
                    line += 3
                else:
                    writeData.write(lines[line])
                    line += 1


def CopyData(sequence):
    for i in os.listdir(final_path+'/'+sequence):  # 遍历序列文件夹下的文件
        i = i.split('.')  # 将jpg文件的前缀和后缀分开
        if i[1] == 'data':
            data_path = (final_path+'/'+sequence+'/'+sequence+'.data')
            shutil.copy(data_path, final_path_data+'/'+sequence)  # 复制文件


def main():
    for i in range(0, 65536):
        sequence = to_bin(i, 16)
        modification(sequence)
        print("%s已读入" % sequence)
        # print(to_bin(i,16))
main()
# modification()
# main()
