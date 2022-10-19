import os  # 导入模块

path = r'E:\Study\pe-pp\Sequence_num'
test_path = r'E:\Study\pe-pp\test'
sort_path = r'E:\Study\pe-pp\Sequence_num_sort_demo'
final_path = r'E:\Study\pe-pp\Sequence_final'

# 批量修改car文件内容，批量生成mdf文件后再去除首列辅助列

# with open(r'../data/sort_num_car/0000000001100000.car', 'r') as fix_car_readFile:
#     readlines = fix_car_readFile.readlines()
#     with open(r'../data/sort_num_car/0000000001100000.car', 'w') as fix_car_writeFile:
#         # 先写入头文件部分
#         for i in range(0, 5):
#             fix_car_writeFile.write(readlines[i])
#
#         for index_mid in range(5, len(readlines) - 2):
#             temp = readlines[index_mid].split()
#             if temp[6] == 'b' or temp[6] == 'p3':
#                 temp[6] = 'c3'
#             elif temp[6] == 'e2' or temp[6] == 'p2':
#                 temp[6] = 'c2'
#             elif temp[6] == 'p1':
#                 temp[6] = 'c1'
#             fix_car_writeFile.write(
#                 readlines[index_mid][0:50:1.txt] + ' ' + 'XXXX 1.txt' + ' ' * 6 + temp[6]
#                 + ' ' * 6 + temp[7] + readlines[index_mid][72:])
#
#         # 写入文件尾部内容
#         fix_car_writeFile.write('end' + '\n' + 'end')

def fix_car(sequence):
    with open(sort_path + '/' + sequence + '/' + sequence + '.car', 'r') as fix_car_readFile:
        readlines = fix_car_readFile.readlines()
        with open(final_path + '/' + sequence + '/' + sequence + '.car', 'w') as fix_car_writeFile:
            # 先写入头文件部分
            for i in range(0, 5):
                fix_car_writeFile.write(readlines[i])

            for index_mid in range(5, len(readlines) - 2):
                temp = readlines[index_mid].split()
                if temp[6] == 'b' or temp[6] == 'p3':
                    temp[6] = 'c3'
                elif temp[6] == 'e2' or temp[6] == 'p2':
                    temp[6] = 'c2'
                elif temp[6] == 'p1':
                    temp[6] = 'c1'
                fix_car_writeFile.write(
                    readlines[index_mid][0:50:1] + ' ' + 'XXXX 1.txt' + ' ' * 6 + temp[6]
                    + ' ' * 6 + temp[7] + readlines[index_mid][72:])

            # 写入文件尾部内容
            fix_car_writeFile.write('end' + '\n' + 'end')


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
        fix_car(sequence)
        print("%s已读入" % sequence)
        # print(to_bin(i,16))


main()
