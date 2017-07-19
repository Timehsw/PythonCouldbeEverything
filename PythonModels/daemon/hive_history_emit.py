# coding=utf-8
# !/usr/bin/env python
__author__ = 'zenith'

import sys, os, json
import time, getpass

from daemon import Daemon


class HiveEmit(Daemon):
    hive_offset = 0
    hive_history_file = "/root/.hivehistory"

    def run(self):
        user = getpass.getuser()
        if not user == "root":
            self.hive_history_file = "/home/%s/.hivehistory" % getpass.getuser()
        while True:
            time.sleep(60)
            try:
                #读offset Begin
                offset_file = open(self.hive_offset_file, "r")
                dic = json.loads(offset_file.read())
                offset_file.close()
                self.hive_offset = int(dic.get(user, 0))
                #读offset End

                history_file = open(self.hive_history_file, "rb")
                if self.hive_offset < len(history_file.read()):
                    history_file.seek(self.hive_offset)
                    msg = history_file.read()
                    if msg:
                        #将文件写入新的文件里
                        target = open(self.hive_data_file, "ab")
                        target.write(msg)
                        target.close()
                        #更新offset
                        self.hive_offset += len(msg)
                        dic[user] = self.hive_offset

                        #写offset Begin
                        offset_file_w = open(self.hive_offset_file, "w")
                        offset_file_w.write(json.dumps(dic))
                        offset_file_w.close()
                        #写offset End

                history_file.close()
            except Exception:
                pass


if __name__ == "__main__":
    emit = HiveEmit('/tmp/daemon-hive-emit.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            emit.start()
        elif 'stop' == sys.argv[1]:
            emit.stop()
        elif 'restart' == sys.argv[1]:
            emit.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
