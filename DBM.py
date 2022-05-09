import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='may')

def addUser(t):
    db=getConnection()
    sql="insert into people values(%s,%s)"
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()
    
def validUser():
    db=getConnection()
    sql="select name,passw from people"
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

def addrecipe(t):
    db=getConnection()
    sql="insert into data values(%s,%s)"
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def allData():
    db=getConnection()
    sql="select * from data"
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

def delData(t):
    db=getConnection ()
    sql="delete from data where title=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def updaterecipe(t):
    db=getConnection()
    sql='update data set recipe=%s where title=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def selectrecipe(title):
    db=getConnection()
    sql='select * from data where title=%s'
    cr=db.cursor()
    cr.execute(sql,title)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist[0]