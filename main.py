import pymysql as ps
import pandas as pd

connect = ps.connect(host='localhost', user='root', password='2345s', db='user_management', charset='utf8', autocommit=True, cursorclass=ps.cursors.DictCursor)

# # test code
# db = connect.cursor()
# sql = 'SHOW TABLES;' 
# db.execute(sql)
# result = db.fetchall()
# db.close()
# result = pd.DataFrame(result)
# print(result)