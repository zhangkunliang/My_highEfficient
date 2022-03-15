# coding:utf-8
import os

path = r'E:\Study\pe-pp\Sequence_num'
test_path = r'E:\Study\pe-pp\test'


def write_mdf(sequence):
    with open(path + '/' + sequence + '/' + sequence + '.car', 'r') as readFile_car:
        readFile_car_r = readFile_car.readlines()  # 读取文件内容行数
        # print(readFile_f)
        with open(r'./data/polybaseP.mdf', 'r') as readFile_mdf:
            with open(path + '/' + sequence + '/' + sequence + '.mdf', 'w') as writeFile_mdf:
                readFile_mdf_r = readFile_mdf.readlines()
                # print(readFile_mdf_r[4])
                for i in range(0, 18):
                    writeFile_mdf.write(readFile_mdf_r[i])
                writeFile_mdf.write('\n' + '@molecule' + ' ' + sequence)  # 此处写@molecule+ 文件名
                writeFile_mdf.write('\n')
                writeFile_mdf.write('\n')
                for j in range(5, len(readFile_car_r) - 2):
                    d1 = {5: "C1 H7 H8 H9", 6: "C4", 7: "C4", 8: "C4",
                          len(readFile_car_r) - 6: "C2 H7 H8 H9",
                          len(readFile_car_r) - 5: "C4",
                          len(readFile_car_r) - 4: "C4",
                          len(readFile_car_r) - 3: "C4"
                          }  # 使用字典建立映射关系
                    temp = readFile_car_r[j].strip().split()
                    # 纵向对齐
                    if int(temp[5]) >= 10:
                        var1 = 10
                    else:
                        var1 = 11
                    if temp[6] == 'b':
                        var2 = 7
                    else:
                        var2 = 6
                    if float(temp[8]) > 0:
                        var3 = 5
                    else:
                        var3 = 4
                    string = str(temp[4] + '_' + temp[5] + ':' + temp[0] + ' ' * var1 + temp[7]
                                 + ' ' * 2 + temp[6] + ' ' * var2 + '?'
                                 + ' ' * 5 + '0' + ' ' * 2 + '0' + ' ' * var3
                                 + temp[8] + ' ' + '0' + ' ' + '0' + ' ' + '8' + ' '
                                 + '1.0000' + ' ' * 2 + '0.0000' + ' '
                                 )
                    #  头尾甲基CH3部分
                    if 5 <= j <= 8 or len(readFile_car_r) - 6 <= j <= len(readFile_car_r) - 3:
                        writeFile_mdf.write(string + d1.get(j, ' '))  # 字典中没有映射则返回' '
                        writeFile_mdf.write('\n')
                        # 筛选出特殊情况
                    elif j == 9 and temp[6] == 'p1':
                        # 连接头部甲基C4的p1
                        writeFile_mdf.write(string + 'H1 C2 C3 C4 ')
                        writeFile_mdf.write('\n')
                    elif j == 9 and temp[6] == 'e2':
                        # 连接头部甲基C4的e2
                        writeFile_mdf.write(string + 'H1 C2 H2 C4')
                        writeFile_mdf.write('\n')
                    elif j > 9 and int(temp[5]) <= 17:
                        # 1.C2H4的C1
                        if temp[0] == 'C1' and temp[4] == 'C2H4':
                            writeFile_mdf.write(
                                string + 'H1 C2 H2' + ' ' + 'C2H4_' + str(int(temp[5]) - 1) + ':' + 'C2')
                            writeFile_mdf.write('\n')
                        # 2.C2H4的H1,H2,H3,H4
                        if (temp[0] == 'H1' or temp[0] == 'H2') and temp[4] == 'C2H4':
                            writeFile_mdf.write(string + 'C1')
                            writeFile_mdf.write('\n')
                        if (temp[0] == 'H3' or temp[0] == 'H4') and temp[4] == 'C2H4':
                            writeFile_mdf.write(string + 'C2')
                            writeFile_mdf.write('\n')
                        # 3.C2H4的C2
                        if temp[0] == 'C2' and temp[4] == 'C2H4' and int(temp[5]) < 17:
                            writeFile_mdf.write(
                                string + 'C1 H3 H4' + ' ' + 'C2H4_' + str(int(temp[5]) + 1) + ':' + 'C1')
                            writeFile_mdf.write('\n')
                        # 1.C3H6的H4,H5,H6
                        if (temp[0] == 'H4' or temp[0] == 'H5' or temp[0] == 'H6') and temp[4] == 'C3H6':
                            writeFile_mdf.write(string + 'C3')
                            writeFile_mdf.write('\n')
                        # 2.C3H6的C1
                        if temp[0] == 'C1' and temp[4] == 'C3H6':
                            writeFile_mdf.write(
                                string + 'H1 C2 C3' + ' ' + readFile_car_r[j - 1].strip().split()[4] + '_' +
                                str(int(temp[5]) - 1) + ':' + 'C2')
                            # string + 'H1 C2 C3' + ' ' + 'C3H6_' + str(int(temp[5]) - 1) + ':' + 'C2')  # 连接的上一个分子的C2
                            writeFile_mdf.write('\n')
                        # 3.C3H6的C2
                        if temp[0] == 'C2' and temp[4] == 'C3H6' and int(temp[5]) < 17:
                            writeFile_mdf.write(
                                string + 'C1 H2 H3' + ' ' + readFile_car_r[j + 7].strip().split()[4] + '_' +
                                str(int(temp[5]) + 1) + ':' + 'C1')
                            # string + 'C1 H2 H3' + ' ' + 'C3H6_' + str(int(temp[5]) + 1) + ':' + 'C1')  # 连接的下一个分子的C1
                            writeFile_mdf.write('\n')
                        # 4.C3H6的C3
                        if temp[0] == 'C3' and temp[4] == 'C3H6':
                            writeFile_mdf.write(
                                string + 'C1 H4 H5 H6')
                            writeFile_mdf.write('\n')
                        # 5.C3H6的H1
                        if temp[0] == 'H1' and temp[4] == 'C3H6':
                            writeFile_mdf.write(string + 'C1')
                            writeFile_mdf.write('\n')
                        # 6.C3H6的H2和H3
                        if (temp[0] == 'H2' or temp[0] == 'H3') and temp[4] == 'C3H6':
                            writeFile_mdf.write(string + 'C2')
                            writeFile_mdf.write('\n')
                        if temp[0] == 'C2' and temp[5] == str(17) and temp[6] == 'p2':
                            # 连接尾部甲基C4的p2
                            writeFile_mdf.write(string + 'C1 H2 H3 C4')
                            writeFile_mdf.write('\n')

                        if temp[0] == 'C2' and temp[5] == str(17) and temp[6] == 'e2':
                            # 连接尾部甲基C4的e2
                            writeFile_mdf.write(string + 'H3 H4 C4 C1')
                            writeFile_mdf.write('\n')
                writeFile_mdf.write('\n' + '!' + '\n')
                writeFile_mdf.write('#symmetry' + '\n')
                writeFile_mdf.write('@periodicity 3 xyz' + '\n')
                writeFile_mdf.write('@group (P1)' + '\n')
                writeFile_mdf.write('\n' + '#end')


def create_mdf_file():
    list = os.listdir(path)
    print(list)
    for l in list:
        # *定义一个变量判断文件是否存在,path指代路径,str(i)指代文件夹的名字*
        isExists = os.path.exists(path + '/' + l + '/' + l + '.mdf')
        if not isExists:  # 判断如果文件不存在,则创建
            file = open(path + '/' + l + '/' + l + '.mdf', 'w')
            file.close()
            print("文件创建成功")
        else:
            print("%s 文件已经存在")
            continue  # 如果文件不存在,则继续上述操作,直到循环结束


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
        write_mdf(sequence)
        print("%s已读入" % sequence)
        # print(to_bin(i,16))


main()
# create_mdf_file()
# write_mdf()
