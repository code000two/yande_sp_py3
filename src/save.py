import os.path
import datetime


class Save:
    '''
        初始化图片存储根目录
    '''

    def __init__(self, root_name):
        self._root_name = root_name

    '''
        判断是否有存储根目录
    '''

    def create_folder(self):
        self._root_name += datetime.datetime.now().strftime('%Y%m%d')
        if not os.path.exists(self._root_name):
            os.makedirs(self._root_name)
        print(self._root_name)

    '''
        保存图片 写入数据
    '''

    def write(self, file_name: str, data: bytes):
        # 拼接保存文件名字
        file_name = self._root_name + '/' + file_name
        # 判断文件是否存在
        if not os.path.exists(file_name):
            file = open(file_name, 'wb')
            file.write(data)
            file.close()
            print("保存图片成功")
        else:
            print("保存图片失败 可能文件已经存在")

    '''
        保存下载flag 格式为str
    '''

    def clog(self, file_name: str, data: str, root: bool = False):
        if root:
            file = open(file_name, 'wb')
            file.write(data.encode())
            file.close()
            print("更新最新图片id成功")
        else:
            print("下载结束不写入flag")

    '''
        获取flag文件中的图片id    
    '''

    def get(self, file_name: str):
        file = open(file_name)
        data = file.readline()
        file.close()
        return data

    '''
        判断文件是否存在 
    '''

    def exists(self, file_name: str):
        return os.path.exists(self._root_name + '/' + file_name)
