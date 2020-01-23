#!/root/ysy/python/bin/python3
'''py_mysql
'''
import pymysql

conn = pymysql.connect(
    host='192.168.4.5',
    port=3306,
    user='ysy',
    passwd='123456',
    db='company',
    charset='utf8'
)

cur = conn.cursor()

# insert1 = 'INSERT INTO departments VALUES (%s,%s)'
# hr = [(1,'hr')]
# deps = [(2,'ops'),(3,'dev'),(4,'qa'),(5,'market'),(6,'sales')]
# cur.executemany(insert1,hr)
# cur.executemany(insert1,deps)

# select1 = 'SELECT * FROM departments'
# cur.execute(select1)
# result1 = cur.fetchone()
# print(result1)
# result2 = cur.fetchmany(2)
# print(result2)
# result3 = cur.fetchall()
# print(result3)
#
# cur.execute(select1)
# cur.scroll(2,mode='absolute')
# result1 = cur.fetchone()
# print(result1)
# cur.scroll(1)
# result2 = cur.fetchone()
# print(result2)

update1 = 'UPDATE departments SET dep_name=%s WHERE dep_name=%s'
cur.execute(update1,('hr','account'))

delete1 = 'DELETE FROM departments WHERE dep_id=%s'
cur.execute(delete1,(6,))


conn.commit()

cur.close()
conn.close()