class Log:
    '''
        初始化保护变量
    '''

    def __init__(self):
        self._log_msg = ""

    '''
        添加日志
    '''

    def add(self, msg):
        self._log_msg += msg + '\r'
        print(msg)

    '''
        获取日志
    '''

    def get(self):
        return self._log_msg
