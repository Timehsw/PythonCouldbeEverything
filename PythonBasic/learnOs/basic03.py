# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/4/9
"""
'''
目录浏览模块
返回该目录下的所有目录
返回该目录下的所有文件
返回该目录下的所有文件的路径
'''
import os

class diskwalk(object):
    """API for getting directory walking collections"""
    def __init__(self,path):
        self.path=path

    def enumeratePaths(self):
        """Returns the path to all the files in a directory as a list"""
        path_collection=[]
        for dirpath,dirnames,filenames in os.walk(self.path):
            for file in filenames:
                fullpath=os.path.join(dirpath,file)
                path_collection.append(fullpath)
        return path_collection

    def enumerateFiles(self):
        """Returns all the files in a directory as a list"""
        file_collection=[]
        for dirpath,dirnames,filenames in os.walk(self.path):
            for file in filenames:
                file_collection.append(file)
        return file_collection

    def enumerateDir(self):
        """Returns all the directories in a directory as a list"""
        dir_collection=[]
        for dirpath,dirnames,filenames in os.walk(self.path):
            for dir in dirnames:
                dir_collection.append(dir)
        return dir_collection

demo=diskwalk('/Users/hushiwei/learnpython')
print demo.enumerateDir()
print demo.enumerateFiles()
print demo.enumeratePaths()