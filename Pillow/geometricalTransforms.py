from PIL import Image

im=Image.open(r'./Pillow/img/panda.jpg')
# 尺寸缩小10倍
width, height=im.size
out=im.resize((width//10,height//10 )) # 等价于 out=im.resize((int(width/10),int(height/10) ))
out.save(r'./Pillow/img/panda1.jpg')

# 图片旋转45度
out1=im.rotate(45)
out1.save(r'./Pillow/img/pandarotate45.jpg')