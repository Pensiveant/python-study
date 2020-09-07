from PIL import ImageFilter
from PIL import Image

im=Image.open(r'./Pillow/img/panda.jpg')

# 增强过滤器：模糊
out = im.filter(ImageFilter.BLUR)
out.save(r'./Pillow/img/pandaFilter.jpg')

# 操作每个点
out1 = im.point(lambda i: i * 3)
out1.save(r'./Pillow/img/pandaPointOperations.jpg')

# 