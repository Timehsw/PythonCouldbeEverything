#!/bin/sh

function die ()
{
    echo >&2 "$@"
    echo "usage:"
    echo "       $0 check|split table_name [split_size]"
    exit 1
}

[[ "$#" -lt 2 ]] && die "at least 2 arguments required, $# provided"

COMMAND=$1
TABLE=$2
#超过1G就 split
SIZE="${3:-1073741824}"

function split()
{
    region_key=`python /root/hsw/hbase-scan.py -t hbase:meta -f "RowFilter (=, 'substring:$1')"`
    echo "split '$region_key'" | hbase shell
}

if [ "$COMMAND" != "check" ] ; then
    for region in `hadoop fs -ls /home/hbase/data/default/$TABLE | awk {'print $8'}`
    do
        [[ ${region##*/} =~ ^\. ]] && continue
        [[ `hadoop fs -du -s $region | awk {'print $1'}` -gt $SIZE ]] && split ${region##*/}
    done

    # check after split
    sleep 60
fi

for region in `hadoop fs -ls /home/hbase/data/default/$TABLE | awk {'print $8'}`
do
    [[ ${region##*/} =~ ^\. ]] && continue
    [[ `hadoop fs -du -s $region | awk {'print $1'}` -gt $SIZE ]] && echo "${region##*/} (`hadoop fs -du -s -h $region | awk {'print $1 $2'}`) is a huge region" || echo "${region##*/} (`hadoop fs -du -s -h $region | awk {'print $1 $2'}`
) is a small region"
done
