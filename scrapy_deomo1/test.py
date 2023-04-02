import pymysql
from settings import MYSQL
connect = pymysql.connect(host=MYSQL['host'],
                port=MYSQL['port'],
                user=MYSQL['username'],
                password=MYSQL['password'],
                database=MYSQL['database']
                )
sql = "insert into novel (title, image_path_local, introduce,image_path_network) values ('22', '22', '22','22')"
cursor = connect.cursor()
cursor.execute('select * from novel')
print(cursor.fetchone())



