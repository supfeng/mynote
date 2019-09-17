import os


class ReadNum:
    """获取事件编号"""
    def __init__(self):
        self.fileName = 'num.txt'

    def readAndResetNum(self) -> int:
        """获取事件编号"""
        # 读文件
        numlist = []
        with open(self.fileName) as file:
            for num in file:
                numlist.append(num)
        tmp = int(numlist[0])
        num = tmp
        tmp += 1
        # 写文件
        with open(self.fileName, 'w') as file:
            file.write(str(tmp))
        return num


class OpUsername:
    """对用户名进行操作"""
    def __init__(self):
        self.fileName = 'user.txt'

    def readUser(self) -> str:
        """获取用户名"""
        # 读文件
        name = ''
        with open(self.fileName) as file:
            for c in file:
                name = name + c
        return name

    def writeUser(self, username):
        """写用户名到文件中"""
        with open(self.fileName, 'w') as file:
            file.write(username)


