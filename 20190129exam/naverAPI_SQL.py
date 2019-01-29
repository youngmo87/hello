import pymysql
import time

def get_conn(db):
    return pymysql.connect(
        # host='35.221.66.161',
        host = '127.0.0.1',
        user='dooo',
        password='dooo!',
        port=3306,
        db=db,
        charset='utf8')


isStart = True
def save(sql_truncate, sql_insert, lst):
    try:
        conn = get_conn('melondb')
        conn.autocommit = False
        cur = conn.cursor()
        global isStart
        if isStart:
            cur.execute(sql_truncate)
            isStart = False

        cur.executemany(sql_insert, lst)
        conn.commit()
        print("Affected RowCount is", cur.rowcount, "/", len(lst))

    except Exception as err:
        conn.rollback()
        print("Error!!", err)

    finally:
        try:
            cur.close()
        except:
            print("Error on close cursor")

        try:
            conn.close()
        except Exception as err2:
            print("Fail to connect!!", err2)