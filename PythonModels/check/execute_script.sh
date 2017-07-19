#!/bin/sh
source /etc/profile
python_file=$1
if [ -f "$python_file" ];then
    python $python_file
fi
