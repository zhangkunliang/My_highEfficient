# encoding=gbk

def to_bin(value, num):  # ʮ�������ݣ�������λ��
    bin_chars = ""
    temp = value
    for i in range(num):
        bin_char = bin(temp % 2)[-1]
        temp = temp // 2
        bin_chars = bin_char + bin_chars
    return bin_chars.upper()  # ���ָ��λ��Ķ������ַ���


out_bin = to_bin(2, 16)  # ����"0b"
print(out_bin)
