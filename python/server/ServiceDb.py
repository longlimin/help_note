#!/usr/bin/env python
#-*- coding:utf-8 -*- 
from include import *

""" 
    数据库service
""" 
#   db = database()
#   count,listRes = db.executeQueryPage("select * from student where id=? and name like ? ", 2, 10, "id01", "%name%")
#   listRes = db.executeQuery("select * from student where id=? and name like ? ", "id01", "%name%")
#   db.execute("delete from student where id=? ", "id01")
#   count = db.getCount("select * from student ")
#   db.close()
#
class ServiceDb:
    def __init__(self):
        self.db = Database()

    def insertFile(self, id, time, path):
        self.db.execute('insert into file values(?, ?, ?) ', id, time, path)

    def insertSocket(self, id, time, msg):
        self.db.execute('insert into socket values(?, ?, ?) ', id, time, msg)







    def init(self):
        db = self.db
        db.execute(
            ''' 
            create table if not exists file(
                id      text primary key,
                time    text not null,
                path    text 
            )
            ''' 
        )

        db.execute(
            ''' 
            create table if not exists socket(
                id      text primary key,
                time    text not null,
                msg     text 
            )
            ''' 
    )





  