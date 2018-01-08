#!/usr/bin/env bash
# chkconfig: 2345 66 36
# /etc/rc.d/init.d/hive_history
# chkconfig --add hive_history
#
case "$1" in
  start)
        python /opt/pythonlib/hive_history_emit.py start
        ;;
  stop)
         python /opt/pythonlib/hive_history_emit.py stop
        ;;
  restart)
         python /opt/pythonlib/hive_history_emit.py restart
        ;;
  *)
  echo "Usage: python { start | stop | restart }"
  exit 1
esac
exit 0