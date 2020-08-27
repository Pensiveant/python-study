import requests
from PIL import Image
from io import BytesIO

requestUrl='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1598525431283&di=23348171d7b70f1c6641c32cdba795ec&imgtype=0&src=http%3A%2F%2Fp0.qhimg.com%2Ft01211b12df92615a75.png'

response=requests.get(requestUrl)
contentType=response.headers['Content-Type']
i = Image.open(BytesIO(response.content))
i.save('test.jpg','jpeg')
