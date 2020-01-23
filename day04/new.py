#!/usr/bin/env python3
from sqlalchemy import create_engine
# 创建连接到数据库的引擎
engine = create_engine(
        #指定数据库、用户名、密码、连接到哪台服务器、库名等信息
    'mysql+pymysql://ysy:123456@192.168.4.5/company?charset=utf8',
    encoding='utf8'
    #echo=True    #终端输出
)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, String, Integer

class Departments(Base):  # 必须继承于Base
    __tablename__ = 'departments'  # 库中的表名
    # 每个属性都是表中的一个字段，是类属性
    dep_id = Column(Integer, primary_key=True)    #Integer整数类型,primary_key主键
    # String字符串类型，nullable非空约束，unique唯一性约束
    dep_name = Column(String(20), nullable=False, unique=True)
    def __str__(self):
        return '[部门ID：%s, 部门名称：%s]' % (self.dep_id, self.dep_name)
if __name__ == '__main__':
    # 在数据库中创建表，如果库中已有同名的表，将不会创建
    Base.metadata.create_all(engine)
