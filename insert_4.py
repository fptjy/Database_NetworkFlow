# import mysql.connector  #链接数据库
#
# f = open('1000000_00000_20200610130000_4.txt')
# conn = mysql.connector.connect(user='root', password='',host='127.0.0.1',port='4000',database='1000000_00000_20200610130000')
# cursor = conn.cursor(prepared=True)
#         #next(f)  # 从文件的第二行开始读起
# for line in f:
#     line = line.strip('\n')
#     linelist = line.split(' ')
#     #print(linelist)
#     sql = "insert into IPv4 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
#     cursor.execute(sql, linelist)
#     conn.commit()
# cursor.close()
# conn.close()
#
#
#
# #用 mysql --host 127.0.0.1 --port 4000 -u root -p --local-infile
# #文件加载数据库 LOAD DATA local INFILE '/home/lishangsen/measurement/1000000_00000_20200610130000_4.txt' into TABLE IPv4;


import mysql.connector  # 链接数据库
import os

list_of_folder = ["/home/distkv/jk/go_client_test/ipv4/4_1/", "/home/distkv/jk/go_client_test/ipv4/4_2/",
                  "/home/distkv/jk/go_client_test/ipv4/4_3/", "/home/distkv/jk/go_client_test/ipv4/4_4/",
                  "/home/distkv/jk/go_client_test/ipv4/4_5/", "/home/distkv/jk/go_client_test/ipv4/4_6/",
                  "/home/distkv/jk/go_client_test/ipv4/4_7/", "/home/distkv/jk/go_client_test/ipv4/4_8/",
                  "/home/distkv/jk/go_client_test/ipv4/4_9/"]  # 存放ipv4数据的9个文件夹路径名称列表
for folder in list_of_folder:
    file_pathname = folder
    for filename in os.listdir(file_pathname):
        path = os.path.join(file_pathname, filename)
        #  print(path)
        f = open(path, 'r')

        conn = mysql.connector.connect(user='root', password='_2=bLZyf*1A%8T3K04', host='127.0.0.1', port='4100',
                                       database='1000000_00000_202001291400')
        cursor = conn.cursor(prepared=True)
        # next(f)  # 从文件的第二行开始读起
        for line in f:
            line = line.strip('\n')
            linelist = line.split(' ')
            if len(linelist) == 14:
                sql = "INSERT INTO IPv4 (Timestamp,etherdst,ethersrc,IPihl,iptos,iplen,ipid,ipfrag,ipttl,ipproto,ipdst,ipsrc,sport,dport) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                cursor.executemany(sql, [linelist])
                conn.commit()
        break
        cursor.close()
        conn.close()
