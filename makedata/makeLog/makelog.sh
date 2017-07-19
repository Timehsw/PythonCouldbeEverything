#!/bin/bash


# Streaming 程序监听的目录
streaming_dir="/hsw/streaming"

# 清空旧数据
hadoop fs -rm "${streaming_dir}"'/tmp/*' > /dev/null 2>&1
hadoop fs -rm "${streaming_dir}"'/*' > /dev/null 2>&1

# 一直运行
while [ 1 ] ; do
    python ./MakeLogbyRandom.py > test.log

    # 给日志文件加时间戳,避免重名
    tmplog="access-`date '+%s'`.log"
    hadoop fs -put test.log ${streaming_dir}/tmp/$tmplog
    hadoop fs -mv ${streaming_dir}/tmp/$tmplog ${streaming_dir}/

    echo "`date +"%F %T"` put $tmplog to HDFS succeed"
    sleep 1
done

