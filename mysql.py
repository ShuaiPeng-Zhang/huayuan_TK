try:
    import pymysql
    pymysql.install_as_MySQLdb()
except :
    import os
    os.system('pip install pymysql')
    import pymysql
    pymysql.install_as_MySQLdb()


def conn_mysql(sql):
        conn = pymysql.connect(host = '192.168.108.29',user = 'root',passwd = 'Asd123456',db = 'liangyuan_db',charset='utf8')
        cur = conn.cursor()
        try:
            cur.execute(sql)
            result = cur.fetchall()
            # print(result)
            conn.commit()
            cur.close()
            conn.close()
            return result
        except:
            print('error:SQL操作失败!')
