'''
裁切、粘贴、合并示例
'''

from PIL import Image

im=Image.open(r'./Pillow/img/panda.jpg')
box=(0,0,300,300)
region=im.crop(box)
region = region.transpose(Image.ROTATE_180)
im.paste(region, box)
r,g,b=im.split()
im = Image.merge("RGB", (b, g, r))
im.save(r'./Pillow/img/panda1.jpg')