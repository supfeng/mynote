import mysql.connector
from hashlib import md5
from opNum import ReadNum


class UseDatabase:
    """数据库上下文管理器"""
    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self) -> 'cursor':    # 加 self 的目的是在关闭时依然存在
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


class DBop:
    """对数据库进行操作"""
    def __init__(self):
        self.dbconfig = {'host': '127.0.0.1',   # 定义连接属性
                         'user': 'mynote',
                         'password': '123456',
                         'database': 'mynote'}

    def getNormalThing(self) -> 'double List':
        """从数据库 todo 表中返回 normal 用户事件"""
        """返回值：两个 List 列表"""
        """第一个 List 列表为结果，第二个 List 为数据库中信息的主键"""
        with UseDatabase(self.dbconfig) as cursor:
            _SQL = """select todo_id, todo_time, todo_thing
                      from todo
                      where username='normal'"""
            cursor.execute(_SQL)
            tem = cursor.fetchall()  # 返回结果
        res = []
        resIndex = []
        for i in tem:   # 将结果转换为列表形式
            s = ''
            num = 0
            for j in i:
                if num == 0:
                    resIndex.append(j)
                    num += 1
                else:
                    s = s + '     ' + j
            res.append(s)
        return res, resIndex

    def delTodoThing(self, index) -> None:
        """删除数据库 todo 表中的一条数据"""
        with UseDatabase(self.dbconfig) as cursor:
            _SQL = """delete from todo
                      where todo_id=%s"""
            cursor.execute(_SQL, (index, ))

    def getNormalDone(self) -> 'double List':
        """从数据库 done 表中返回 normal 用户事件"""
        """返回值：两个 List 列表"""
        """第一个 List 列表为结果，第二个 List 为数据库中信息的主键"""
        with UseDatabase(self.dbconfig) as cursor:
            _SQL = """select done_id, done_thing
                      from done
                      where username='normal'"""
            cursor.execute(_SQL)
            tem = cursor.fetchall()  # 返回结果
        res = []
        resIndex = []
        for i in tem:  # 将结果转换为列表形式
            s = ''
            num = 0
            for j in i:
                if num == 0:
                    resIndex.append(j)
                    num += 1
                else:
                    s = s + '     ' + j
            res.append(s)
        return res, resIndex

    def delDoneThing(self, index) -> None:
        """删除 done 表中的一条数据"""
        with UseDatabase(self.dbconfig) as cursor:
            _SQL = """delete from done
                      where done_id=%s"""
            cursor.execute(_SQL, (index, ))

    def insertNormalThing(self, time='', thing=''):
        """插入 normal 用户事件到 todo 表中"""
        """默认事件 thing 和时间 time 为 null"""
        r = ReadNum()   # 获取事件编号
        num = r.readAndResetNum()

        with UseDatabase(self.dbconfig) as cursor:
            _SQL = """insert into todo(todo_id, todo_time, todo_thing) 
                      values(%s, %s, %s)"""
            cursor.execute(_SQL, (num, time, thing,))

    def doToDone(self, index):
        """将 todo 表中的一条数据转移到 done 表中"""
        """参数index：事件索引"""
        with UseDatabase(self.dbconfig) as cursor:
            _SQL = """select * 
                      from todo 
                      where todo_id=%s"""
            cursor.execute(_SQL, (index, ))
            tem = cursor.fetchall()  # 返回结果
        for l in tem:  # 将 todo 表中的数据存到 done 表
            todo_id = l[0]
            todo_thing = l[2]
            username = l[3]
            self.delTodoThing(index)  # 删除 todo 表中的数据
        with UseDatabase(self.dbconfig) as cursor:
            _SQL = """insert into done(done_id, done_thing, username) 
                      values(%s, %s, %s);"""
            cursor.execute(_SQL, (todo_id, todo_thing, username))

    def checkUser(self, username='', password='') -> bool:
        """在 user 表中检查登录账户是否登录成功"""
        """返回值为 bool 值，登录成功，返回 1，登录失败，返回 0"""
        md5_password = md5(password.encode('ascii')).hexdigest()    # 密码经过 md5 加密
        with UseDatabase(self.dbconfig) as cursor:
            _SQL = """select username
                      from user
                      where username=%s and password=%s"""
            cursor.execute(_SQL, (username, md5_password, ))
            tmp = cursor.fetchall()  # 返回结果
        setBool = 0
        if tmp:     # 为空表 打印 0
            setBool = 1
        return setBool

    def getSecretThing(self, secretUsername) -> 'double List':
        """从数据库中返回 secretUsername 用户事件"""
        """返回值：两个 List 列表"""
        """第一个 List 列表为结果，第二个 List 为数据库中信息的主键"""
        with UseDatabase(self.dbconfig) as cursor:
            _SQL = """select todo_id, todo_time, todo_thing
                      from todo
                      where username=%s"""
            cursor.execute(_SQL, (secretUsername, ))
            tem = cursor.fetchall()  # 返回结果
        res = []
        resIndex = []
        for i in tem:   # 将结果转换为列表形式
            s = ''
            num = 0
            for j in i:
                if num == 0:
                    resIndex.append(j)
                    num += 1
                else:
                    s = s + '     ' + j
            res.append(s)
        return res, resIndex

    def getSecretDone(self, secretUsername) -> 'double List':
        """从数据库中返回 secretUsernameDone 用户事件"""
        """返回值：两个 List 列表"""
        """第一个 List 列表为结果，第二个 List 为数据库中信息的主键"""
        with UseDatabase(self.dbconfig) as cursor:
            _SQL = """select done_id, done_thing
                      from done
                      where username=%s"""
            cursor.execute(_SQL, (secretUsername, ))
            tem = cursor.fetchall()  # 返回结果
        res = []
        resIndex = []
        for i in tem:  # 将结果转换为列表形式
            s = ''
            num = 0
            for j in i:
                if num == 0:
                    resIndex.append(j)
                    num += 1
                else:
                    s = s + '     ' + j
            res.append(s)
        return res, resIndex

    def insertSecretThing(self, secretUsername, time='', thing=''):
        """插入 secret 用户事件到 todo 表中"""
        """默认事件 thing 和时间 time 为 null"""
        """secretUsername 为用户名"""
        r = ReadNum()   # 获取事件编号
        num = r.readAndResetNum()
        with UseDatabase(self.dbconfig) as cursor:
            _SQL = """insert into todo(todo_id, todo_time, todo_thing, username) 
                      values(%s, %s, %s, %s)"""
            cursor.execute(_SQL, (num, time, thing, secretUsername, ))

    def insertUser(self, username, password):
        """创建用户账号到 user 表中"""
        """username: 用户名；password：密码"""
        md5_password = md5(password.encode('ascii')).hexdigest()  # 密码经过 md5 加密
        with UseDatabase(self.dbconfig) as cursor:
            _SQL = """insert into user(username, password)
                      values(%s, %s)"""
            cursor.execute(_SQL, (username, md5_password, ))

    def checkUsername(self, username='') -> bool:
        """在 user 表中检查用户名 username 是否存在"""
        """返回值为 bool 值，存在，返回 1，不存在，返回 0"""
        with UseDatabase(self.dbconfig) as cursor:
            _SQL = """select username
                      from user
                      where username=%s"""
            cursor.execute(_SQL, (username, ))
            tmp = cursor.fetchall()  # 返回结果
        setBool = 0
        if tmp:  # 为空表 打印 0
            setBool = 1
        return setBool






















