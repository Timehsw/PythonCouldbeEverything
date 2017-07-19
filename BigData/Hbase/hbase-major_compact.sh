#!/bin/sh

for region in `hadoop fs -ls /home/hbase/data/default | awk {'print $8'}`
do
    [[ ${region##*/} =~ ^\. ]] && continue
    [[ ${region##*/} =~ "SYSTEM" ]] || echo "major_compact '${region##*/}'" | hbase shell
    sleep 10
done

40 12 * * 2 /bin/sh /root/hbase-major-compact/hbase-major-compact.sh