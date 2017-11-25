import pymysql
from dingdian import settings

MYSQL_HOSTS=settings.MYSQL_HOSTS
MYSQL_USER=settings.MYSQL_USER
MYSQL_PASSWORD=settings.MYSQL_PASSWORD
MYSQL_PORT=settings.MYSQL_PORT
MYSQL_DB=settings.MYSQL_DB

cnx=pymysql.connect(host=MYSQL_HOSTS,user=MYSQL_USER,password=MYSQL_PASSWORD,port=MYSQL_PORT,db=MYSQL_DB,charset='utf8')

cur=cnx.cursor()

class Sql:
    @classmethod #这个是一个修饰符；作用是我们不需要初始化类就可以直接调用类中的函数使用
    def insert_dd_name(cls,xs_name,xs_author,category,name_id):
        sql='INSERT INTO dd_name(`xs_name`,`xs_author`,`category`,`name_id`)VALUES(%(xs_name)s,%(xs_author)s,%(category)s,%(name_id)s)'
        value={
            'xs_name':xs_name,
            'xs_author':xs_author,
            'category':category,
            'name_id':name_id
            }
        cur.execute(sql,value)
        cnx.commit()


    #这一段代码会查找name_id这个字段，如果存在则会返回 1 不存在则会返回0
    @classmethod
    def select_name(cls,name_id):        
        sql="SELECT EXISTS(SELECT 1 FROM dd_name WHERE name_id=%(name_id)s)"
        value={
            'name_id':name_id
            }
        cur.execute(sql,value)
        return cur.fetchall()[0]  #返回mysql的查询结果
