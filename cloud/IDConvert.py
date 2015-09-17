#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Copyright (C) 2013-2015 Runji
#

import sys
import os
import os.path
import MySQLdb

def upload_sen(sen_file):
    try:
        sen_h = open(sen_file, 'r')
        sen_dst = open("robot.ori2", 'w')
    except:
        print '文件打开失败'


    db_conn=MySQLdb.connect(host="localhost",user="root",passwd="runji",db="speech",charset="utf8")    
    c = db_conn.cursor()
    for line in sen_h:
        tmp = line.split(' ')
        sen = tmp[1].rstrip().decode('utf-8')
        if len(sen) == 0:
            continue
        c.execute('SELECT sen_id FROM senDB WHERE sen_txt = "%s";' % sen)
        rec = c.fetchall()
        if len(rec) > 0:
            dst_txt="%d %s\n"%(rec[0][0], sen)
#            print dst_txt
            sen_dst.writelines(dst_txt.encode('utf-8'))
#            continue
#       c.execute('insert into senDB (sen_txt) values("%s");' % sen)
#    db_conn.commit() #上传前，确保文本文件本身没有重复行！否则就得每条都commit
    sen_h.close()
    sen_dst.close()
if __name__ == '__main__':
    sen_file = sys.argv[1]
    upload_sen(sen_file)

