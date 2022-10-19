import os  # 导入模块

path = r'E:\Study\pe-pp\Sequence_num'
test_path = r'E:\Study\pe-pp\test'
sort_path = r'E:\Study\pe-pp\Sequence_num_sort_demo'
final_path = r'E:\Study\pe-pp\Sequence_final'

# 根据修改后的car文件批量生成最终版mdf文件
# 原子分类
# with open(r'../data/sort_num_car/0000000001100000.car', 'r') as readFile_car:
#     readFile_lines = readFile_car.readlines()
#     with open(r'../data/mdf/PolybaseP.mdf', 'r') as readFile_mdf:
#         readFile_mdf_r = readFile_mdf.readlines()
#         with open(r'../data/sort_num_car/0000000001100000.mdf', 'w') as writeFile_mdf:
#             # 创建0-9的数字列表
#             char_first_num = [str(i) for i in range(0, 10)]
#             char_second_num = [str(i) for i in range(0, 10)]
#             # 创建英文26个字母列表
#             char_dx = [chr(i) for i in range(65, 91)]
#             char_dx.remove('L')
#             # 组合数组
#             char_num_dx = char_second_num + char_dx
#             # 写入mdf文件头部内容
#             # print(readFile_mdf_r[4])
#             for i in range(0, 18):
#                 writeFile_mdf.write(readFile_mdf_r[i])
#             writeFile_mdf.write('\n' + '@molecule' + ' ' + '0000000001100000')  # 此处写@molecule+ 文件名
#             writeFile_mdf.write('\n')
#             writeFile_mdf.write('\n')
#             # 使用两个空数组用来保存car文件第一列内容
#             list_C = []
#             list_H = []
#             for index_first in range(5, len(readFile_lines) - 2):
#                 char = readFile_lines[index_first][0]
#                 char__ = readFile_lines[index_first][0:3:1.txt]
#                 if char == 'C':
#                     list_C.append(char__)
#                 else:
#                     list_H.append(char__)
#             # print(list_H)
#             # print(list_C[69])
#             # print(list_C)
#             # print(list_H)
#             # 定义第一列数组的索引
#             index_C = 0
#             index_H = 0
#             count_C = len(list_C)
#             count_H = len(list_H)
#             # 根据car文件内容写入mdf文件
#             # 成键部分内容
#             # C原子部分
#             for j in range(5, count_C + 5):
#                 temp = readFile_lines[j].strip().split()
#                 # 纵向对齐
#                 if temp[6] == 'b':
#                     var1 = 7
#                     var3 = 'c3'
#                 elif temp[6] == 'e2' or temp[6] == 'p2':
#                     var1 = 6
#                     var3 = 'c2'
#                 elif temp[6] == 'p3':
#                     var1 = 6
#                     var3 = 'c3'
#                 elif temp[6] == 'p1':
#                     var1 = 6
#                     var3 = 'c1'
#                 if float(temp[8]) > 0:
#                     var2 = 5
#                 else:
#                     var2 = 4
#
#                 # 提取公共部分
#                 string = str('XXXX_1:' + temp[0] + ' ' * 10 + temp[7]
#                              + ' ' * 2 + var3 + ' ' * var1 + '?'
#                              + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * var2
#                              + temp[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
#                              + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
#                              )
#                 # 先写入首部C原子，且将b改为c3
#                 if temp[6] == 'b' and j == 5:
#                     writeFile_mdf.write(string + 'C01' + ' ' + 'H00' + ' ' + 'H01' + ' ' + 'H02 ' + '\n')
#                     index_C += 1.txt
#                     index_H += 3
#                 # 写入e2部分且将e2修改为c2
#                 elif temp[6] == 'e2' and readFile_lines[j - 1.txt].strip().split()[4] == 'CbHn':
#                     writeFile_mdf.write(
#                         string + list_C[index_C - 1.txt] + ' ' + list_H[index_H] + ' ' + list_H[index_H + 1.txt] + ' ' +
#                         list_C[index_C + 1.txt] + '\n')
#                     index_C += 1.txt
#                     index_H += 2
#                 elif temp[6] == 'e2' and readFile_lines[j - 1.txt].strip().split()[4] == 'C2H4':
#                     writeFile_mdf.write(
#                         string + list_C[index_C - 1.txt] + ' ' + list_H[index_H] + ' ' + list_H[index_H + 1.txt] + ' ' +
#                         list_C[index_C + 1.txt] + '\n')
#                     index_C += 1.txt
#                     index_H += 2
#                 elif temp[6] == 'e2' and readFile_lines[j - 1.txt].strip().split()[4] == 'C3H6':
#                     writeFile_mdf.write(
#                         string + list_C[index_C - 2] + ' ' + list_H[index_H] + ' ' + list_H[index_H + 1.txt] + ' ' +
#                         list_C[index_C + 1.txt] + '\n')
#                     index_C += 1.txt
#                     index_H += 2
#                 # 写入p1,p2,p3原子
#                 elif temp[6] == 'p1' and readFile_lines[j - 1.txt].strip().split()[4] == 'CbHn':
#                     writeFile_mdf.write(
#                         string + list_C[index_C - 1.txt] + ' ' + list_H[index_H] + ' ' + list_C[index_C + 1.txt] + ' ' +
#                         list_C[index_C + 2] + '\n')
#                     index_C += 1.txt
#                     index_H += 1.txt
#                 elif temp[6] == 'p1' and readFile_lines[j - 1.txt].strip().split()[4] == 'C2H4':
#                     writeFile_mdf.write(
#                         string + list_C[index_C - 1.txt] + ' ' + list_H[index_H] + ' ' + list_C[index_C + 1.txt] + ' ' +
#                         list_C[index_C + 2] + '\n')
#                     index_C += 1.txt
#                     index_H += 1.txt
#                 # 读取顺序为p1->p2-p3
#                 elif temp[6] == 'p1' and readFile_lines[j - 1.txt].strip().split()[4] == 'C3H6':
#                     writeFile_mdf.write(
#                         string + list_C[index_C - 2] + ' ' + list_C[index_C + 2] + ' ' + list_H[index_H] + ' ' +
#                         list_C[index_C + 1.txt] + '\n')
#                     index_C += 1.txt
#                     index_H += 1.txt
#                 elif temp[6] == 'p2':
#                     writeFile_mdf.write(
#                         string + list_C[index_C - 1.txt] + ' ' + list_H[index_H] + ' ' + list_H[index_H + 1.txt] + ' ' +
#                         list_C[index_C + 2] + '\n')
#                     index_C += 1.txt
#                     index_H += 2
#                 elif temp[6] == 'p3':
#                     writeFile_mdf.write(
#                         string + list_C[index_C - 2] + ' ' + list_H[index_H] + ' ' + list_H[index_H + 1.txt] + ' ' +
#                         list_H[index_H + 2] + '\n')
#                     index_C += 1.txt
#                     index_H += 3
#                 # 写入尾部C原子
#                 elif temp[6] == 'b' and j > 5:
#                     writeFile_mdf.write(
#                         string + list_C[index_C - 1.txt] + ' ' + list_H[index_H] + ' ' + list_H[index_H + 1.txt] + ' ' +
#                         list_H[index_H + 2] + '\n')
#
#             # H原子部分
#             # 将索引重新置为0
#             index_C = 0
#             k = 5 + count_C
#             # print('k的值等于%s：' % k)
#             # print("H原子数量为%s" % count_H)
#             while k < 5 + count_C + count_H:
#                 # for k in range(5 + count_C, 5 + count_C + count_H):
#                 # 提取公共部分
#                 # 写入首部H原子
#                 if readFile_lines[k].split()[4] == 'CbHn' and k < count_C + 8:
#                     while count_C + 5 <= k < count_C + 8:
#                         temp_H = readFile_lines[k].split()
#                         string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
#                                        + ' ' * 2 + 'hc' + ' ' * 6 + '?'
#                                        + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
#                                        + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
#                                        + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
#                                        )
#                         writeFile_mdf.write(string_H + list_C[index_C] + '\n')
#                         k += 1.txt
#                         # print(k)
#                         # index_H += 3
#                     index_C += 1.txt
#                     # print('写完首部H原子后C的索引为%s' % index_C)
#                 # 写入固定的前段五个乙烯单体
#                 if readFile_lines[k].split()[4] == 'CbHn' and count_C + 8 <= k < count_C + 28:
#                     help1 = k
#                     while k < help1 + 2:
#                         temp_H = readFile_lines[k].split()
#                         string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
#                                        + ' ' * 2 + 'hc' + ' ' * 6 + '?'
#                                        + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
#                                        + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
#                                        + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
#                                        )
#                         writeFile_mdf.write(string_H + list_C[index_C] + '\n')
#                         k += 1.txt
#                         # print(k)
#                     help2 = k
#                     while k < help2 + 2:
#                         temp_H = readFile_lines[k].split()
#                         string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
#                                        + ' ' * 2 + 'hc' + ' ' * 6 + '?'
#                                        + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
#                                        + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
#                                        + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
#                                        )
#                         writeFile_mdf.write(string_H + list_C[index_C + 1.txt] + '\n')
#                         k += 1.txt
#                         # print(k)
#                     index_C += 2
#                     # print(index_C)
#                     # print('写完固定的前段五个乙烯单体后C的索引为%s' % index_C)
#                 if readFile_lines[k].split()[4] == 'C2H4':
#                     help3 = k
#                     while k < help3 + 2:
#                         temp_H = readFile_lines[k].split()
#                         string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
#                                        + ' ' * 2 + 'hc' + ' ' * 6 + '?'
#                                        + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
#                                        + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
#                                        + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
#                                        )
#                         writeFile_mdf.write(string_H + list_C[index_C] + '\n')
#                         k += 1.txt
#                         # print(k)
#                     help4 = k
#                     while k < help4 + 2:
#                         temp_H = readFile_lines[k].split()
#                         string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
#                                        + ' ' * 2 + 'hc' + ' ' * 6 + '?'
#                                        + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
#                                        + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
#                                        + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
#                                        )
#                         writeFile_mdf.write(string_H + list_C[index_C + 1.txt] + '\n')
#                         k += 1.txt
#                         # print(k)
#                     index_C += 2
#
#                 if readFile_lines[k].split()[4] == 'C3H6':
#                     # print(index_C)
#                     # 首先写入p1连接的H原子
#                     temp_H = readFile_lines[k].split()
#                     string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
#                                    + ' ' * 2 + 'hc' + ' ' * 6 + '?'
#                                    + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
#                                    + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
#                                    + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
#                                    )
#                     writeFile_mdf.write(string_H + list_C[index_C] + '\n')
#                     k = k + 1.txt
#                     # print(k)
#                     v = k
#                     index_C += 1.txt
#                     # 写入连接p2的H原子
#                     while k < v + 2:
#                         temp_H = readFile_lines[k].split()
#                         string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
#                                        + ' ' * 2 + 'hc' + ' ' * 6 + '?'
#                                        + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
#                                        + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
#                                        + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
#                                        )
#                         writeFile_mdf.write(string_H + list_C[index_C] + '\n')
#                         k += 1.txt
#                         # print(k)
#                     w = k
#                     index_C += 1.txt
#                     # 写入连接p3的原子
#                     while k < w + 3:
#                         temp_H = readFile_lines[k].split()
#                         string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
#                                        + ' ' * 2 + 'hc' + ' ' * 6 + '?'
#                                        + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
#                                        + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
#                                        + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
#                                        )
#                         writeFile_mdf.write(string_H + list_C[index_C] + '\n')
#                         k += 1.txt
#                         # print(k)
#                     index_C += 1.txt
#                     # print(index_C)
#                     # print('写完丙烯单体后C的索引为%s' % index_C)
#                 # 写入固定的尾部5个乙烯单体
#                 if readFile_lines[k].split()[4] == 'CbHn' and count_C + count_H - 18 <= k < count_C + count_H + 2:
#                     help5 = k
#                     while k < help5 + 2:
#                         temp_H = readFile_lines[k].split()
#                         string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
#                                        + ' ' * 2 + 'hc' + ' ' * 6 + '?'
#                                        + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
#                                        + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
#                                        + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
#                                        )
#                         writeFile_mdf.write(string_H + list_C[index_C] + '\n')
#                         k += 1.txt
#                     help6 = k
#                     while k < help6 + 2:
#                         temp_H = readFile_lines[k].split()
#                         string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
#                                        + ' ' * 2 + 'hc' + ' ' * 6 + '?'
#                                        + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
#                                        + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
#                                        + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
#                                        )
#                         writeFile_mdf.write(string_H + list_C[index_C + 1.txt] + '\n')
#                         k += 1.txt
#                     index_C += 2
#                 # print(index_C)
#                 # 写入尾部H原子
#                 if readFile_lines[k].split()[4] == 'CbHn' and count_C + count_H + 2 <= k < 5 + count_C + count_H:
#                     while 2 + count_C + count_H <= k < 5 + count_C + count_H:
#                         temp_H = readFile_lines[k].split()
#                         string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
#                                        + ' ' * 2 + 'hc' + ' ' * 6 + '?'
#                                        + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
#                                        + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
#                                        + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
#                                        )
#                         # print(index_C)
#                         writeFile_mdf.write(string_H + list_C[index_C] + '\n')
#                         k += 1.txt
#                         # index_H += 3
#                     index_C += 1.txt
#
#                 # break
#                 continue
#
#             writeFile_mdf.write('\n' + '!' + '\n')
#             writeFile_mdf.write('#symmetry' + '\n')
#             writeFile_mdf.write('@periodicity 3 xyz' + '\n')
#             writeFile_mdf.write('@group (P1)' + '\n')
#             writeFile_mdf.write('\n' + '#end')


def write_final_mdf(sequence):
    with open(sort_path + '/' + sequence + '/' + sequence + '.car', 'r') as readFile_car:
        readFile_lines = readFile_car.readlines()
        with open(r'../data/mdf/PolybaseP.mdf', 'r') as readFile_mdf:
            readFile_mdf_r = readFile_mdf.readlines()
            with open(final_path + '/' + sequence + '/' + sequence + '.mdf', 'w') as writeFile_mdf:
                # 创建0-9的数字列表
                char_first_num = [str(i) for i in range(0, 10)]
                char_second_num = [str(i) for i in range(0, 10)]
                # 创建英文26个字母列表
                char_dx = [chr(i) for i in range(65, 91)]
                char_dx.remove('L')
                # 组合数组
                char_num_dx = char_second_num + char_dx
                # 写入mdf文件头部内容
                # print(readFile_mdf_r[4])
                for i in range(0, 18):
                    writeFile_mdf.write(readFile_mdf_r[i])
                writeFile_mdf.write('\n' + '@molecule' + ' ' + sequence)  # 此处写@molecule+ 文件名
                writeFile_mdf.write('\n')
                writeFile_mdf.write('\n')
                # 使用两个空数组用来保存car文件第一列内容
                list_C = []
                list_H = []
                for index_first in range(5, len(readFile_lines) - 2):
                    char = readFile_lines[index_first][0]
                    char__ = readFile_lines[index_first][0:3:1]
                    if char == 'C':
                        list_C.append(char__)
                    else:
                        list_H.append(char__)
                # print(list_H)
                # print(list_C[69])
                # print(list_C)
                # print(list_H)
                # 定义第一列数组的索引
                index_C = 0
                index_H = 0
                count_C = len(list_C)
                count_H = len(list_H)
                # 根据car文件内容写入mdf文件
                # 成键部分内容
                # C原子部分
                for j in range(5, count_C + 5):
                    temp = readFile_lines[j].strip().split()
                    # 纵向对齐
                    if temp[6] == 'b':
                        var1 = 7
                        var3 = 'c3'
                    elif temp[6] == 'e2' or temp[6] == 'p2':
                        var1 = 6
                        var3 = 'c2'
                    elif temp[6] == 'p3':
                        var1 = 6
                        var3 = 'c3'
                    elif temp[6] == 'p1':
                        var1 = 6
                        var3 = 'c1'
                    if float(temp[8]) > 0:
                        var2 = 5
                    else:
                        var2 = 4

                    # 提取公共部分
                    string = str('XXXX_1:' + temp[0] + ' ' * 10 + temp[7]
                                 + ' ' * 2 + var3 + ' ' * var1 + '?'
                                 + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * var2
                                 + temp[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
                                 + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
                                 )
                    # 先写入首部C原子，且将b改为c3
                    if temp[6] == 'b' and j == 5:
                        writeFile_mdf.write(string + 'C01' + ' ' + 'H00' + ' ' + 'H01' + ' ' + 'H02 ' + '\n')
                        index_C += 1
                        index_H += 3
                    # 写入e2部分且将e2修改为c2
                    elif temp[6] == 'e2' and readFile_lines[j - 1].strip().split()[4] == 'CbHn':
                        writeFile_mdf.write(
                            string + list_C[index_C - 1] + ' ' + list_H[index_H] + ' ' + list_H[index_H + 1] + ' ' +
                            list_C[index_C + 1] + '\n')
                        index_C += 1
                        index_H += 2
                    elif temp[6] == 'e2' and readFile_lines[j - 1].strip().split()[4] == 'C2H4':
                        writeFile_mdf.write(
                            string + list_C[index_C - 1] + ' ' + list_H[index_H] + ' ' + list_H[index_H + 1] + ' ' +
                            list_C[index_C + 1] + '\n')
                        index_C += 1
                        index_H += 2
                    elif temp[6] == 'e2' and readFile_lines[j - 1].strip().split()[4] == 'C3H6':
                        writeFile_mdf.write(
                            string + list_C[index_C - 2] + ' ' + list_H[index_H] + ' ' + list_H[index_H + 1] + ' ' +
                            list_C[index_C + 1] + '\n')
                        index_C += 1
                        index_H += 2
                    # 写入p1,p2,p3原子
                    elif temp[6] == 'p1' and readFile_lines[j - 1].strip().split()[4] == 'CbHn':
                        writeFile_mdf.write(
                            string + list_C[index_C - 1] + ' ' + list_H[index_H] + ' ' + list_C[index_C + 1] + ' ' +
                            list_C[index_C + 2] + '\n')
                        index_C += 1
                        index_H += 1
                    elif temp[6] == 'p1' and readFile_lines[j - 1].strip().split()[4] == 'C2H4':
                        writeFile_mdf.write(
                            string + list_C[index_C - 1] + ' ' + list_H[index_H] + ' ' + list_C[index_C + 1] + ' ' +
                            list_C[index_C + 2] + '\n')
                        index_C += 1
                        index_H += 1
                    # 读取顺序为p1->p2-p3
                    elif temp[6] == 'p1' and readFile_lines[j - 1].strip().split()[4] == 'C3H6':
                        writeFile_mdf.write(
                            string + list_C[index_C - 2] + ' ' + list_C[index_C + 2] + ' ' + list_H[index_H] + ' ' +
                            list_C[index_C + 1] + '\n')
                        index_C += 1
                        index_H += 1
                    elif temp[6] == 'p2':
                        writeFile_mdf.write(
                            string + list_C[index_C - 1] + ' ' + list_H[index_H] + ' ' + list_H[index_H + 1] + ' ' +
                            list_C[index_C + 2] + '\n')
                        index_C += 1
                        index_H += 2
                    elif temp[6] == 'p3':
                        writeFile_mdf.write(
                            string + list_C[index_C - 2] + ' ' + list_H[index_H] + ' ' + list_H[index_H + 1] + ' ' +
                            list_H[index_H + 2] + '\n')
                        index_C += 1
                        index_H += 3
                    # 写入尾部C原子
                    elif temp[6] == 'b' and j > 5:
                        writeFile_mdf.write(
                            string + list_C[index_C - 1] + ' ' + list_H[index_H] + ' ' + list_H[index_H + 1] + ' ' +
                            list_H[index_H + 2] + '\n')

                # H原子部分
                # 将索引重新置为0
                index_C = 0
                k = 5 + count_C
                # print('k的值等于%s：' % k)
                # print("H原子数量为%s" % count_H)
                while k < 5 + count_C + count_H:
                    # for k in range(5 + count_C, 5 + count_C + count_H):
                    # 提取公共部分
                    # 写入首部H原子
                    if readFile_lines[k].split()[4] == 'CbHn' and k < count_C + 8:
                        while count_C + 5 <= k < count_C + 8:
                            temp_H = readFile_lines[k].split()
                            string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
                                           + ' ' * 2 + 'hc' + ' ' * 6 + '?'
                                           + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
                                           + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
                                           + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
                                           )
                            writeFile_mdf.write(string_H + list_C[index_C] + '\n')
                            k += 1
                            # print(k)
                            # index_H += 3
                        index_C += 1
                        # print('写完首部H原子后C的索引为%s' % index_C)
                    # 写入固定的前段五个乙烯单体
                    if readFile_lines[k].split()[4] == 'CbHn' and count_C + 8 <= k < count_C + 28:
                        help1 = k
                        while k < help1 + 2:
                            temp_H = readFile_lines[k].split()
                            string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
                                           + ' ' * 2 + 'hc' + ' ' * 6 + '?'
                                           + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
                                           + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
                                           + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
                                           )
                            writeFile_mdf.write(string_H + list_C[index_C] + '\n')
                            k += 1
                            # print(k)
                        help2 = k
                        while k < help2 + 2:
                            temp_H = readFile_lines[k].split()
                            string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
                                           + ' ' * 2 + 'hc' + ' ' * 6 + '?'
                                           + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
                                           + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
                                           + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
                                           )
                            writeFile_mdf.write(string_H + list_C[index_C + 1] + '\n')
                            k += 1
                            # print(k)
                        index_C += 2
                        # print(index_C)
                        # print('写完固定的前段五个乙烯单体后C的索引为%s' % index_C)
                    if readFile_lines[k].split()[4] == 'C2H4':
                        help3 = k
                        while k < help3 + 2:
                            temp_H = readFile_lines[k].split()
                            string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
                                           + ' ' * 2 + 'hc' + ' ' * 6 + '?'
                                           + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
                                           + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
                                           + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
                                           )
                            writeFile_mdf.write(string_H + list_C[index_C] + '\n')
                            k += 1
                            # print(k)
                        help4 = k
                        while k < help4 + 2:
                            temp_H = readFile_lines[k].split()
                            string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
                                           + ' ' * 2 + 'hc' + ' ' * 6 + '?'
                                           + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
                                           + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
                                           + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
                                           )
                            writeFile_mdf.write(string_H + list_C[index_C + 1] + '\n')
                            k += 1
                            # print(k)
                        index_C += 2

                    if readFile_lines[k].split()[4] == 'C3H6':
                        # print(index_C)
                        # 首先写入p1连接的H原子
                        temp_H = readFile_lines[k].split()
                        string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
                                       + ' ' * 2 + 'hc' + ' ' * 6 + '?'
                                       + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
                                       + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
                                       + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
                                       )
                        writeFile_mdf.write(string_H + list_C[index_C] + '\n')
                        k = k + 1
                        # print(k)
                        v = k
                        index_C += 1
                        # 写入连接p2的H原子
                        while k < v + 2:
                            temp_H = readFile_lines[k].split()
                            string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
                                           + ' ' * 2 + 'hc' + ' ' * 6 + '?'
                                           + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
                                           + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
                                           + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
                                           )
                            writeFile_mdf.write(string_H + list_C[index_C] + '\n')
                            k += 1
                            # print(k)
                        w = k
                        index_C += 1
                        # 写入连接p3的原子
                        while k < w + 3:
                            temp_H = readFile_lines[k].split()
                            string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
                                           + ' ' * 2 + 'hc' + ' ' * 6 + '?'
                                           + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
                                           + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
                                           + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
                                           )
                            writeFile_mdf.write(string_H + list_C[index_C] + '\n')
                            k += 1
                            # print(k)
                        index_C += 1
                        # print(index_C)
                        # print('写完丙烯单体后C的索引为%s' % index_C)
                    # 写入固定的尾部5个乙烯单体
                    if readFile_lines[k].split()[4] == 'CbHn' and count_C + count_H - 18 <= k < count_C + count_H + 2:
                        help5 = k
                        while k < help5 + 2:
                            temp_H = readFile_lines[k].split()
                            string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
                                           + ' ' * 2 + 'hc' + ' ' * 6 + '?'
                                           + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
                                           + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
                                           + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
                                           )
                            writeFile_mdf.write(string_H + list_C[index_C] + '\n')
                            k += 1
                        help6 = k
                        while k < help6 + 2:
                            temp_H = readFile_lines[k].split()
                            string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
                                           + ' ' * 2 + 'hc' + ' ' * 6 + '?'
                                           + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
                                           + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
                                           + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
                                           )
                            writeFile_mdf.write(string_H + list_C[index_C + 1] + '\n')
                            k += 1
                        index_C += 2
                    # print(index_C)
                    # 写入尾部H原子
                    if readFile_lines[k].split()[4] == 'CbHn' and count_C + count_H + 2 <= k < 5 + count_C + count_H:
                        while 2 + count_C + count_H <= k < 5 + count_C + count_H:
                            temp_H = readFile_lines[k].split()
                            string_H = str('XXXX_1:' + temp_H[0] + ' ' * 10 + 'H'
                                           + ' ' * 2 + 'hc' + ' ' * 6 + '?'
                                           + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * 5
                                           + temp_H[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
                                           + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
                                           )
                            # print(index_C)
                            writeFile_mdf.write(string_H + list_C[index_C] + '\n')
                            k += 1
                            # index_H += 3
                        index_C += 1

                    # break
                    continue

                writeFile_mdf.write('\n' + '!' + '\n')
                writeFile_mdf.write('#symmetry' + '\n')
                writeFile_mdf.write('@periodicity 3 xyz' + '\n')
                writeFile_mdf.write('@group (P1)' + '\n')
                writeFile_mdf.write('\n' + '#end')


def create_mdf_file():
    list = os.listdir(final_path)
    # print(list)
    for l in list:
        # *定义一个变量判断文件是否存在,path指代路径,str(i)指代文件夹的名字*
        isExists = os.path.exists(final_path + '/' + l + '/' + l + '.mdf')
        if not isExists:  # 判断如果文件不存在,则创建
            file = open(final_path + '/' + l + '/' + l + '.mdf', 'w')
            file.close()
            print("%s 文件创建成功" % l)
        else:
            print("%s 文件已经存在")
            continue  # 如果文件不存在,则继续上述操作,直到循环结束


# create_mdf_file()


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
        write_final_mdf(sequence)
        print("%s已读入" % sequence)
        # print(to_bin(i,16))

main()
