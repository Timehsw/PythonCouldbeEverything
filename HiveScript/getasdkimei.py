# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/4/18
"""

import subprocess

kupaipath = "/root/hsw/KupaiImei.log"
jinlipath = "/root/hsw/JinliImei.log"


def run_it(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,
                         stderr=subprocess.PIPE)
    print ('running:%s' % cmd)
    out, err = p.communicate()
    if p.returncode != 0:
        print ("Non zero exit code:%s executing: %s \nerr course ---> %s" % (p.returncode, cmd, err))
    return out


def getimei():
    # 酷派 20003a 20003b 60002a 81006a 81007a
    kupai_hql = "select imei_md5 from dmp.dmp_appboot where p_date='20170417' and channel_id in ('20003a','20003b','60002a','81006a','81007a') and length(imei)==15 and not imei_md5  like '35%' group by imei_md5 limit 500000;"

    exec_kupai_hql = "hive -e \"%s\" > %s" % (kupai_hql, kupaipath)
    run_it(exec_kupai_hql)

    print '#' * 40

    # 金立 20004a 20004b 20004c 81001a
    jinli_hql = "select imei_md5 from dmp.dmp_appboot where p_date='20170417' and channel_id in ('20004a','20004b','20004c','81001a') and length(imei)==15 and not imei_md5  like '35%' group by imei_md5 limit 500000;"
    exec_jinli_hql = "hive -e \"%s\" > %s" % (jinli_hql, jinlipath)
    run_it(exec_jinli_hql)


if __name__ == '__main__':
    getimei()
