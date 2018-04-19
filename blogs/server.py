# -*- coding: utf-8 -*-
import MySQLdb

#
# # 添加用户
# try:
#     conn = MySQLdb.connect(host='localhost', port=3306, db='nuoxiao', user='root', passwd='123456', charset='utf8')
#     cs1 = conn.cursor()
#     count = cs1.execute("insert into blogs_users(name,dateTime) values('weflac','2018-04-11')")
#     print(count)
#     conn.commit()
#     cs1.close()
#     conn.close()
# except Exception as e:
#     print(e)

# # 添加园子
try:
    conn = MySQLdb.connect(host='localhost', port=3306, db='nuoxiao', user='root', passwd='123456', charset='utf8')
    cs1 = conn.cursor()
    count = cs1.execute("insert into blogs_garden(name,introduce,cover_url,description,dateTime,author_id) values('博客庄园','撒上一粒种子 选地搭架子','http://www.nuoxiao.com/blog/dist/images/demo/stock-photos/1.jpg','test','2018-04-11',1)")
    count2 = cs1.execute("insert into blogs_garden(name,introduce,cover_url,description,dateTime,author_id) values('平凡世界','平凡的人社 不一样的世界','http://www.nuoxiao.com/blog/dist/images/demo/stock-photos/2.jpg','test','2018-04-11',1)")
    count3 = cs1.execute( "insert into blogs_garden(name,introduce,cover_url,description,dateTime,author_id) values('神经院子','不同的角度 同样的神经','http://www.nuoxiao.com/blog/dist/images/demo/stock-photos/3.jpg','test','2018-04-11',1)")

    print(count,count2,count3)
    conn.commit()
    cs1.close()
    conn.close()
except Exception as e:
    print(e)