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

create_dep = '''CREATE TABLE departments(
dep_id INT,dep_name VARCHAR(20),
PRIMARY KEY(dep_id)
)'''
create_emp = '''CREATE TABLE employees(
emp_id INT,emp_name VARCHAR(20),birth_date DATE,
email VARCHAR(50),dep_id INT,
PRIMARY KEY(emp_id),
FOREIGN KEY(dep_id) REFERENCES departments(dep_id)
)'''
create_sal = '''CREATE TABLE salary(
id INT,date DATE,emp_id INT,basic INT,awards INT,
PRIMARY KEY(id),
FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
)'''
cur.execute(create_dep)
cur.execute(create_emp)
cur.execute(create_sal)


conn.commit()





cur.close()
conn.close()