# coding=utf-8

'''
用于开机时打开日常需要用到的软件
author:pensiveant
email:1429055703@qq.com
'''
import os
import subprocess

program = [
    r'D:\program\TIM\Bin\QQScLauncher.exe',  # QQ
    r'D:\program\dingding\DingtalkLauncher.exe',  # 钉钉
    r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe",  # 微信
    r"C:\Program Files (x86)\Microsoft\BingDesktop\BingDesktop.exe",  # 必应桌面
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  # 谷歌浏览器
]

for value in program:
    if os.path.isfile(value):
        subprocess.Popen(value)

