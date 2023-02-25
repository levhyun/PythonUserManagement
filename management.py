import pymysql as ps

connect = ps.connect(host='localhost', user='root', password='2345s', db='user_management', charset='utf8', autocommit=True, cursorclass=ps.cursors.DictCursor)

def signup(email, id, password, phone, gender):
    if DuplicateCheck('email', email) == True:
        return 'EMAIL_ERROR'
    elif DuplicateCheck('id', id) == True:
        return 'ID_ERROR'
    elif DuplicateCheck('phone', phone) == True:
        return 'PHONE_ERROR'
    else:
        db = connect.cursor()
        sql = f'INSERT INTO USER(email, id, password, phone, gender) VALUES("{email}","{id}","{password}","{phone}","{gender}");'
        db.execute(sql)
        return 'SUCCESS'    
    
def login(id, password):
    db = connect.cursor()
    sql = f'SELECT id, password FROM USER;' 
    db.execute(sql)
    result = db.fetchall()
    db.close()
    for data in result:
        if data['id'] == id and data['password'] == password:
            return 'SUCCESS' 
    return 'FAILURE'

def DuplicateCheck(filed,email):
    db = connect.cursor()
    sql = f'SELECT {filed} FROM USER;' 
    db.execute(sql)
    result = db.fetchall()
    db.close()
    for data in result:
        if data[filed] == email:
            return True
    return False