import os  # 导入模块

path = r'E:\Study\pe-pp\Sequence_num'
test_path = r'E:\Study\pe-pp\test'
sort_path = r'E:\Study\pe-pp\Sequence_num_sort_demo'
final_path = r'E:\Study\pe-pp\Sequence_final'

# 修改后版本，原子分组改为字母排序方式
# 原子分类
# with open(r'../data/sort_num_car/0000000001100000.car', 'r') as readFile_car:
#     readFile_lines = readFile_car.readlines()
#     # 修改car文件，根据倒数第二列将C和H原子进行分类
#     with open(r'../data/sort_num_car/0000000001100000.car', 'w') as writeFile_car:
#         # 创建0-9的数字列表
#         char_first_num = [str(i) for i in range(0, 10)]
#         char_second_num = [str(i) for i in range(0, 10)]
#         # 创建英文26个字母列表
#         char_dx = [chr(i) for i in range(65, 91)]
#         char_dx.remove('L')
#         # 组合数组
#         char_num_dx = char_second_num + char_dx
#         # 将文件头部内容先写入
#         for index_head in range(0, 5):
#             writeFile_car.write(readFile_lines[index_head])
#         index_char_first = 0
#         index_second_char = 0
#         # 写入文件中间内容
#         for index_mid in range(5, len(readFile_lines) - 2):
#
#             # 先将C原子进行分类
#             if readFile_lines[index_mid].split()[7] == 'C':
#                 # 判断是否为second列表的最后一个元素
#                 if index_second_char != 35:
#                     writeFile_car.write('C' + str(index_char_first)
#                                         + char_num_dx[index_second_char] + readFile_lines[index_mid][3:]
#                                         )
#                     index_second_char += 1.txt
#                 else:
#                     # 第二个字符从列表头开始记
#                     index_second_char = 0
#                     index_char_first += 1.txt
#                     writeFile_car.write('C' + str(index_char_first)
#                                         + char_num_dx[index_second_char] + readFile_lines[index_mid][3:]
#                                         )
#                     index_second_char += 1.txt
#         index_char_first = 0
#         index_second_char = 0
#         # 从头开始循环分类H原子
#         for index_mid in range(5, len(readFile_lines) - 2):
#             # 先将C原子进行分类
#             if readFile_lines[index_mid].split()[7] == 'H':
#                 if index_second_char != 35:
#                     writeFile_car.write('H' + str(index_char_first)
#                                         + char_num_dx[index_second_char] + readFile_lines[index_mid][3:]
#                                         )
#                     index_second_char += 1.txt
#                 else:
#                     index_second_char = 0
#                     index_char_first += 1.txt
#                     writeFile_car.write('H' + str(index_char_first)
#                                         + char_num_dx[index_second_char] + readFile_lines[index_mid][3:]
#                                         )
#                     index_second_char += 1.txt
#         # car文件第一列原子序号列写入完毕
#         # 写入文件尾部内容
#         writeFile_car.write('end' + '\n' + 'end')

def write_sort_car(sequence):
    with open(path + '/' + sequence + '/' + sequence + '.car', 'r') as readFile_car:
        readFile_lines = readFile_car.readlines()
        # 修改car文件，根据倒数第二列将C和H原子进行分类
        with open(sort_path + '/' + sequence + '/' + sequence + '.car', 'w') as writeFile_car:
            # 创建0-9的数字列表
            # char_first_num = [str(i) for i in range(0, 10)]
            char_second_num = [str(i) for i in range(0, 10)]
            # 创建英文26个字母列表
            char_dx = [chr(i) for i in range(65, 91)]
            char_dx.remove('L')
            # 组合数组
            char_num_dx = char_second_num + char_dx
            # 将文件头部内容先写入
            for index_head in range(0, 5):
                writeFile_car.write(readFile_lines[index_head])
            index_char_first = 0
            index_second_char = 0
            # 写入文件中间内容
            for index_mid in range(5, len(readFile_lines) - 2):

                # 先将C原子进行分类
                if readFile_lines[index_mid].split()[7] == 'C':
                    # 判断是否为second列表的最后一个元素
                    if index_second_char != 35:
                        writeFile_car.write('C' + str(index_char_first)
                                            + char_num_dx[index_second_char] + readFile_lines[index_mid][3:]
                                            )
                        index_second_char += 1
                    else:
                        # 第二个字符从列表头开始记
                        index_second_char = 0
                        index_char_first += 1
                        writeFile_car.write('C' + str(index_char_first)
                                            + char_num_dx[index_second_char] + readFile_lines[index_mid][3:]
                                            )
                        index_second_char += 1
            index_char_first = 0
            index_second_char = 0
            # 从头开始循环分类H原子
            for index_mid in range(5, len(readFile_lines) - 2):
                # 先将C原子进行分类
                if readFile_lines[index_mid].split()[7] == 'H':
                    if index_second_char != 35:
                        writeFile_car.write('H' + str(index_char_first)
                                            + char_num_dx[index_second_char] + readFile_lines[index_mid][3:]
                                            )
                        index_second_char += 1
                    else:
                        index_second_char = 0
                        index_char_first += 1
                        writeFile_car.write('H' + str(index_char_first)
                                            + char_num_dx[index_second_char] + readFile_lines[index_mid][3:]
                                            )
                        index_second_char += 1
            # car文件第一列原子序号列写入完毕
            # 写入文件尾部内容
            writeFile_car.write('end' + '\n' + 'end')


def to_bin(value, num):  # 十进制数据，二进制位宽
    bin_chars = ""
    temp = value
    for i in range(num):
        bin_char = bin(temp % 2)[-1]
        temp = temp // 2
        bin_chars = bin_char + bin_chars
    return bin_chars.upper()  # 输出指定位宽的二进制字符串


def main():
    for i in range(0, 65536):
        sequence = to_bin(i, 16)
        write_sort_car(sequence)
        print("%s已读入" % sequence)
        # print(to_bin(i,16))


main()
