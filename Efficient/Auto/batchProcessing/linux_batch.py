# coding=utf-8
import os

os.chdir('../PPE/1111111111111111')
print(os.getcwd())
os.system('bsub -a intelmpi -e error.txt -o output.txt -J 1111111111111111 -i TC.in -n 24 mpirun.lsf /home/anmeng/WORK1/lammps-3Mar20/src/lmp_mpi')

def to_bin(value, num):  # 十进制数据，二进制位宽
    bin_chars = ""
    temp = value
    for i in range(num):
        bin_char = bin(temp % 2)[-1]
        temp = temp // 2
        bin_chars = bin_char + bin_chars
    return bin_chars.upper()  # 输出指定位宽的二进制字符串



# def main():
#     for i in range(0, 65536):
#         sequence = to_bin(i, 16)
#         modification(sequence)
#         print("%s已读入" % sequence)
#         # print(to_bin(i,16))
