# coding=utf-8
import os
import datetime
import time

path = r"./data/"
Topic_access = path + "access" + ".csv"
Topic_parse = path + "parse" + ".csv"


# 判断入库是否积压
def Is_Storage_backlog():
    with open('config.txt', 'r') as config:
        read_config = config.readlines()
        config_arr = []
        for index in range(0, len(read_config)):
            config_arr.append(read_config[index].strip())
        # print(config_arr)
    # 获取所有消费组
    group = os.popen(
        "/opt/nsfocus/espc/deps/kafka/bin/kafka-consumer-groups.sh --bootstrap-server 127.0.0.1:9092 --list")
    read_group = group.readlines()
    group_arr = []
    for i in range(0, len(read_group)):
        group_i = read_group[i].strip()
        group_arr.append(group_i)
    # 做差集，保存group中出现不在配置文件中出现的组名
    topic_arr = list(set(group_arr).difference(set(config_arr)))
    len_topic_arr = len(topic_arr)
    # print(topic_arr)
    # print(len_topic_arr)
    # 遍历每个消费组，统计各消费组下topic的积压情况(LAG)
    for index in range(0, len_topic_arr):
        if not topic_arr[index].startswith('ruleEngine'):
            # 每个消费组下的topic信息
            topic_popen = os.popen(
                '/opt/nsfocus/espc/deps/kafka/bin/kafka-consumer-groups.sh --describe --group ' + topic_arr[
                    index] + ' --bootstrap-server 127.0.0.1:9092')
            read_topic_popen = topic_popen.readlines()
            # 读取topic消费信息文本长度
            len_read_topic_popen = len(read_topic_popen)

            # 先写入表头
            if not os.path.exists(Topic_access):
                with open(Topic_access, 'w') as access:
                    access.write('Time' + ',' + 'Group_name' + ',' + 'Topic_name' + ',' + 'LAG_access')
                    access.close()
            if not os.path.exists(Topic_parse):
                with open(Topic_parse, 'w') as parse:
                    parse.write('Time' + ',' + 'Group_name' + ',' + 'Topic_name' + ',' + 'LAG_parse')
                    parse.close()
            # 每个group下的消费信息文本索引，从第三行开始读入
            topic_index = 2
            # 再次存入
            while topic_index < len_read_topic_popen:
                if not read_topic_popen[topic_index].split()[1].endswith('_access') and not \
                        read_topic_popen[topic_index].split()[1].endswith('_parse'):
                    topic_index += 5
                    continue
                if read_topic_popen[topic_index].split()[1].endswith('_access') and \
                        read_topic_popen[topic_index].split()[5] != '-':
                    # 初始化入库积压
                    LAG_access_temp = 0
                    if os.path.exists(Topic_access):
                        with open(Topic_access, 'a') as access:
                            # print(read_topic_popen[topic_index].split()[1])
                            # topic若以_access结尾，则需要记录为入库积压
                            temp_index_access = topic_index  # 记录此时的索引号,每五行读取一个topic
                            while topic_index < temp_index_access + 5:
                                # LAG值不为'-',且topic以_access结尾
                                LAG_access_temp += float(read_topic_popen[topic_index].split()[5])
                                print(read_topic_popen[topic_index].strip().split()[1])
                                topic_index += 1
                            print(topic_index)
                            # 累加五次LAG_access之后判断是否为0，不为0则存入
                            if float(LAG_access_temp) == 0:
                                continue
                            else:
                                access.write(
                                    '\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + topic_arr[
                                        index] + ',' +
                                    read_topic_popen[topic_index-1].strip().split()[1] + ',' + str(LAG_access_temp))
                                # 将LAG_access_temp重新置为0
                            access.close()
                elif read_topic_popen[topic_index].split()[1].endswith('_parse') and \
                        read_topic_popen[topic_index].split()[5] != '-':
                    # 初始化解析积压
                    LAG_parse_temp = 0
                    if os.path.exists(Topic_parse):
                        with open(Topic_parse, 'a') as parse:
                            # topic若以_parse结尾，则需要记录为解析积压
                            temp_index_parse = topic_index  # 记录此时的索引号,每五行读取一个topic
                            while topic_index < temp_index_parse + 5:
                                # LAG值不为'-',且topic以_parse结尾
                                LAG_parse_temp += float(read_topic_popen[topic_index].split()[5])
                                print(read_topic_popen[topic_index].strip().split()[1])
                                topic_index += 1
                            print(topic_index)
                            # 累加五次LAG_parse之后判断是否为0，不为0则存入
                            if float(LAG_parse_temp) == 0:
                                continue
                            else:
                                parse.write(
                                    '\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + topic_arr[
                                        index] + ',' +
                                    read_topic_popen[topic_index-1].strip().split()[1] + ',' + str(LAG_parse_temp))
                                # 将LAG_parse_temp重新置为0
                            parse.close()


def Is_Storage_SetTimeinterval(time_interval):
    while True:
        Is_Storage_backlog()
        time.sleep(time_interval)


def main():
    Is_Storage_SetTimeinterval(300)


if __name__ == '__main__':
    main()
