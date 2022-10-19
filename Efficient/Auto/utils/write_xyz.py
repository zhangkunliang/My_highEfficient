import os

path = r'E:\Study\pe-pp\ms\PE-PP'
path_xyz = r'E:\Study\pe-pp\ms\pepp_xyz'
testpath = r'E:\Study\pe-pp\ms\test'
testpath1 = r'E:\Study\pe-pp\ms\test1'


def to_bin(value, num):  # 十进制数据，二进制位宽
    bin_chars = ""
    temp = value
    for i in range(num):
        bin_char = bin(temp % 2)[-1]
        temp = temp // 2
        bin_chars = bin_char + bin_chars
    return bin_chars.upper()  # 输出指定位宽的二进制字符串


def create_xyz_dir():
    for i in range(65536):  # 创建65536个文件夹
        # *定义一个变量判断文件是否存在,path指代路径,str(i)指代文件夹的名字*
        isExists = os.path.exists(path_xyz + '/' + str(to_bin(i, 16)))
        if not isExists:  # 判断如果文件不存在,则创建
            os.makedirs(path_xyz + '/' + str(to_bin(i, 16)))

            print("%s 目录创建成功" % i)
        else:
            print("%s 目录已经存在" % i)
            continue  # 如果文件不存在,则继续上述操作,直到循环结束


def create_xyz_file():
    list = os.listdir(path_xyz)
    # print(list)
    for l in list:
        # *定义一个变量判断文件是否存在,path指代路径,str(i)指代文件夹的名字*
        isExists = os.path.exists(path_xyz + '/' + l + '/' + l + '.xyz')
        if not isExists:  # 判断如果文件不存在,则创建
            file = open(path_xyz + '/' + l + '/' + l + '.xyz', 'w')
            file.close()
            print("文件创建成功")
        else:
            print("%s 文件已经存在")
            continue  # 如果文件不存在,则继续上述操作,直到循环结束


def test():
    with open(r'/Users/zhangkunliang/ms/PE-PP' + '/' + '0000000000000000' + '/' + '0000000000000000' + '.car',
              'r') as readfile:
        with open(r'/Users/zhangkunliang/ms/pepp_xyz' + '/' + '0000000000000000' + '/' + '0000000000000000' + '.xyz',
                  'w') as copyfile:
            lines = readfile.readlines()
            print(len(lines))
            for l in range(5, len(lines) - 2):
                for i in range(0, 4):
                    new_line = lines[l].strip().split()[:4]
                    # print(new_line)
                    copyfile.write(new_line[i] + ' ')
                copyfile.write('\n')
            print('写入xyz成功')
            copyfile.close()


def write_xyz():
    count = 1
    listdir = os.listdir(path)
    for list in listdir:
        # print(list)
        with open(path + '/' + list + '/' + list + '.car', 'r') as readfile:
            with open(path_xyz + '/' + list + '/' + list + '.xyz', 'w') as copyfile:
                lines = readfile.readlines()
                # print(len(lines))
                copyfile.write(str(len(lines) - 7) + '\n')
                copyfile.write(' ' * 2 + list + '\n')
                for l in range(5, len(lines) - 2):
                    for i in range(0, 4):
                        new_line = lines[l].strip().split()[:4]
                        # print(new_line)
                        copyfile.write(new_line[i] + ' ' * 3)
                    copyfile.write('\n')
                print('已经成功写入了%s个xyz' % count)
                count += 1
                copyfile.close()


# create_xyz_dir()
# create_xyz_file()
write_xyz()
# test()
