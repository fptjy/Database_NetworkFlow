import mysql.connector  # 链接数据库
import os

list_of_folder = ["~/jk/go_client_test/ipv6/6_1/", "~/jk/go_client_test/ipv6/6_2/", "~/jk/go_client_test/ipv6/6_3/",
                  "~/jk/go_client_test/ipv6/6_4/", "~/jk/go_client_test/ipv6/6_5/"]  # 存放ipv6数据的5个文件夹路径名称列表
for folder in list_of_folder:
    file_pathname = "r" + folder
    for filename in os.listdir(file_pathname):
        path = os.path.join(file_pathname, filename)
        f = open(path, 'r')

        conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', port='4100',
                                       database='1000000_00000_20200610130000')
        cursor = conn.cursor(prepared=True)
        # next(f)  # 从文件的第二行开始读起
        for line in f:
            line = line.strip('\n')
            linelist = line.split(' ')
            # print(linelist)
            sql = "insert into IPv6 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(sql, linelist)
            conn.commit()
        cursor.close()
        conn.close()
