from pymysql import Connection


def get_connection(host: str = 'localhost', port: int = 3306, user: str = 'root', password: str = '', database: str = '', autocommit: bool = True):
    '''
    获取数据库连接
    
    :param host: MySQL服务器地址
    :param port: MySQL服务器端口
    :param user: 数据库用户名
    :param password: 数据库密码
    :param database: 数据库名
    :param autocommit: 是否自动提交事务
    :return: pymysql.connect() 对象
    '''
    return Connection(host=host, port=port, user=user, password=password, database=database, autocommit=autocommit)


def close_connection(connection: Connection):
    """
    关闭数据库连接
    
    :param connection: pymysql.connect() 对象
    """
    if connection:
        connection.close()


if __name__=="__main__":
    con = None
    try:
        con = get_connection(database="studyProjectDatabase")
        cursor = con.cursor()
        cursor.execute("select *from t_user")
        print(cursor.fetchall())
    except Exception as e:
        print(e)
    finally:
        close_connection(con)