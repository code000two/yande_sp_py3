import save
import yande_re
import log
import phttp
import time

class Download:
    def do_download(self,pic_size: {}, page, max_page, pic_type, path):
        # 默认'C:/Yandere/'
        wr = save.Save(path)
        yande = yande_re.Yande()
        lg = log.Log()
        resp = phttp.Http()

        wr.create_folder()

        flag_id = int(wr.get('flag_id.data'))  # 上次开始爬取时第一张图片ID。爬到此ID则终止此次爬取
        i = 0  # 当前第几张
        end = False  # 爬取是否已结束

        while True:

            # 终止页码为0 或 未到达终止页码时 才进行爬取
            if max_page == 0 or page <= max_page:
                # 获取页面内容
                lg.add('正在读取第' + str(page) + '页……')
                html = yande.get_html(page)
                # 获取每个li的内容
                for li in yande.get_li(html):
                    i += 1
                    info = yande.get_info(li)[0]  # (id, img_url, width, height)
                    width = int(info[2])
                    height = int(info[3])

                    # 存储last_start_id
                    if i == 1:
                        if len(info) == 4:
                            wr.clog('flag_id.data', info[0], True)
                        else:
                            # 第一张个li就出现了问题，这就无法存储last_start_id了
                            exit()

                    # 数据结构是否错误？
                    if len(info) != 4:
                        lg.add(str(i) + ' 错误，跳过')
                        continue

                    # 已经爬到上次开始爬的地方了 且 终止页码为0 本次爬取结束
                    if int(info[0]) == flag_id and max_page == 0:
                        end = True
                        break

                    download = False  # 是否下载此图？
                    # 判断图片类型（不想写一长串……只好如此了）
                    if pic_type == 0:
                        download = True
                    elif pic_type == 1 and width > height:
                        download = True
                    elif pic_type == 2 and width < height:
                        download = True
                    elif pic_type == 3 and width == height:
                        download = True
                    else:
                        lg.add('图片类型不符，跳过')
                        continue
                    # 判断图片尺寸
                    if width >= pic_size['min']['width'] and height >= pic_size['min']['height']:
                        if pic_size['max']['width'] and width > pic_size['max']['width']:
                            download = False
                        if pic_size['max']['height'] and height > pic_size['max']['height']:
                            download = False
                    else:
                        download = False
                    # 判断图片宽高比
                    proportion = width / height
                    if proportion < pic_size['min']['proportion'] or (
                            pic_size['max']['proportion'] and proportion > pic_size['max']['proportion']):
                        download = False
                    if not download:
                        lg.add('图片尺寸不符，跳过')
                        continue

                    if download:
                        # 获取文件名
                        # 此处不进行URL解码，因为有些文件名神TM带*之类的
                        file_name = info[1].split('/')[-1]
                        # 文件是否已存在？
                        if wr.exists(file_name):
                            lg.add(info[0] + ' 已存在，跳过')
                            continue

                        lg.add(str(i) + ' - ' + info[0] + ' 开始下载……')
                        ts = time.time()
                        img = resp.get(info[1], {'Host': 'files.yande.re',
                                                 'Referer': 'https://yande.re/post/show/' + info[0]}).content
                        lg.add('下载完毕。耗时：' + str(int(time.time() - ts)) + 's')

                        wr.write(file_name, img)

                if end:
                    break
            else:
                break

            page += 1

        lg.add('爬取结束')
        wr.clog('log_' + str(int(time.time())) + '.txt', lg.get())
        exit(200)