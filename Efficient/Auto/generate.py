# encoding=gbk
import os  # ����ģ��

path = r'E:\Study\pe-pp\Sequence_num'  # ���ô������ļ��д�ŵ�λ��


def to_bin(value, num):  # ʮ�������ݣ�������λ��
    bin_chars = ""
    temp = value
    for i in range(num):
        bin_char = bin(temp % 2)[-1]
        print(bin(temp % 2))
        temp = temp // 2
        bin_chars = bin_char + bin_chars
    return bin_chars.upper()  # ���ָ��λ��Ķ������ַ���


for i in range(65536):  # ����65536���ļ���
    # *����һ�������ж��ļ��Ƿ����,pathָ��·��,str(i)ָ���ļ��е�����*
    isExists = os.path.exists(path + '/' + str(to_bin(i, 16)))
    if not isExists:  # �ж�����ļ�������,�򴴽�
        os.makedirs(path + '/' + str(to_bin(i, 16)))
        print("%s Ŀ¼�����ɹ�" % i)
    else:
        print("%s Ŀ¼�Ѿ�����" % i)
        continue  # ����ļ�������,�������������,ֱ��ѭ������

# out_bin = to_bin(11, 16)  # ����"0b"
# print(out_bin)
