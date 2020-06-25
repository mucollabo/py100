import os
import sqlite3

# sqlite 데이터베이스 스키마 정의
app_root = os.getcwd()
conn = sqlite3.connect(os.path.join(app_root, 'danawa.sqlite'))

cur = conn.cursor()

sql = '''
CREATE TABLE Product (
id integer primary key autoincrement,
title text not null,
price integer,
link text)
'''

cur.execute(sql)
conn.commit()
conn.close()

file_list = os.listdir(app_root)
print(file_list)