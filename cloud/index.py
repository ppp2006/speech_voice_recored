#!/usr/bin/env python
# -*- coding:utf-8 -*-
from mod_python import apache
from urllib import unquote
import os
import sys
import MySQLdb
import os.path

BASE_DIR = '/home/runji/projects/cloud/'
DB_NAME = 'speech'
DIGITS = 5

def formatId(id):
    return '0'*(DIGITS-len(id))+id

def getDbConn():
    db_conn = MySQLdb.connect(host="localhost",user="root",passwd="runji",db="speech",charset="utf8")
    return db_conn

def getSen(uid):
    db_file = os.path.join(BASE_DIR, DB_NAME)
    db_conn = getDbConn()
    c = db_conn.cursor()
    apache.log_error("get_sen uid = %s!"%uid, apache.APLOG_WARNING)
    c.execute('select sen_id,sen_txt from senDB where sen_id not in (select sen_id from recDB where user_id = %s) limit 1;' % uid)
    rec = c.fetchall()
    if len(rec) == 0:
        result = 'sen_id=0'
    else:
        sen_id, sen_txt = rec[0]
        apache.log_error("fuck txt = %s!"%sen_txt.decode('utf-8'), apache.APLOG_WARNING)
        result = u'sen_id=%s&sen_txt=%s'%(sen_id, sen_txt.decode('utf-8'))
    return result

def putSen(uid, sid, wav):
    db_file = os.path.join(BASE_DIR, DB_NAME)
    db_conn = getDbConn()
    c = db_conn.cursor()
    apache.log_error("put_sen uid = %s!"%uid, apache.APLOG_WARNING)
    c.execute('select fin from recDB where user_id = %s and sen_id = %s limit 1;'%(uid, sid))
    rec = c.fetchall()
    if len(rec) == 0:
        apache.log_error("not found record!", apache.APLOG_WARNING)
        c.execute('insert into recDB (user_id, sen_id, fin) values (%s, %s, "Y");'%(uid, sid))
        db_conn.commit()
    else:
        fin = rec[0]
        if fin == 'Y':
            apache.log_error("record exist already!", apache.APLOG_ERR)
            return '录音已存在'
        else:
            c.execute('update recDB set FIN = "Y" where user_id = %s and sen_id = %s;'%(uid, sid))
            db_conn.commit()
    wav_dir = os.path.join(BASE_DIR, 'voices/%s/'%uid)
    try:
        os.mkdir(wav_dir)
    except:
        pass
    on = os.path.join(wav_dir, '%s_%s.wav'%(formatId(uid), formatId(sid)))
    #on = os.path.join(wav_dir, '%s.wav'%uid)
    try:
        of = open(on, 'w')
        of.write(wav)
        of.close()
    except:
        apache.log_error(str(on), apache.APLOG_WARNING)
        
    return '上传成功！'

def login(user_name):
    db_conn = getDbConn()
    c = db_conn.cursor()
    apache.log_error("user_name = %s!"%user_name, apache.APLOG_WARNING)
    c.execute('select user_id from userDB where user_name = "%s" limit 1;'%user_name)
    rec = c.fetchall()
    if len(rec) == 0:
        apache.log_error("user_name not found!", apache.APLOG_WARNING)
	return '0'
    else:
        return str(rec[0][0]) #record 0 field 0, then convert from int to str

def handler(req):
    reload(sys) #set default encoding from ascii to utf-8
    sys.setdefaultencoding('utf-8')

    apache.log_error(req.args)

    params = {}
    for pair in req.args.split('&'):
        key, value = pair.split('=')
        params[key] = value
    if params['service'] == 'get_sen':
        req.content_type = "text/plain; charset=utf-8"
        uid = params['uid']
        sen = getSen(uid)
        req.write(sen)
        return apache.OK
    elif params['service'] == 'put_sen':
        wav = req.read()
        uid = params['uid']
        sid = params['sid']
        result = putSen(uid, sid, wav)
        req.content_type = "text/plain; charset=utf-8"
        req.write(result)
        return apache.OK
    elif params['service'] == 'login':
        user_name = unquote(params['user_name']).decode('utf-8')
        result = login(user_name)
        req.content_type = "text/plain; charset=utf-8"
        req.write(result)
        return apache.OK

