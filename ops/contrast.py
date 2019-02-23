import re
from skimage import  exposure

# 调整对比度

CODE = 'contrast'
REGEX = re.compile(r"^" + CODE + "_(?P<x_trans>[-0-9]+)_(?P<y_trans>[-0-9]+)")

class Contrast:
    def __init__(self, x_trans, y_trans):
        self.code = CODE + str(x_trans) + '_' + str(y_trans)
        self.x_trans = x_trans
        self.y_trans = y_trans

    def process(self, img):
        return exposure.rescale_intensity(img, out_range=(self.x_trans, self.y_trans))

    @staticmethod
    def match_code(code):
        match = REGEX.match(code)
        if match:
            d = match.groupdict()
            return Contrast(int(d['x_trans']), int(d['y_trans']))