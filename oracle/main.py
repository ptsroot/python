# -*- coding:utf-8 -*-
import cx_Oracle as oracle
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# 测试环境
ORACLE_HOST = '222.85.147.140:12561'
ORACLE_USERNAME = 'xiaoi'
ORACLE_PASSWORD = 'xiaoi123'
ORACLE_SERVICE_NAME = 'ORCL'
ORACLE_TABLE_NAME_TEST = 'FS_12345_DATA'
ORACLE_CONN_STR_TEST = ORACLE_USERNAME+'/'+ORACLE_PASSWORD+'@'+ORACLE_HOST+'/'+ORACLE_SERVICE_NAME
ORACLE_CONN_STR = ORACLE_CONN_STR_TEST
ORACLE_TABLE_NAME = ORACLE_TABLE_NAME_TEST

def exec_sql(sql):
    conn = oracle.connect(ORACLE_CONN_STR)
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    conn.close()
    return result


def get_data_from_oracle():
    sql = 'select "id", "text" from ' + ORACLE_TABLE_NAME + ' where rownum <= 300'
    result = exec_sql(sql)
    return result

if __name__ == "__main__":
    ret = get_data_from_oracle()
    for item in ret:
        print(item)
