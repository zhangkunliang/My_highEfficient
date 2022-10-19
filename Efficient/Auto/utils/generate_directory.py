# encoding=gbk
import os  # 导入模块

path = r'E:\Study\pe-pp\Sequence_num_sort_demo'  # 设置创建后文件夹存放的位置
final_path = r'E:\Study\pe-pp\Sequence_final_data'


def to_bin(value, num):  # 十进制数据，二进制位宽
    bin_chars = ""
    temp = value
    for i in range(num):
        bin_char = bin(temp % 2)[-1]
        # print(bin(temp % 2))
        temp = temp // 2
        bin_chars = bin_char + bin_chars
    return bin_chars.upper()  # 输出指定位宽的二进制字符串


for i in range(65536):  # 创建65536个文件夹
    # *定义一个变量判断文件是否存在,path指代路径,str(i)指代文件夹的名字*
    isExists = os.path.exists(final_path + '/' + str(to_bin(i, 16)))
    if not isExists:  # 判断如果文件不存在,则创建
        os.makedirs(final_path + '/' + str(to_bin(i, 16)))
        print("%s 目录创建成功" % i)
    else:
        print("%s 目录已经存在" % i)
        continue  # 如果文件不存在,则继续上述操作,直到循环结束

# out_bin = to_bin(11, 16)  # 不带"0b"
# print(out_bin)
