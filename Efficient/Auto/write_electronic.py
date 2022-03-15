with open(r'./data/PolybaseP.car', 'r') as readFile:
    head_f = readFile.readlines()  # 读取文件内容行数
    to_list = list('1111111111111111')  # 将文件名转为数组
    with open('./data/' + 'PolybaseP_2' + '.car', 'w') as copyfile:
        for i in range(0, 5):
            line_i = head_f[i]
            copyfile.write(line_i)
        for j in range(5, 157):
            temp = head_f[j].strip().split()
            if temp[0] == 'C1':
                temp[8] = '-0.053'
            if temp[0] == 'C3' or temp[0] == 'C4':
                temp[8] = '-0.159'
            if temp[0] == 'C2':
                temp[8] = '-0.106'
            if temp[7] == 'H':
                temp[8] = '0.053'
            if float(temp[1]) >= 10:
                value_1 = 6
            else:
                value_1 = 7
            if float(temp[3]) >= 0:
                value_3 = 4
            else:
                value_3 = 3
            if float(temp[5]) >= 10:
                value_5 = 5
            else:
                value_5 = 6
            if float(temp[8]) < 0:
                value_6 = 2
            else:
                value_6 = 3

            copyfile.write(
                temp[0] + ' ' * value_1 +
                temp[1] + ' ' * 4 +
                temp[2] + ' ' * value_3 +
                temp[3] + ' ' * 1 +
                temp[4] + ' ' * 1 +
                temp[5] + ' ' * value_5 +
                temp[6] + ' ' * 6 +
                temp[7] + ' ' * value_6 +
                temp[8] + '\n'
            )
        for k in range(157,159):
            copyfile.write('end'+'\n')
        copyfile.close()
