import requests

class Http:
    '''
        通过requests 中的get方法获取 网页返回
    '''

    def get(self, url: str, header: list = {}):
        # 默认模拟浏览器头部
        header['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        header['Accept-Language'] = 'zh-CN,zh;q=0.8,en;q=0.6'
        header[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2883.103 Safari/537.36'

        # 调用方法
        resp = requests.get(url, headers=header)

        # 返回response
        # 正则判断resp.text 下载resp.content
        return resp
