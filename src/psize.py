
class Size:
    def psize(self,width=0, height=0, proportion=0,
              max_width=0, max_height=0, max_proportion=0):
        pic_size = {
        'min': {'width': width, 'height': height, 'proportion': proportion},
        'max': {'width': max_width, 'height': max_height, 'proportion': max_proportion},
        }
        return pic_size