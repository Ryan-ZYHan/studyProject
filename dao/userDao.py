"""
用户实例数据访问层
"""
from entity.userEntity import User
from py_tool import dbOperator as dbo
import copy

currentUser: User = None  # 当前用户


def login(user: User):
    """
    用户登录
    :param user:用户实体
    :return: 登录成功返回用户信息实体，登录失败返回None
    """
    global currentUser
    con = None
    try:
        con = dbo.get_connection(database="studyProjectDatabase")
        cursor = con.cursor()
        cursor.execute(
            f"select *from t_user where userName = '{user.userName}' and password = '{user.password}'")
        result = cursor.fetchone()
        print(result)
        currentUser = copy.deepcopy(user) if result is not None else None
        return result
    except Exception as e:
        con.rollback()
        currentUser = None
        print(e)
    finally:
        dbo.close_connection(con)


if __name__ == "__main__":
    # con = None
    # try:
    #     con = dbo.get_connection(database="studyProjectDatabase")
    #     cursor = con.cursor()
    #     cursor.execute("select *from t_user")
    #     print(cursor.fetchall())
    # except Exception as e:
    #     print(e)
    # finally:
    #     dbo.close_connection(con)
    user = User("user1", "password1")
    resultUser = login(user)
    print(currentUser)
