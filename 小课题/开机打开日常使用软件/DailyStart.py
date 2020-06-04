# coding=utf-8

'''
用于开机时打开日常需要用到的软件
author:pensiveant
email:1429055703@qq.com
version:0.0.0.1
'''
import os
import subprocess
import configparser

program=[
    r'D:\program\TIM\Bin\QQScLauncher.exe',  # qq
    r'D:\program\dingding\DingtalkLauncher.exe', # 钉钉
    r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe", # 微信
    r"C:\Program Files (x86)\Microsoft\BingDesktop\BingDesktop.exe", # 必应
    r"D:\program\vscode\Microsoft VS Code\Code.exe", # vscode
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" # chrome
]

for value in program:
    if os.path.isfile(value):
        subprocess.Popen(value)

