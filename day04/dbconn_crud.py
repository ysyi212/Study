from dbconn import Session,Departments,Employees

session = Session()

# bk = Departments(dep_id=7,dep_name='backup')
# of = Departments(dep_id=8,dep_name='offices')
# session.add_all([bk,of])

# lb = Employees(
#     emp_id=1,emp_name='liubei',
#     birth_date='1970-1-1',email='lb@tedu.cn',dep_id=1
# )
# gy = Employees(
#     emp_id=2,emp_name='guanyu',
#     birth_date='1973-5-4',email='gy@qq.com',dep_id=2
# )
# zf = Employees(
#     emp_id=3,emp_name='zhangfei',
#     birth_date='1974-10-1',email='zf@tedu.cn',dep_id=2
# )
# zy = Employees(
#     emp_id=4,emp_name='zhaoyun',
#     birth_date='1980-12-12',email='zy@tedu.cn',dep_id=3
# )
# session.add_all([lb,gy,zf,zy])

#查询的参数是类，返回的是实例列表
qset1 = session.query(Departments)
print(qset1) #只有取值的时候才会真正查询
print(qset1.all()) #all返回列表
for dep in qset1:
    print(dep.dep_id,dep.dep_name)

#查询的参数是类变量，返回的是由变量构成的元素列表
qset2 = session.query(Employees.emp_name,Employees.email)
print(qset2.all())

#排序
qset3 = session.query(Departments).order_by(Departments.dep_id)
for dep in qset3:
    print(dep.dep_id,dep.dep_name)

#取切片
qset4 = session.query(Departments).order_by(Departments.dep_id)[2:4]
for dep in qset4:
    print(dep.dep_id,dep.dep_name)

#过滤
qset5 = session.query(Departments).filter(Departments.dep_id>3).\
    filter(Departments.dep_id<6)
for dep in qset5:
    print(dep.dep_id,dep.dep_name)

#模糊查询
qset7 = session.query(Employees).filter(Employees.email.like('%tedu.cn'))
for emp in qset7:
    print(emp.emp_name,emp.email)

qset8 = session.query(Employees).filter(Employees.dep_id.in_([1,2]))
for emp in qset8:
    print(emp.emp_name,emp.emp_id)

#取反用～
qset9 = session.query(Employees).filter(~Employees.dep_id.in_([1,2]))
for emp in qset9:
    print(emp.emp_name,emp.emp_id)

#多表查询,有主外健关系，可自动匹配
qset10 = session.query(Employees.emp_name,Departments.dep_name)\
    .join(Departments)
for data in qset10:
    print(data)

qset11 = session.query(Departments)
print(qset11.all())
print('*' * 30)
print(qset11.first())

#修改
qset12 = session.query(Departments).filter(Departments.dep_name=='hr')
hr = qset12.first()
hr.dep_name = 'hrr'

#删除
qset13 = session.query(Departments).filter(Departments.dep_id==6)
sales = qset13.first()
session.delete(sales)




session.commit()

session.close()