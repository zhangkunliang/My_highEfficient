# coding=utf-8
import os
import datetime
import time

path = r"./data/Log/"
Topic_resolve = path + "resolve" + ".csv"


# 根据传入解析规则（参数），判断解析是否积压,
def Is_Resolve_backlog(resolve_rule):
    # 判断解析积压
    pop_resolve = os.popen(
        "/opt/nsfocus/espc/deps/kafka/bin/kafka-consumer-groups.sh --describe --group sec_dev_log-"
        + resolve_rule + " --bootstrap-server 127.0.0.1:9092")
    print(pop_resolve)
    pop_resolve_info = pop_resolve.readlines()
    len_resolve = len(pop_resolve_info)
    print("已查询到%s条数据" % (len_resolve-3))
    # print(len_resolve)
    # 定义数组保存LAG数值
    resolve_LAG_arr = []
    for i_s in range(3, len_resolve):
        if '' != pop_resolve_info[i_s].split()[5] and pop_resolve_info[i_s].split()[5].isdigit():
            resolve_LAG = pop_resolve_info[i_s].split()[5]
            resolve_LAG_arr.append(resolve_LAG)
    # 累加LAG数组中的所有值
    resolve_LAG_sum = 0
    for LAG_num in resolve_LAG_arr:
        # print(LAG_num)
        resolve_LAG_sum += float(LAG_num)
    if not os.path.exists(Topic_resolve):
        with open(Topic_resolve, 'w') as topic_f:
            topic_f.write('time' + ',' + 'rule_name' + ',' + 'resolve')
            topic_f.write('\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + resolve_rule + ',' + str(
                resolve_LAG_sum))
            topic_f.close()
    else:
        with open(Topic_resolve, 'a') as topic_f:
            topic_f.write('\n' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ',' + resolve_rule + ',' + str(
                resolve_LAG_sum))
            topic_f.close()


def Is_Resolve_SetTimeinterval(time_interval):
    while True:
        Is_Resolve_backlog()
        time.sleep(time_interval)


def main():
    Is_Resolve_backlog(30)


if __name__ == '__main__':
    main()

