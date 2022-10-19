#!/bin/bash
top -b -n 2 -d 1 | grep Cpu | sed -n '2p' | awk -F , {'print $4'} | awk {'print $1'}
#判断 /opt/nsfocs/espc/挂载点 是否存在 存在则获取 /opt/nsfocs/espc/XX挂载点集合 大小，如果 不存在 则获取 /opt大小
data_dir_list=`df -h | grep /opt/nsfocus/espc/ | awk -F "/opt/nsfocus/espc/" '{print $2}'`
if [ ${#data_dir_list} != 0 ]; then
   #存在
  total_count=0
  use_count=0
  for dir_name in $data_dir_list
  do
    dir_total_count=`df -BG /opt/nsfocus/espc/$dir_name | grep / | awk {'print $2'} | awk -F G {'print $1'}`
    let total_count=$total_count+$dir_total_count
    dir_use_count=`df -BG /opt/nsfocus/espc/$dir_name | grep / | awk {'print $3'} | awk -F G {'print $1'}`
    let use_count=$use_count+$dir_use_count
  done

  #再增加判断 /opt 是否在数据盘挂载 如果是则也统计/opt 反之忽略
  df -BG /opt > /dev/null 2>&1
  if [ $? != 0 ]; then
      # /opt 挂载点不存在 则直接返回结果
      echo $total_count
      echo $use_count
  else
      # /opt 挂载点存在 则需要再进一步区分/opt 是否在数据盘挂载
      root_disk=`df -h | grep /boot | awk '{print $1}' | cut -d "/" -f3 | cut -b 1-3`
      opt_disk=`df -BG  /opt  | grep /opt | awk '{print $1}' | cut -d "/" -f3 | cut -b 1-3`
      if [ $root_disk != '' -a $opt_disk != '' -a $root_disk != $opt_disk ];then
        opt_total_count=`df -BG /opt/ | grep / | awk {'print $2'} | awk -F G {'print $1'}`
        let total_count=$total_count+$opt_total_count
        opt_use_count=`df -BG /opt/ | grep / | awk {'print $3'} | awk -F G {'print $1'}`
        let use_count=$use_count+$opt_use_count
      fi
      echo $total_count
      echo $use_count
  fi

else
  # 不存在
  df -BG /opt/ | grep / | awk {'print $2'} | awk -F G {'print $1'}
  df -BG /opt/ | grep / | awk {'print $3'} | awk -F G {'print $1'}
fi