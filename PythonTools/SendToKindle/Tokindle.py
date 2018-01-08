# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/12/29.
    推送本地书籍到kindle设备
    1.用watchdog监控本地目录(pip install watchdog)
    2.用smtplib给kindle发邮件
    3.书籍既是附件

    后台执行: nohup python Tokindle.py /Users/hushiwei/DailyKindleEBookLib > server.log 2>&1 &
'''

import sys, time, logging
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from SMTPClient import SMTPClient, Message

EXT_LIST = ['mobi', 'azw3']  # 可以添加azw3, epub 等任何格式
################   QQ邮箱  #######################
HOST_NAME = 'smtp.qq.com'
HOST_PORT = 465
USER_NAME = '694244330@qq.com'
USER_PASS = 'xxxxxxxxxxxxxx'
#################################################

KINDLE_MAILS = ['hushiwei@kindle.cn']  # 可以为一个list
FROM_NAME = '694244330@qq.com'
TO_NAME = 'Kindle Vorage'
MORNITOR_PATH = None


class FileSyncEvent(FileSystemEventHandler):
    def __init__(self):
        self._logger = logging.getLogger('server')

    def on_created(self, event):
        '''
        当有新文件在监控目录下生成的时候,执行一下逻辑
        :param event:
        :return:
        '''
        created_file = os.path.abspath(event.src_path)
        self._logger.info("Create file %s" % created_file)

        ext_name = os.path.splitext(created_file)[1]
        # 截取文件的后缀名,判断是否为kindle设备支持的格式
        if ext_name in ['.mobi']:
            self._logger.info("Send to kindle %s..." % created_file)
            send_to_kindle(created_file)

    def on_modified(self, event):
        self._logger.info("Modify file %s" % event.src_path)

    def on_moved(self, event):
        self._logger.info("Move file %s -> %s" % (event.src_path, event.dest_path))
        dest_file = os.path.abspath(event.dest_path)
        dest_dir = os.path.dirname(dest_file)

        if dest_dir != MORNITOR_PATH:
            return

        ext_name = os.path.splitext(dest_file)[1]
        if ext_name in [".mobi"]:
            self._logger.info("Send to kindle %s..." % dest_file)
            send_to_kindle(dest_file)


def send_to_kindle(file):
    '''
    发送到kindle的核心逻辑
    :param file: 电子书的绝对完整路径
    :return:
    '''
    logger = logging.getLogger("SendToKindle")

    ebook_name = os.path.basename(file)
    subject = "EBook %s" % ebook_name

    smpt_client = SMTPClient(HOST_NAME, HOST_PORT, USER_NAME, USER_PASS)
    msg = Message(FROM_NAME, TO_NAME, subject, 'Send EBook From Hushiwei`s Macbook Pro,Thanks!', with_attach=True)
    msg.attach(file)
    res, msg = smpt_client.send(KINDLE_MAILS, msg)
    if res == 1:
        logger.info("Send %s to kindle successfully!" % file)
    else:
        logger.error(msg)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    logger = logging.getLogger("Main")
    path = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ",")
    if not os.path.isdir(path):
        logger.info("%s is not a dir" % path)
        sys.exit()

    MORNITOR_PATH = path

    event_handler = FileSyncEvent()
    observe = Observer()
    observe.schedule(event_handler, path, recursive=True)
    logger.info("Start Sync Server,mornitoring folder: %s" % path)
    observe.start()
    logger.info("Begin to mornitor!")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observe.stop()
    observe.join()
