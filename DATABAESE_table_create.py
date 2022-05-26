def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
 

import mysql.connector  #链接数据库
from mysql.connector import errorcode

DB_NAME = '1000000_00000_20200610130000'

TABLES = {}
# TABLES['IPv4'] = (
#     "CREATE TABLE `IPv4` ("
#     "  `P_ID` int  NOT NULL,"
#     "  `MAC_src`  VARCHAR(40)  NOT NULL,"
#     "  `MAC_dst`  VARCHAR(40)  NOT NULL,"
#     "  `Ether_type` int NOT NULL,"
#     "  `IPsrc`  VARCHAR(40)  NOT NULL DEFAULT '0',"
#     "  `IPdst`  VARCHAR(40)  NOT NULL DEFAULT '0',"
#     "  `sport`  int NOT NULL,"
#     "  `dport`  int NOT NULL,"
#     "  `IPversion`  int NOT NULL,"
#     "  `IPihl`  int UNSIGNED NOT NULL,"
#     "  `IPtos`  int UNSIGNED NOT NULL,"
#     "  `IPlen`  int UNSIGNED NOT NULL,"
#     "  `IPid`  int UNSIGNED NOT NULL,"
#     "  `IPflags`  int UNSIGNED NOT NULL,"
#     "  `IPfrag`  int UNSIGNED NOT NULL,"
#     "  `IPttl`  int UNSIGNED NOT NULL,"
#     "  `IPproto`  int UNSIGNED NOT NULL,"
#     "  `IPtime` VARCHAR(20) NOT NULL,"
#     "   PRIMARY KEY (`P_ID`)"
#
#     ") ")

TABLES['IPv6'] = (
    "CREATE TABLE `IPv6` ("
    "  `P_ID` int  NOT NULL,"
    "  `Timestamp` VARCHAR(40)  NOT NULL,"
    "  `ether.dst` VARCHAR(40)  NOT NULL,"
    "  `ether.src` VARCHAR(40)  NOT NULL,"
    "  `ipv6.tc`  int UNSIGNED NOT NULL,"
    "  `ipv6.fl`  int UNSIGNED NOT NULL,"
    "  `ipv6.plen`  int UNSIGNED NOT NULL,"
    "  `ipv6.nh`  int UNSIGNED NOT NULL,"
    "  `ipv6.hlim`  int UNSIGNED NOT NULL,"
    "  `ipv6.dst`  VARCHAR(40)  NOT NULL DEFAULT '0',"
    "  `ipv6.src`  VARCHAR(40)  NOT NULL DEFAULT '0',"
    "  `sport`  int UNSIGNED NOT NULL,"
    "  `dport`  int UNSIGNED NOT NULL,"
    "   PRIMARY KEY (`P_ID`)"
    ") ")

#创建数据库
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              port='4100',
                              database='test')
                            
#建立数据库1000000_00000_20200610130000 其中包含IPv4 与 IPv6两张表

cursor = cnx.cursor()
try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)


for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()