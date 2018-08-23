from ftplib import FTP
import datetime
import time
import re
import sched
import os

srcpath1 = '/M1810/DailyBuildM1810/app/海外版/Nougat_Flyme6_M1810/M1810_NF6_base/user'
srcpath = srcpath1.encode("utf-8").decode("latin1")   #解决UnicodeEncodeError: 'latin-1' codec can't encode characters in position 9-13: ordinal not in range(256)
#dirpath = r"\\10.0.10.2\\file_exchange\\版本\\flyme版本\\user"

def ftpconnect():
    ftp = FTP()
    ftp_server = '14.152.75.253'
    username = 'mzyude'
    password = '2018mzvPGhB2'
    ftp.connect(ftp_server,21)
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

def download_ftp_file():
    #格式化取到昨天的日期
    #d = (datetime.datetime.now()- datetime.timedelta(days=1)).strftime('%Y%m%d')
    #格式化取到今天的日期
    d = (datetime.datetime.now()).strftime('%Y%m%d')
    
    #调用ftp连接函数
    ftp = ftpconnect()
    bufsize = 1024
    ftp.cwd(srcpath)
    list = ftp.nlst()
    for name in list:
        #正则过滤掉其他日期
        L = re.match(d,name)
        if L:
            dirfile = os.path.join('v:\\flyme版本\\user', name)
            print (dirfile)
            flag = os.path.exists(dirfile)
            print(flag)
            
            if not os.path.exists(dirfile):
                os.makedirs(dirfile)
                os.makedirs(dirfile+'\\debugs')
                os.makedirs(dirfile+'\\firmware')
                os.makedirs(dirfile+'\\release_notes')

            #处理QFIL文件    
            if not os.path.exists(dirfile+'\\QFIL.zip') or not is_same_size(ftp, dirfile+'\\QFIL.zip', name + '//bin//QFIL.zip'):
                f = open(dirfile+'\\QFIL.zip','wb')
                filename = 'RETR '+ name + '//bin//QFIL.zip'
                print (filename)
                try:
                    ftp.retrbinary(filename,f.write,bufsize)
                except:
                    print ("QFIL.zip文件不存在")

            #处理debugs文件
            ftp.cwd(name+'//debugs')
            files = ftp.nlst()
            os.chdir(dirfile+'\\debugs')
            for file in files:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                if not os.path.exists(dirfile+'\\debugs\\'+file) or not is_same_size(ftp, dirfile+'\\debugs\\'+file,file):
                    f = open(file, 'wb')
                    filename = 'RETR ' + file
                    try:
                        ftp.retrbinary(filename,f.write,bufsize)
                    except:
                        print ("debugs文件不存在")

            #处理firmware文件
            ftp.cwd('..//firmware')
            files = ftp.nlst()
            os.chdir('..\\firmware')
            for file in files:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                if not os.path.exists(dirfile+'\\firmware\\'+file) or not is_same_size(ftp, dirfile+'\\firmware\\'+file,file):
                    f = open(file, 'wb')
                    filename = 'RETR ' + file
                    try:
                        ftp.retrbinary(filename,f.write,bufsize)
                    except:
                        print ("firmware文件不存在")

            #处理release_notes文件
            ftp.cwd('..//release_notes')
            files = ftp.nlst()
            os.chdir('..\\release_notes')
            for file in files:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                if not os.path.exists(dirfile+'\\release_notes\\'+file) or not is_same_size(ftp, dirfile+'\\release_notes\\'+file,file):
                    f = open(file, 'wb')
                    filename = 'RETR ' + file
                    try:
                        ftp.retrbinary(filename,f.write,bufsize)
                    except:
                        print ("release_notes文件不存在")
            
                    
            ftp.cwd('../..')
        
    ftp.quit()

if __name__ == '__main__':

   while True:
       download_ftp_file()
       time.sleep(3*60*60)



    
