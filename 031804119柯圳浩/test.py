import pymysql


def register(userID, telephone, passwd):
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',
                          db='DongSheng', charset='utf8')
    cursor = con.cursor(pymysql.cursors.DictCursor)
    cursor.execute("insert into stock (id,name,passwd) values( %s, % s, % s)", userID, telephone, passwd)
    con.commit()
    con.close()


def userID():
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',
                          db='DongSheng', charset='utf8')
    cursor = con.cursor(pymysql.cursors.DictCursor)
    # 查询user表格
    # DSid为最后一个id
    count = DSid + 1
    con.commit()
    con.close()
    return count


telephone = eval(input())
passwd = input()
DSid = userID()
register(DSid, telephone, passwd)
