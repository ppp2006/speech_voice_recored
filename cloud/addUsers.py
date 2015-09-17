#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Copyright (C) 2013-2015 Runji
#

import sys
import os
import os.path
import MySQLdb

DB_FILE = 'speech.db'

def upload_sen(user_name_list):
    try:
        list_h = open(user_name_list, 'r')
    except:
        print '文件打开失败'
    db_conn=MySQLdb.connect(host="localhost",user="root",passwd="runji",db="speech",charset="utf8")    
    c = db_conn.cursor()
    for line in list_h:
        user_name = line.rstrip().decode('utf-8')
        if len(user_name) == 0:
            continue#跳过空行
        c.execute('SELECT user_id FROM userDB WHERE user_name = "%s";' % user_name)
        rec = c.fetchall()
        if len(rec) > 0:
            continue #用户已存在，不予录入
        c.execute('insert into userDB (user_name) values("%s");' % user_name)
    db_conn.commit() #上传前，确保文本文件本身没有重复行！否则就得每条都commit
    list_h.close()

if __name__ == '__main__':
    user_name_list = sys.argv[1]
    upload_sen(user_name_list)

