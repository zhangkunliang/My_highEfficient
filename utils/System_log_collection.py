# _*_coding=utf-8 _*
import os
import datetime
import time

path = r"./data/system/"

CPU = path + "monitor_CPU" + ".csv"
Memory = path + "monitor_Memory" + ".csv"
Disk = path + "monitor_Disk" + ".csv"
IO = path + "monitor_IO" + ".csv"
cpu_temp = path + "cpu_temp" + ".txt"
swap = path + "swap" + ".csv"


def measurement(new_str):
    if 'g' in new_str:
        new_str = str(int(float(new_str[:-1]) * 1024)) + 'm'
        return new_str
    elif 't' in new_str:
        new_str = str(int(float(new_str[:-1]) * 1024 * 1024)) + 'm'
        return new_str
    elif 'm' in new_str:
        new_str = str(int(new_str[:-1])) + 'm'
        return new_str
    else:
        new_str = str(int(float(new_str[:-1]) / 1024)) + 'm'
        return new_str


# 统计方法
def statistic():
    # 统计CPU使用情况
    print('-----------------------------cpu---------------------------------------')
    pop_cpu = os.popen("top -b -n 2 -d 1 |grep Cpu | sed -n \'2p\'")
    cpu_info = pop_cpu.read().decode('unicode-escape')
    print(cpu_info)
    cpu_info_rate = cpu_info.split('\n')[0].split()
    print(cpu_info_rate)
    if not os.path.exists(CPU):
        with open(CPU, 'w') as cpu_f:
            cpu_f.write('time' + ',' + 'USR%+SYS%')
            cpu_f.write('\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + str(
                float(cpu_info_rate[1]) + float(cpu_info_rate[3])))
            cpu_f.close()
    else:
        with open(CPU, 'a') as cpu_f:
            cpu_f.write('\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + str(
                float(cpu_info_rate[1]) + float(cpu_info_rate[3])))
            cpu_f.close()
    # 统计内存使用情况
    print('-----------------------------Memory---------------------------------------')
    pop_memory = os.popen("free -m")
    mem_info = pop_memory.read()
    print(mem_info)
    Mem = mem_info.split('\n')[1].split()
    print(Mem)
    if not os.path.exists(Memory):
        with open(Memory, 'w') as mem_f:
            mem_f.write(
                'time' + ',' + 'total' + ',' + 'used' + ',' + 'free' + ',' + 'shared' + ',' + 'buff/cache'
                + ',' + 'available')
            mem_f.write('\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + str(Mem[1])
                        + ',' + str(Mem[2]) + ',' + str(Mem[3]) + ',' + str(Mem[4]) + ',' + str(Mem[5]) + ',' + str(
                Mem[6]))
            mem_f.close()
    else:
        with open(Memory, 'a') as mem_f:
            mem_f.write('\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + str(Mem[1])
                        + ',' + str(Mem[2]) + ',' + str(Mem[3]) + ',' + str(Mem[4]) + ',' + str(Mem[5]) + ',' + str(
                Mem[6]))
            mem_f.close()
    Mem_swap = mem_info.split('\n')[2].split()
    if not os.path.exists(swap):
        with open(swap, 'w') as swap_f:
            swap_f.write('time' + ',' + 'total' + ',' + 'used' + ',' + 'free')
            swap_f.write(
                '\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + str(Mem_swap[1]) + ',' + str(
                    Mem_swap[2]) + ',' + str(Mem_swap[3]))
            swap_f.close()
    else:
        with open(swap, 'a') as swap_f:
            swap_f.write(
                '\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + str(Mem_swap[1]) + ',' + str(
                    Mem_swap[2]) + ',' + str(Mem_swap[3]))
            swap_f.close()
    # 统计硬盘使用情况
    print('-----------------------------disk---------------------------------------')
    pop_disk = os.popen("sh ./getStat.sh")
    disk_info_cur = pop_disk.readlines()
    # len_mem = len(disk_info_cur)
    # print(len_mem)
    print(disk_info_cur)
    if not os.path.exists(Disk):
        with open(Disk, 'w') as disk_f:
            disk_f.write(
                'Time' + ',' + 'Avail%' + ',' + 'Size' + ',' + 'Used')
            disk_f.write(
                '\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + disk_info_cur[0].strip() + ',' +
                disk_info_cur[1].strip() + ',' + disk_info_cur[2].strip())
            disk_f.close()
    else:
        with open(Disk, 'a') as disk_f:
            disk_f.write(
                '\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + disk_info_cur[0].strip() + ',' +
                disk_info_cur[1].strip() + ',' + disk_info_cur[2].strip())
            disk_f.close()
    # 统计IO使用情况
    print('-----------------------------IO---------------------------------------')
    pop_io = os.popen("iostat")
    # 磁盘信息
    pop_disk_cur = os.popen("df -h")
    IO_info_cur = pop_io.readlines()
    disk_info_cur = pop_disk_cur.readlines()
    # iostat后长度
    len_mem = len(IO_info_cur)
    # df -h后长度
    len_disk = len(disk_info_cur)
    opt_disk = ''
    for i in range(0, len_disk):
        if disk_info_cur[i].split()[-1] == '/opt':
            # 获取/opt下磁盘名称
            opt_disk = disk_info_cur[i].split()[0][-4:-1]
    if not os.path.exists(IO):
        with open(IO, 'w') as io_f:
            io_f.write(
                'Time' + ',' + 'Device' + ',' + 'tps' + ',' + 'kB_read/s' + ',' + 'kB_wrtn/s' + ',' + 'kB_read' + ','
                + 'kB_wrtn')
            for i in range(6, len_mem - 1):
                if IO_info_cur[i].split()[0] == opt_disk:
                    io_f.write(
                        '\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + IO_info_cur[i].split()[0]
                        + ',' + IO_info_cur[i].split()[1] + ',' + IO_info_cur[i].split()[2] + ',' +
                        IO_info_cur[i].split()[3] + ',' + IO_info_cur[i].split()[4] + ',' + IO_info_cur[i].split()[5])
            io_f.close()
    else:
        with open(IO, 'a') as io_f:
            for i in range(6, len_mem - 1):
                if IO_info_cur[i].split()[0] == opt_disk:
                    io_f.write(
                        '\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + IO_info_cur[i].split()[0]
                        + ',' + IO_info_cur[i].split()[1] + ',' + IO_info_cur[i].split()[2] + ',' +
                        IO_info_cur[i].split()[3] + ',' + IO_info_cur[i].split()[4] + ',' + IO_info_cur[i].split()[5])
            io_f.close()


def statistic_SetTimeinterval(time_interval):
    while True:
        statistic()
        time.sleep(time_interval)


def main():
    statistic_SetTimeinterval(30)


if __name__ == '__main__':
    main()
