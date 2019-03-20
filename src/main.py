import psize
import download

def main():
    size = psize.Size()
    dl = download.Download()

    page = int(input("请输入下载开始页码: "))
    max_page = int(input("请输入下载结束页码: "))
    pic_type = int(input("选择图片的类型: \n 0=全部 1=横图 2=竖图 3=正方形\n"))
    change_size = str(input("是否限制图片大小: \n 0=不限制 1=限制\n"))
    if change_size == '0':
        pic_size = size.psize()
    elif change_size == '1':
        print("请勿输入浮点数！")
        width = int(input("最小长: "))
        height = int(input("最小宽: "))
        proportion = int(input("长宽比: "))

        max_width = int(input("最大长: "))
        max_height = int(input("最大宽: "))
        max_proportion = int(input("长宽比: "))

        pic_size = size.psize(width, height, proportion, max_width, max_height, max_proportion)
    else:
        print("输入有误，结束~~")
        return

    path = str(input("修改图片存储根目录?(默认为'C:/Yandere/'): \n"))
    if path == '':
        root = 'C:/Yandere/'
    else:
        root = path

    dl.do_download(pic_size, page, max_page, pic_type, root)

if __name__ == '__main__':
    main()


