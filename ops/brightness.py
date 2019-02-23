import re
from skimage import  exposure

# 调整亮度

CODE = 'bright'
REGEX = re.compile(r"^" + CODE + "_(?P<alpha>[.0-9]+)")

class Bright:
    def __init__(self, alpha):
        self.code = CODE + str(alpha)
        self.alpha = alpha

    def process(self, img):
        return exposure.adjust_gamma(img, self.alpha)

    @staticmethod
    def match_code(code):
        match = REGEX.match(code)
        if match:
            d = match.groupdict()
            return Bright(float(d['alpha']))
