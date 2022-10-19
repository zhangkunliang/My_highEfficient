# coding=utf-8
import os
import datetime
import time

import psutil

# 总路径
path = r"./data/component/"
# 汇总文件地址
summary = path + 'summary.csv'

# 组件命令
cmd_kafka = 'ps aux|grep deps/kafka | grep server.properties |grep -v grep|awk \'{print $2}\''
cmd_elas = 'ps aux|grep Elasticsearch|grep -v grep|awk \'{print $2}\''
cmd_postgresql = 'ps aux|grep postgresql |grep -v grep|awk \'{print $2}\''
cmd_proxy = 'ps aux|grep /opt/nsfocus/espc/deps/tomcat/proxy |grep -v grep|awk \'{print $2}\''
cmd_rest = 'ps aux|grep /opt/nsfocus/espc/deps/tomcat/conf/ |grep -v grep|awk \'{print $2}\''
cmd_streamsets = 'ps aux|grep streamsets-datacollector |grep -v grep | grep java|awk \'{print $2}\''
cmd_flink = 'ps aux|grep org.apache.flink.runtime |grep -v grep |grep java | xargs |awk \'{print $2}\''
cmd_event = 'ps aux|grep stream-event-service |grep -v grep |grep java|awk \'{print $2}\''


# 组件监控结果存放路径
def component_path(component):
    return path + "Process monitoring " + component + ".csv"


# 对应组件命令输出的进程号
def read_ProcessNum(command):
    return int(os.popen(command).read())


# 根据进程号读取数据
def process(command):
    return psutil.Process(read_ProcessNum(command))


# top命令下对应进程号查询的内容
def top_popen(command):
    return os.popen("top  -p {} -b -n 1".format(read_ProcessNum(command))).readlines()[-1].split()


# pidstat命令下对应进程号查询的内容
def pidstat_popen(command):
    return os.popen("pidstat -p  {} -d 1 10".format(read_ProcessNum(command))).readlines()[-1].split()


# 将pidstat命令下对应进程号查询内容第四和第五列值得总和
def res(command):
    return float(pidstat_popen(command)[3]) + float(pidstat_popen(command)[4])


# 计量单位转化
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


# 写文件方法
def write_file(component_name, command):
    if not os.path.exists(component_path(component_name)):
        with open(component_path(component_name), 'w') as component:
            component.write(
                "time" + ',' + "name" + ',' + "PID" + ',' + "CPU(%)" + ',' + "MEM" + ',' + "MEM(%)" + ',' + "IO(k/s)")
            temp = '\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + str(component_name) + ',' + str(
                top_popen(command)[0]) + ',' + str(process(command).cpu_percent(interval=1.5)) + ',' + str(
                measurement(str(top_popen(command)[5]))) + ',' + str(
                top_popen(command)[9]) + ',' + str(res(command))
            component.write(temp)
        with open(summary, 'w') as sum_data:
            sum_data.write(
                "time" + ',' + "name" + ',' + "PID" + ',' + "CPU(%)" + ',' + "MEM" + ',' + "MEM(%)" + ',' + "IO(k/s)")
            sum_data.write(temp)


    else:
        with open(component_path(component_name), 'a') as component:
            temp = '\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + str(component_name) + ',' + str(
                top_popen(command)[0]) + ',' + str(process(command).cpu_percent(interval=1.5)) + ',' + str(
                measurement(str(top_popen(command)[5]))) + ',' + str(
                top_popen(command)[9]) + ',' + str(res(command))
            component.write(temp)
        with open(summary, 'a') as sum_data:
            sum_data.write(temp)


# 监控方法
def monitor():
    write_file('kafka', cmd_kafka)
    write_file('Elasticsearch', cmd_elas)
    write_file('Postgresql', cmd_postgresql)
    write_file('Proxy', cmd_proxy)
    write_file('Rest', cmd_rest)
    write_file('Streamsets', cmd_streamsets)
    write_file('Flink', cmd_flink)
    write_file('StreamEvent', cmd_event)


def collection_SetTimeinterval(time_interval):
    while True:
        monitor()
        time.sleep(time_interval)


def main():
    collection_SetTimeinterval(5)


if __name__ == '__main__':
    main()
