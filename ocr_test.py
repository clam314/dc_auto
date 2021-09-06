# from PIL import Image
# import pytesseract
#
# image = Image.open(r"tpl1630680767598.png")
# # text = pytesseract.image_to_string(image)
# text_ch = pytesseract.image_to_string(image,lang='chi_sim')
# print("-----------识别数据为--------------")
# # print(text)
# print(text_ch)

import base64
# encoding:utf-8
import requests

# access_token = ""
# # client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=NErowZumSBE5zhnEfEd2Bpyj&client_secret=yEf3O9c5RBxBw33mYgzEodFIO0nKx1Bf'
# response = requests.get(host)
# if response:
#     print(response.json())

'''
通用文字识别（高精度版）
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
f = open(r"tpl1630418313475.png", 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = "24.c26374e1930470d248a112256cc9e94f.2592000.1633274618.282335-24798449"
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())