import re
import phttp
import log


class Yande:
    '''
        获取网页html文件 默认从第一页开始
    '''

    def get_html(self, page=1):
        # 拼接请求url 初始化headers
        url = 'https://yande.re/post?page=' + str(page)
        header = {}

        # 实例
        resp = phttp.Http()
        lg = log.Log()

        # 获取html
        html = resp.get(url, header).text
        if not html:
            lg.add("获取" + url + "html失败")
            exit()

        return html

    '''
        根据html 正则筛选出图片列表
    '''

    def get_li(self, html):
        return re.compile('<li style="width: 160px;" id="p.+?</li>').findall(html)

    '''
        根据li 正则筛选出图片信息，包括id url 长和宽
    '''

    def get_info(self, li):
        return re.compile('id="p(\d+)" class=".+?img" href="(.+?)">.+?directlink-res">(\d+) x (\d+)</span>').findall(li)
