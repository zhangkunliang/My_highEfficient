# coding:utf-8
import os

path = r'E:\Study\pe-pp\Sequence_num'
test_path = r'E:\Study\pe-pp\test'

with open(r'../data/car/1111111111111111.car', 'r') as readFile_car:
    readFile_car_r = readFile_car.readlines()  # 读取文件内容行数
    # print(readFile_f)
    with open(r'../data/mdf/PolybaseP.mdf', 'r') as readFile_mdf:
        with open(r'../data/car/1111111111111111_test.mdf', 'w') as writeFile_mdf:
            readFile_mdf_r = readFile_mdf.readlines()
            # print(readFile_mdf_r[4])
            for i in range(0, 18):
                writeFile_mdf.write(readFile_mdf_r[i])
            writeFile_mdf.write('\n' + '@molecule' + ' ' + '1111111111111111')  # 此处写@molecule+ 文件名
            writeFile_mdf.write('\n')
            writeFile_mdf.write('\n')
            for j in range(5, len(readFile_car_r) - 2):
                d1 = {5: "C1 HL HM HN", 6: "CB", 7: "CB", 8: "CB",
                      9:  "CB C2 H1 H2", 10: "C1", 11: "C1",
                      12: "C1 C3 H3 H4", 13: "C2", 14: "C2",
                      15: "C2 C4 H5 H6", 16: "C3", 17: "C3",
                      18: "C3 C5 H7 H8", 19: "C4", 20: "C4",
                      21: "C4 C6 H9 HA", 22: "C5", 23: "C5",
                      24: "C5 C7 HB HC", 25: "C6", 26: "C6",
                      27: "C6 C8 HD HE", 28: "C7", 29: "C7",
                      30: "C7 C9 HF HG", 31: "C8", 32: "C8",
                      33: "C8 CA HH HI", 34: "C9", 35: "C9",
                      36: "C9 C3H6_2:C1 HJ HK", 37: "CA", 38: "CA",
                      len(readFile_car_r) - 6: "CA HL HM HN", len(readFile_car_r) - 4: "CB",
                      len(readFile_car_r) - 3: "CB", len(readFile_car_r) - 5: "CB",
                      len(readFile_car_r) - 36: "C3H6_17:C2 C2 H1 H2", len(readFile_car_r) - 35: "C1",
                      len(readFile_car_r) - 34: "C1",
                      len(readFile_car_r) - 33: "C1 C3 H3 H4", len(readFile_car_r) - 32: "C2",
                      len(readFile_car_r) - 31: "C2",
                      len(readFile_car_r) - 30: "C2 C4 H5 H6", len(readFile_car_r) - 29: "C3",
                      len(readFile_car_r) - 28: "C3",
                      len(readFile_car_r) - 27: "C3 C5 H7 H8", len(readFile_car_r) - 26: "C4",
                      len(readFile_car_r) - 25: "C4",
                      len(readFile_car_r) - 24: "C4 C6 H9 HA", len(readFile_car_r) - 23: "C5",
                      len(readFile_car_r) - 22: "C5",
                      len(readFile_car_r) - 21: "C5 C7 HB HC", len(readFile_car_r) - 20: "C6",
                      len(readFile_car_r) - 19: "C6",
                      len(readFile_car_r) - 18: "C6 C8 HD HE", len(readFile_car_r) - 17: "C7",
                      len(readFile_car_r) - 16: "C7",
                      len(readFile_car_r) - 15: "C7 C9 HF HG", len(readFile_car_r) - 14: "C8",
                      len(readFile_car_r) - 13: "C8",
                      len(readFile_car_r) - 12: "C8 CA HH HI", len(readFile_car_r) - 11: "C9",
                      len(readFile_car_r) - 10: "C9",
                      len(readFile_car_r) - 9: "C9 CB HJ HK", len(readFile_car_r) - 8: "CA",
                      len(readFile_car_r) - 7: "CA"
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
                             + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
                             )
                #  头尾甲基CH3+5个c2h4部分
                if 5 <= j <= 38 or len(readFile_car_r) - 36 <= j <= len(readFile_car_r) - 3:
                    if j == 36 and readFile_car_r[39].strip().split()[4] == 'C3H6':
                        writeFile_mdf.write(string + 'C9 C3H6_2:C1 HJ HK')  # 头部的5个C2H4尾部C原子连接的是C3H6的C
                        writeFile_mdf.write('\n')
                    elif j == 36 and readFile_car_r[39].strip().split()[4] == 'C2H4':
                        writeFile_mdf.write(string + 'C9 C2H4_2:C1 HJ HK')  # 头部的5个C2H4尾部C原子连接的是C2H4的C
                        writeFile_mdf.write('\n')
                    elif j == len(readFile_car_r) - 36 and readFile_car_r[len(readFile_car_r) - 37].strip().split()[4] == 'C3H6':
                        writeFile_mdf.write(string + 'C3H6_17:C2 C2 H1 H2')  # 尾部的5个C2H4头部C原子连接的是C3H6的C
                        writeFile_mdf.write('\n')
                    elif j == len(readFile_car_r) - 36 and readFile_car_r[len(readFile_car_r) - 37].strip().split()[4] == 'C2H4':
                        writeFile_mdf.write(string + 'C2H4_17:C2 C2 H1 H2')  # 尾部的5个C2H4头部C原子连接的是C2H4的C
                        writeFile_mdf.write('\n')
                    else:
                        writeFile_mdf.write(string+d1.get(j,' '))
                        writeFile_mdf.write('\n')
                elif j == 39 and temp[6] == 'p1':
                    # 连接头部甲基C4的p1
                    writeFile_mdf.write(string + 'H1 C2 C3 CbHn_1:CA')
                    writeFile_mdf.write('\n')
                elif j == 39 and temp[6] == 'e2':
                    # 连接头部甲基C4的e2
                    writeFile_mdf.write(string + 'H1 C2 H2 CbHn_1:CA')
                    writeFile_mdf.write('\n')
                elif j > 39 and int(temp[5]) <= 17:
                    # 1.txt.C2H4的C1
                    if temp[0] == 'C1' and temp[4] == 'C2H4':
                        writeFile_mdf.write(
                            string + 'H1 C2 H2' + ' ' + readFile_car_r[j - 1].strip().split()[4] + '_' + str(
                                int(temp[5]) - 1) + ':' + 'C2')
                        # writeFile_mdf.write(
                        #     string + 'H1 C2 H2' + ' ' + 'C2H4_' + str(int(temp[5]) - 1.txt) + ':' + 'C2')
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
                            string + 'C1 H3 H4' + ' ' + readFile_car_r[j + 3].strip().split()[4] + '_' + str(
                                int(temp[5]) + 1) + ':' + 'C1')
                        # writeFile_mdf.write(
                        #     string + 'C1 H3 H4' + ' ' + 'C2H4_' + str(int(temp[5]) + 1.txt) + ':' + 'C1')
                        writeFile_mdf.write('\n')
                    # 1.txt.C3H6的H4,H5,H6
                    if (temp[0] == 'H4' or temp[0] == 'H5' or temp[0] == 'H6') and temp[4] == 'C3H6':
                        writeFile_mdf.write(string + 'C3')
                        writeFile_mdf.write('\n')
                    # 2.C3H6的C1
                    if temp[0] == 'C1' and temp[4] == 'C3H6':
                        writeFile_mdf.write(
                            string + 'H1 C2 C3' + ' ' + readFile_car_r[j - 1].strip().split()[4] + '_' +
                            str(int(temp[5]) - 1) + ':' + 'C2')
                        # string + 'H1 C2 C3' + ' ' + 'C3H6_' + str(int(temp[5]) - 1.txt) + ':' + 'C2')  # 连接的上一个分子的C2
                        writeFile_mdf.write('\n')
                    # 3.C3H6的C2
                    if temp[0] == 'C2' and temp[4] == 'C3H6' and int(temp[5]) < 17:
                        writeFile_mdf.write(
                            string + 'C1 H2 H3' + ' ' + readFile_car_r[j + 7].strip().split()[4] + '_' +
                            str(int(temp[5]) + 1) + ':' + 'C1')
                        # string + 'C1 H2 H3' + ' ' + 'C3H6_' + str(int(temp[5]) + 1.txt) + ':' + 'C1')  # 连接的下一个分子的C1
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
                        writeFile_mdf.write(string + 'C1 H2 H3 CbHn_18:C1')
                        writeFile_mdf.write('\n')

                    if temp[0] == 'C2' and temp[5] == str(17) and temp[6] == 'e2':
                        # 连接尾部甲基C4的e2
                        writeFile_mdf.write(string + 'H3 H4 CbHn_18:C1 C1')
                        writeFile_mdf.write('\n')
            writeFile_mdf.write('\n' + '!' + '\n')
            writeFile_mdf.write('#symmetry' + '\n')
            writeFile_mdf.write('@periodicity 3 xyz' + '\n')
            writeFile_mdf.write('@group (P1)' + '\n')
            writeFile_mdf.write('\n' + '#end')


# 首次生成mdf文件，格式不正确，无法导出data
def write_mdf(sequence):
    with open(path + '/' + sequence + '/' + sequence + '.car', 'r') as readFile_car:
        readFile_car_r = readFile_car.readlines()  # 读取文件内容行数
        # print(readFile_f)
        with open(r'../data/mdf/PolybaseP.mdf', 'r') as readFile_mdf:
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
                                 + '1.txt.0000' + ' ' * 2 + '0.0000' + ' '
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
                        # 1.txt.C2H4的C1
                        if temp[0] == 'C1' and temp[4] == 'C2H4':
                            writeFile_mdf.write(
                                string + 'H1 C2 H2' + ' ' + readFile_car_r[j - 1].strip().split()[4] + '_' + str(
                                    int(temp[5]) - 1) + ':' + 'C2')
                            # writeFile_mdf.write(
                            #     string + 'H1 C2 H2' + ' ' + 'C2H4_' + str(int(temp[5]) - 1.txt) + ':' + 'C2')
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
                                string + 'C1 H3 H4' + ' ' + readFile_car_r[j + 3].strip().split()[4] + '_' + str(
                                    int(temp[5]) + 1) + ':' + 'C1')
                            # writeFile_mdf.write(
                            #     string + 'C1 H3 H4' + ' ' + 'C2H4_' + str(int(temp[5]) + 1.txt) + ':' + 'C1')
                            writeFile_mdf.write('\n')
                        # 1.txt.C3H6的H4,H5,H6
                        if (temp[0] == 'H4' or temp[0] == 'H5' or temp[0] == 'H6') and temp[4] == 'C3H6':
                            writeFile_mdf.write(string + 'C3')
                            writeFile_mdf.write('\n')
                        # 2.C3H6的C1
                        if temp[0] == 'C1' and temp[4] == 'C3H6':
                            writeFile_mdf.write(
                                string + 'H1 C2 C3' + ' ' + readFile_car_r[j - 1].strip().split()[4] + '_' +
                                str(int(temp[5]) - 1) + ':' + 'C2')
                            # string + 'H1 C2 C3' + ' ' + 'C3H6_' + str(int(temp[5]) - 1.txt) + ':' + 'C2')  # 连接的上一个分子的C2
                            writeFile_mdf.write('\n')
                        # 3.C3H6的C2
                        if temp[0] == 'C2' and temp[4] == 'C3H6' and int(temp[5]) < 17:
                            writeFile_mdf.write(
                                string + 'C1 H2 H3' + ' ' + readFile_car_r[j + 7].strip().split()[4] + '_' +
                                str(int(temp[5]) + 1) + ':' + 'C1')
                            # string + 'C1 H2 H3' + ' ' + 'C3H6_' + str(int(temp[5]) + 1.txt) + ':' + 'C1')  # 连接的下一个分子的C1
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

# main()
# create_mdf_file()
# write_mdf()
