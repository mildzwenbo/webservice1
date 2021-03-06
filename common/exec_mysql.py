import pymysql
from common.log import logger
import threading
import configparser
from common.get_path import GetPath
from common.select_environment import Select

select = Select().select()

each = GetPath()
mysql_conf_path = each.get_conf_path('mysql.ini')
mutex=threading.Lock()
mutex.acquire() # 上锁，防止多线程下出问题
conf = configparser.ConfigParser()
conf.read(mysql_conf_path, encoding='utf-8')



if select == '1':
    host = conf.get('mysql', 'host')
    port = int(conf.get('mysql', 'port'))
    user = conf.get('mysql', 'user')
    passwd = conf.get('mysql', 'passwd')
    db = conf.get('mysql', 'db')

elif select == '0':
    host = conf.get('pvt_mysql', 'host')
    port = int(conf.get('pvt_mysql', 'port'))
    user = conf.get('pvt_mysql', 'user')
    passwd = conf.get('pvt_mysql', 'passwd')
    db = conf.get('pvt_mysql', 'db')
# host = conf.get('mysql', 'host')
# port = int(conf.get('mysql', 'port'))
# user = conf.get('mysql', 'user')
# passwd = conf.get('mysql', 'passwd')
# db = conf.get('mysql', 'db')
mutex.release()


class ExecMysql():
    log = logger

    def select_mysql(self, sql):
        try:
            connect = pymysql.connect(
                host=host,
                port=port,
                user=user,
                passwd=passwd,
                db=db,
            )
            cursor = connect.cursor()
            cursor.execute(sql)
            row = cursor.fetchall()
            return row
        except Exception as msg:
            self.log.info(str(msg))
        finally:
            cursor.close()
            connect.close()

    def insert_mysql(self, sql):
        try:
            connect = pymysql.connect(
                host=host,
                port=port,
                user=user,
                passwd=passwd,
                db=db,
            )
            cursor = connect.cursor()
            cursor.execute(sql)
            connect.commit()
        except Exception as msg:
            self.log.info(str(msg))
        finally:
            cursor.close()
            connect.close()

    def delete_mysql(self, sql):
        try:
            connect = pymysql.connect(
                host=host,
                port=port,
                user=user,
                passwd=passwd,
                db=db,
            )
            cursor = connect.cursor()
            cursor.execute(sql)
            connect.commit()
        except Exception as msg:
            self.log.info(str(msg))
        finally:
            cursor.close()
            connect.close()

    def update_mysql(self, sql):
        try:
            connect = pymysql.connect(
                host=host,
                port=port,
                user=user,
                passwd=passwd,
                db=db,
            )
            cursor = connect.cursor()
            cursor.execute(sql)
            connect.commit()
        except Exception as msg:
            self.log.info(str(msg))
        finally:
            cursor.close()
            connect.close()


def fun_select():
    a = ExecMysql()
    sql = "SELECT * FROM run_status;"
    b = a.select_mysql(sql)
    for i in b:
        print(i)


if __name__ == '__main__':
    mysql = ExecMysql()
    # 查询
    # sql = "SELECT name FROM search_name WHERE product_name ='operation_product_click';"
    # result = mysql.select_mysql(sql)[0][0] #得到的为元组
    # print(result)
    a = 'abc'
    sql = "UPDATE add_product_name SET product_name='%s' WHERE id=2;" % a
    print(sql)
    mysql.update_mysql(sql)
    # for i in result:
    #     print(i[1])
    # print('-' * 100)
    # 插入数据
    # insert_sql = "INSERT INTO run_status(name, status) VALUE ('status1', '1234');"
    # mysql.insert_mysql(insert_sql)
    # fun_select()
    # print('-'*100)
    # # 更新数据
    # update_sql = "UPDATE trade SET user='fei' WHERE id=32;"
    # mysql.update_mysql(update_sql)
    # fun_select()
    # print('-' * 100)
    # #删除数据
    # delete_sql = "DELETE FROM trade WHERE id=32;"
    # mysql.delete_mysql(delete_sql)
    # fun_select()

    # mysql.update_mysql("UPDATE run_status SET status='0' WHERE name='test_g_release_product_clcik';")

    # mysql = ExecMysql()
    # sql = "SELECT name FROM search_name WHERE product_name='operation_product_click';"
    # sql1 = "SELECT product_name FROM add_product_name WHERE name='test_ac_input_something';"
    # search_name = mysql.select_mysql(sql)[0][0]
    # name = mysql.select_mysql(sql1)[0][0]
    # print(name)
