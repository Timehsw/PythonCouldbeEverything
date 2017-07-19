# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/4/9
"""
'''
删除模块
'''
import os


class Delete(object):
    """Delete Methods For File Objects"""

    def __init__(self, file):
        self.file = file

    def interactive(self):
        """interactice deletion mode"""
        input = raw_input("Do you really want to delete %s [N]/Y" % self.file)
        if input.upper():
            print "DELETING: %s" % self.file
            status = os.remove(self.file)
        else:
            print "Skipping: %s" % self.file
        return

    def dryrun(self):
        """simulatin mode for deletion"""
        print "Dry Run: %s [NOT DELETED]" % self.file
        return

    def delete(self):
        """Performs a delete on a file ,with additional conditions"""
        print "DELETING: %s" % self.file
        try:
            status=os.remove(self.file)
        except Exception,err:
            print err
            return status
