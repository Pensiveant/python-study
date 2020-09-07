'''
颜色通道转换
'''

from PIL import Image

im=Image.open(r'./Pillow/img/panda.jpg')
print(im.mode) # 'RGB'
out=im.convert('L')
out.save(r'./Pillow/img/panda-L.png')