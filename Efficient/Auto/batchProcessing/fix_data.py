import sys

import numpy as np
import pandas as pd
import os  # 导入模块

path = r'E:\Study\pe-pp\Sequence_num'
test_path = r'E:\Study\pe-pp\test'
sort_path = r'E:\Study\pe-pp\Sequence_num_sort_demo'
final_path = r'E:\Study\pe-pp\Sequence_final'

# 增加头文件内容，包括原子数、类型数、键角等信息以及盒子大小


with open(r'../data/data/0000000011111111.data', 'r') as readFile_data:
    read_lines = readFile_data.readlines()
    # print(read_lines)
    # print(df)
    # print(df[0:5])
    atoms = 0  # 成功
    bonds = 0  # 成功
    angles = 0  # 成功
    dihedrals = 0  # 成功
    impropers = 0  # 成功
    atom_types = 0  # 成功
    bond_types = 0  # 成功
    angle_types = 0  # 成功
    dihedral_types = 0  # 成功
    improper_types = 0  # 成功
    max_atom_types_xset = 0  # 成功
    min_atom_types_xset = 0  # 成功
    max_atom_types_yset = 0  # 成功
    min_atom_types_yset = 0  # 成功
    max_atom_types_zset = 0  # 成功
    min_atom_types_zset = 0  # 成功
    with open(r'../data/data/0000000011111111.data', 'w') as writeFile_data:
        index = 0
        # print(len(read_lines))
        while index < len(read_lines):
            # 有空格行 所以列表会溢出,使用'\n'跳过空格行!!!
            if read_lines[index] != '\n' and read_lines[index].split()[0] == 'Atoms':
                max_atom_types = -100
                min_box_xsize = 1000
                max_box_xsize = -1000
                min_box_ysize = 1000
                max_box_ysize = -1000
                min_box_zsize = 1000
                max_box_zsize = -1000
                index += 2
                # print(index)
                # print(read_lines[index + 2])
                index_1 = index
                index_2 = index
                while read_lines[index] != '\n':
                    # 使用双指针划分范围
                    index += 1
                    index_2 += 1
                # print(index_2) 417
                for index in range(index_1, index_2):
                    max_atom_types = max(max_atom_types, int(read_lines[index].split()[2]))
                    max_box_xsize = max(max_box_xsize, float(read_lines[index].split()[4]))
                    min_box_xsize = min(min_box_xsize, float(read_lines[index].split()[4]))
                    min_box_ysize = min(min_box_ysize, float(read_lines[index].split()[5]))
                    max_box_ysize = max(max_box_ysize, float(read_lines[index].split()[5]))
                    min_box_zsize = min(min_box_zsize, float(read_lines[index].split()[6]))
                    max_box_zsize = max(max_box_zsize, float(read_lines[index].split()[6]))
                    index += 1
                # print(index)
                max_atom = index_2 - index_1
                # 赋值
                atoms = max_atom
                atom_types = max_atom_types
                max_atom_types_xset = '{:.9f}'.format(max_box_xsize + 5)
                min_atom_types_xset = '{:.9f}'.format(min_box_xsize - 5)
                max_atom_types_yset = '{:.9f}'.format(max_box_ysize + 50)
                min_atom_types_yset = '{:.9f}'.format(-max_box_ysize - 50)
                max_atom_types_zset = '{:.9f}'.format(max_box_zsize + 50)
                min_atom_types_zset = '{:.9f}'.format(min_box_zsize - 50)
                # print(round(min_atom_types_xset,5))
                # print('{:.9f}'.format(min_atom_types_xset))
                # print(min_atom_types_xset)
            elif read_lines[index] != '\n' and read_lines[index].split()[0] == 'Bonds':
                index += 2
                max_Bonds = -100
                max_bond_types = -100
                index_1 = index
                index_2 = index
                while read_lines[index] != '\n':
                    # 使用双指针划分范围
                    index += 1
                    index_2 += 1

                for index in range(index_1, index_2):
                    max_bond_types = max(max_bond_types, int(read_lines[index].split()[1]))
                    index += 1
                # print(index)
                # 赋值
                max_Bonds = index_2 - index_1
                bonds = max_Bonds
                bond_types = max_bond_types
                # print(bonds)
            elif read_lines[index] != '\n' and read_lines[index].split()[0] == 'Angles':
                index += 2
                max_Angles = -100
                max_Angles_types = -100
                index_1 = index
                index_2 = index
                while read_lines[index] != '\n':
                    # 使用双指针划分范围
                    index += 1
                    index_2 += 1
                for index in range(index_1, index_2):
                    max_Angles_types = max(max_Angles_types, int(read_lines[index].split()[1]))
                    index += 1
                # 赋值
                max_Angles = index_2 - index_1
                angles = max_Angles
                angle_types = max_Angles_types
                # print(angle_types)
            elif read_lines[index] != '\n' and read_lines[index].split()[0] == 'Dihedrals':
                index += 2
                max_dihedrals = -100
                max_dihedrals_types = -100
                index_1 = index
                index_2 = index
                while read_lines[index] != '\n':
                    # 使用双指针划分范围
                    index += 1
                    index_2 += 1
                for index in range(index_1, index_2):
                    max_dihedrals_types = max(max_dihedrals_types, int(read_lines[index].split()[1]))
                    index += 1
                # 赋值
                max_dihedrals = index_2 - index_1
                dihedrals = max_dihedrals
                dihedral_types = max_dihedrals_types
                # print(dihedral_types)
            elif read_lines[index] != '\n' and read_lines[index].split()[0] == 'Impropers':
                index += 2
                max_Impropers = -100
                max_Impropers_types = -100
                index_1 = index
                index_2 = index
                while read_lines[index] != '\n':
                    # 使用双指针划分范围
                    index += 1
                    index_2 += 1
                for index in range(index_1, index_2):
                    max_Impropers_types = max(max_Impropers_types, int(read_lines[index].split()[1]))
                    index += 1
                # 赋值
                max_Impropers = index_2 - index_1
                impropers = max_Impropers
                improper_types = max_Impropers_types
                # print(impropers)
            index += 1
        writeFile_data.write('LAMMPS data file. msi2lmp v3.9.9 / 05 Nov 2018 / CGCMM for ' + 'example' + '\n')
        writeFile_data.write('\n')
        writeFile_data.write(' ' * 4 + str(atoms) + ' ' + 'atoms' + '\n')
        writeFile_data.write(' ' * 4 + str(bonds) + ' ' + 'bonds' + '\n')
        writeFile_data.write(' ' * 4 + str(angles) + ' ' + 'angles' + '\n')
        writeFile_data.write(' ' * 4 + str(dihedrals) + ' ' + 'dihedrals' + '\n')
        writeFile_data.write(' ' * 4 + str(impropers) + ' ' + 'impropers' + '\n')
        writeFile_data.write('\n')
        writeFile_data.write(' ' * 3 + str(atom_types) + ' ' + 'atom' + ' ' + 'types' + '\n')
        writeFile_data.write(' ' * 2 + str(bond_types) + ' ' + 'bond' + ' ' + 'types' + '\n')
        writeFile_data.write(' ' * 2 + str(angle_types) + ' ' + 'angle' + ' ' + 'types' + '\n')
        writeFile_data.write(' ' * 2 + str(dihedral_types) + ' ' + 'dihedral' + ' ' + 'types' + '\n')
        writeFile_data.write(' ' * 2 + str(improper_types) + ' ' + 'improper' + ' ' + 'types' + '\n')
        writeFile_data.write('\n')
        writeFile_data.write(
            ' ' * 4 + str(min_atom_types_xset) + ' ' * 5 + str(max_atom_types_xset) + ' ' + 'xlo xhi' + '\n')
        writeFile_data.write(
            ' ' * 3 + str(min_atom_types_yset) + ' ' * 5 + str(max_atom_types_yset) + ' ' + 'ylo yhi' + '\n')
        writeFile_data.write(
            ' ' * 3 + str(min_atom_types_zset) + ' ' * 5 + str(max_atom_types_zset) + ' ' + 'zlo zhi' + '\n')
        writeFile_data.write('\n')
        index_behind = 0
        while index_behind < len(read_lines):
            if read_lines[index_behind] != '\n' and read_lines[index_behind].strip().split()[0] == 'Check':
                new_index = index_behind
                for i in range(new_index, len(read_lines)):
                    writeFile_data.write(read_lines[i])
                    index_behind += 1
                index_behind = new_index
            index_behind += 1


def write_data(sequence):
    with open(r'../data/data/example.data', 'r') as readFile_data:
        read_lines = readFile_data.readlines()
        # print(read_lines)
        # print(df)
        # print(df[0:5])
        atoms = 0  # 成功
        bonds = 0  # 成功
        angles = 0  # 成功
        dihedrals = 0  # 成功
        impropers = 0  # 成功
        atom_types = 0  # 成功
        bond_types = 0  # 成功
        angle_types = 0  # 成功
        dihedral_types = 0  # 成功
        improper_types = 0  # 成功
        max_atom_types_xset = 0  # 成功
        min_atom_types_xset = 0  # 成功
        max_atom_types_yset = 0  # 成功
        min_atom_types_yset = 0  # 成功
        max_atom_types_zset = 0  # 成功
        min_atom_types_zset = 0  # 成功
        with open(r'../data/data/example.data', 'w') as writeFile_data:
            index = 0
            # print(len(read_lines))
            while index < len(read_lines):
                # 有空格行 所以列表会溢出,使用'\n'跳过空格行!!!
                if read_lines[index] != '\n' and read_lines[index].split()[0] == 'Atoms':
                    max_atom_types = -100
                    min_box_xsize = 1000
                    max_box_xsize = -1000
                    min_box_ysize = 1000
                    max_box_ysize = -1000
                    min_box_zsize = 1000
                    max_box_zsize = -1000
                    index += 2
                    # print(index)
                    # print(read_lines[index + 2])
                    index_1 = index
                    index_2 = index
                    while read_lines[index] != '\n':
                        # 使用双指针划分范围
                        index += 1
                        index_2 += 1
                    # print(index_2) 417
                    for index in range(index_1, index_2):
                        max_atom_types = max(max_atom_types, int(read_lines[index].split()[2]))
                        max_box_xsize = max(max_box_xsize, float(read_lines[index].split()[4]))
                        min_box_xsize = min(min_box_xsize, float(read_lines[index].split()[4]))
                        min_box_ysize = min(min_box_ysize, float(read_lines[index].split()[5]))
                        max_box_ysize = max(max_box_ysize, float(read_lines[index].split()[5]))
                        min_box_zsize = min(min_box_zsize, float(read_lines[index].split()[6]))
                        max_box_zsize = max(max_box_zsize, float(read_lines[index].split()[6]))
                        index += 1
                    # print(index)
                    max_atom = index_2 - index_1
                    # 赋值
                    atoms = max_atom
                    atom_types = max_atom_types
                    max_atom_types_xset = '{:.9f}'.format(max_box_xsize + 5)
                    min_atom_types_xset = '{:.9f}'.format(min_box_xsize - 5)
                    max_atom_types_yset = '{:.9f}'.format(max_box_ysize + 50)
                    min_atom_types_yset = '{:.9f}'.format(-max_box_ysize - 50)
                    max_atom_types_zset = '{:.9f}'.format(max_box_zsize + 50)
                    min_atom_types_zset = '{:.9f}'.format(min_box_zsize - 50)
                    # print(round(min_atom_types_xset,5))
                    # print('{:.9f}'.format(min_atom_types_xset))
                    # print(min_atom_types_xset)
                elif read_lines[index] != '\n' and read_lines[index].split()[0] == 'Bonds':
                    index += 2
                    max_Bonds = -100
                    max_bond_types = -100
                    index_1 = index
                    index_2 = index
                    while read_lines[index] != '\n':
                        # 使用双指针划分范围
                        index += 1
                        index_2 += 1

                    for index in range(index_1, index_2):
                        max_bond_types = max(max_bond_types, int(read_lines[index].split()[1]))
                        index += 1
                    # print(index)
                    # 赋值
                    max_Bonds = index_2 - index_1
                    bonds = max_Bonds
                    bond_types = max_bond_types
                    # print(bonds)
                elif read_lines[index] != '\n' and read_lines[index].split()[0] == 'Angles':
                    index += 2
                    max_Angles = -100
                    max_Angles_types = -100
                    index_1 = index
                    index_2 = index
                    while read_lines[index] != '\n':
                        # 使用双指针划分范围
                        index += 1
                        index_2 += 1
                    for index in range(index_1, index_2):
                        max_Angles_types = max(max_Angles_types, int(read_lines[index].split()[1]))
                        index += 1
                    # 赋值
                    max_Angles = index_2 - index_1
                    angles = max_Angles
                    angle_types = max_Angles_types
                    # print(angle_types)
                elif read_lines[index] != '\n' and read_lines[index].split()[0] == 'Dihedrals':
                    index += 2
                    max_dihedrals = -100
                    max_dihedrals_types = -100
                    index_1 = index
                    index_2 = index
                    while read_lines[index] != '\n':
                        # 使用双指针划分范围
                        index += 1
                        index_2 += 1
                    for index in range(index_1, index_2):
                        max_dihedrals_types = max(max_dihedrals_types, int(read_lines[index].split()[1]))
                        index += 1
                    # 赋值
                    max_dihedrals = index_2 - index_1
                    dihedrals = max_dihedrals
                    dihedral_types = max_dihedrals_types
                    # print(dihedral_types)
                elif read_lines[index] != '\n' and read_lines[index].split()[0] == 'Impropers':
                    index += 2
                    max_Impropers = -100
                    max_Impropers_types = -100
                    index_1 = index
                    index_2 = index
                    while read_lines[index] != '\n':
                        # 使用双指针划分范围
                        index += 1
                        index_2 += 1
                    for index in range(index_1, index_2):
                        max_Impropers_types = max(max_Impropers_types, int(read_lines[index].split()[1]))
                        index += 1
                    # 赋值
                    max_Impropers = index_2 - index_1
                    impropers = max_Impropers
                    improper_types = max_Impropers_types
                    # print(impropers)
                index += 1
            writeFile_data.write('LAMMPS data file. msi2lmp v3.9.9 / 05 Nov 2018 / CGCMM for ' + sequence + '\n')
            writeFile_data.write('\n')
            writeFile_data.write(' ' * 4 + str(atoms) + ' ' + 'atoms' + '\n')
            writeFile_data.write(' ' * 4 + str(bonds) + ' ' + 'bonds' + '\n')
            writeFile_data.write(' ' * 4 + str(angles) + ' ' + 'angles' + '\n')
            writeFile_data.write(' ' * 4 + str(dihedrals) + ' ' + 'dihedrals' + '\n')
            writeFile_data.write(' ' * 4 + str(impropers) + ' ' + 'impropers' + '\n')
            writeFile_data.write('\n')
            writeFile_data.write(' ' * 3 + str(atom_types) + ' ' + 'atom' + ' ' + 'types' + '\n')
            writeFile_data.write(' ' * 2 + str(bond_types) + ' ' + 'bond' + ' ' + 'types' + '\n')
            writeFile_data.write(' ' * 2 + str(angle_types) + ' ' + 'angle' + ' ' + 'types' + '\n')
            writeFile_data.write(' ' * 2 + str(dihedral_types) + ' ' + 'dihedral' + ' ' + 'types' + '\n')
            writeFile_data.write(' ' * 2 + str(improper_types) + ' ' + 'improper' + ' ' + 'types' + '\n')
            writeFile_data.write('\n')
            writeFile_data.write(
                ' ' * 4 + str(min_atom_types_xset) + ' ' * 5 + str(max_atom_types_xset) + ' ' + 'xlo xhi' + '\n')
            writeFile_data.write(
                ' ' * 3 + str(min_atom_types_yset) + ' ' * 5 + str(max_atom_types_yset) + ' ' + 'ylo yhi' + '\n')
            writeFile_data.write(
                ' ' * 3 + str(min_atom_types_zset) + ' ' * 5 + str(max_atom_types_zset) + ' ' + 'zlo zhi' + '\n')
            writeFile_data.write('\n')
            index_behind = 0
            while index_behind < len(read_lines):
                if read_lines[index_behind] != '\n' and read_lines[index_behind].strip().split()[0] == 'Check':
                    new_index = index_behind
                    for i in range(new_index, len(read_lines)):
                        writeFile_data.write(read_lines[i])
                        index_behind += 1
                    index_behind = new_index
                index_behind += 1


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
        write_data(sequence)
        print("%s已读入" % sequence)
        # print(to_bin(i,16))
