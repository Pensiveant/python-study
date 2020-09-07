'''
读取和保存图片示例
'''


from PIL import Image
import requests
from io import BytesIO

# # 本地读取图片
# im=Image.open(r'./Pillow/img/girl.jpg')
# im.show()
# print(im.format,im.size,im.mode)
# im.save(r'./Pillow/img/girl.png')

# 从网络读取图片
url='https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2317824872,604106962&fm=26&gp=0.jpg'
response=requests.get(url)
content=response.content
bytesIoObj=BytesIO(content)
im1=Image.open(bytesIoObj)
im1.save(r'./Pillow/img/panda.jpg')
