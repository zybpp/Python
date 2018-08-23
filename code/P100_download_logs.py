#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:zhangyanbin

from ftplib import FTP
import datetime
import time
import re
import sched
import os

NATIVE_SERVER = r'net use h: "\\10.0.10.2\移动终端bg软件部\02_项目资料\联想\P100&P101\LOG\Logs" "zyb.2017" /user:"zhangyanbin"'
CLIENT_FTP_SERVER = "119.233.254.21"
CLIENT_USERNAME = "lenovoFT"
CLIENT_PASSWORD = "ftplenovo"
srcpath = "/6.Project/Tab5 10Plus/Logs"
#dirpath = r"\\10.0.10.2\移动终端bg软件部\02_项目资料\联想\P100&P101\LOG\Logs"
files_list = []

def ftpconnect(ftp_server,username,password):
    ftp = FTP()
    ftp.connect(ftp_server)
    ftp.login(username,password)
    print (ftp.getwelcome())
    return ftp

def is_same_size(ftp, localfile, remotefile):
    localfile_size = os.path.getsize(localfile)
    print (localfile_size)

    try:
        remotefile_size = ftp.size(remotefile)
        print (remotefile_size)
    except:
        remotefile_size = -1
        
    if remotefile_size == localfile_size:
        return 1
    else:
        return 0

def get_client_files_list(client_ftp):
    dir_list = []
    client_ftp.dir(dir_list.append)
    #print(dir_list)
    for i in dir_list:
        # try:
        print(i)
        # except UnicodeEncodeError:
        #     print("zhangyanbin1111")
        #     i.encode("utf-8")
        #     print(i.decode("utf-8"))
        if i.startswith("d"):
            path = client_ftp.pwd() + "/" + re.findall("\d.:\d. (.+)",i)[0]
            print(path)
            #print(repr(path))
            client_ftp.cwd(path)
            get_client_files_list(client_ftp)
        else:
            path = client_ftp.pwd() + "/" + re.findall("\d.:\d. (.+)",i)[0]
            str = re.sub("\d.:\d. (.+)",path,i)
            #print(str)
            print(str)
            files_list.append(str)
            #client_ftp.cwd("..")
            #print(files_list)
    client_ftp.cwd("..")

def download_ftp_file():
    current_date = datetime.date.today()
    print(current_date)
    d = (datetime.datetime.now()).strftime('%Y%m%d')
    print(d)
    
    #调用ftp连接函数
    os.system(r"net use h: /del /y")
    os.system(NATIVE_SERVER)
    #os.system(r"net view \\10.0.10.2")
    print(os.getcwd())
    print(os.listdir("h:"))
    client_ftp = ftpconnect(CLIENT_FTP_SERVER,CLIENT_USERNAME,CLIENT_PASSWORD)
    bufsize = 1024
    print(srcpath)
    client_ftp.cwd(srcpath)
    print(client_ftp.pwd())
    if client_ftp.pwd() == srcpath:
        get_client_files_list(client_ftp)
    print(files_list)
    # for name in list:
    #     #正则过滤掉其他日期
    #     L = re.match(d,name)
    #     if L:
    #         dirfile = os.path.join('v:\\flyme版本\\user', name)
    #         print (dirfile)
    #         flag = os.path.exists(dirfile)
    #         print(flag)
    #
    #         if not os.path.exists(dirfile):
    #             os.makedirs(dirfile)
    #             os.makedirs(dirfile+'\\debugs')
    #             os.makedirs(dirfile+'\\firmware')
    #             os.makedirs(dirfile+'\\release_notes')
    #
    #         #处理QFIL文件
    #         if not os.path.exists(dirfile+'\\QFIL.zip') or not is_same_size(ftp, dirfile+'\\QFIL.zip', name + '//bin//QFIL.zip'):
    #             f = open(dirfile+'\\QFIL.zip','wb')
    #             filename = 'RETR '+ name + '//bin//QFIL.zip'
    #             print (filename)
    #             try:
    #                 ftp.retrbinary(filename,f.write,bufsize)
    #             except:
    #                 print ("QFIL.zip文件不存在")
    #
    #         #处理debugs文件
    #         ftp.cwd(name+'//debugs')
    #         files = ftp.nlst()
    #         os.chdir(dirfile+'\\debugs')
    #         for file in files:
    #             if not os.path.exists(dirfile+'\\debugs\\'+file) or not is_same_size(ftp, dirfile+'\\debugs\\'+file,file):
    #                 f = open(file, 'wb')
    #                 filename = 'RETR ' + file
    #                 try:
    #                     ftp.retrbinary(filename,f.write,bufsize)
    #                 except:
    #                     print ("debugs文件不存在")
    #
    #         #处理firmware文件
    #         ftp.cwd('..//firmware')
    #         files = ftp.nlst()
    #         os.chdir('..\\firmware')
    #         for file in files:
    #             if not os.path.exists(dirfile+'\\firmware\\'+file) or not is_same_size(ftp, dirfile+'\\firmware\\'+file,file):
    #                 f = open(file, 'wb')
    #                 filename = 'RETR ' + file
    #                 try:
    #                     ftp.retrbinary(filename,f.write,bufsize)
    #                 except:
    #                     print ("firmware文件不存在")
    #
    #         #处理release_notes文件
    #         ftp.cwd('..//release_notes')
    #         files = ftp.nlst()
    #         os.chdir('..\\release_notes')
    #         for file in files:
    #             if not os.path.exists(dirfile+'\\release_notes\\'+file) or not is_same_size(ftp, dirfile+'\\release_notes\\'+file,file):
    #                 f = open(file, 'wb')
    #                 filename = 'RETR ' + file
    #                 try:
    #                     ftp.retrbinary(filename,f.write,bufsize)
    #                 except:
    #                     print ("release_notes文件不存在")
    #
    #
    #         ftp.cwd('../..')
    #
    client_ftp.quit()
    os.system(r"net use h: /del /y")

if __name__ == '__main__':
   while True:
       download_ftp_file()
       time.sleep(3*60*60)



    
