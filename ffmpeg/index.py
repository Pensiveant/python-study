#coding=utf-8
'''
视频压缩工具
@author:pensiveant
@email:1429055703@qq.com
@description:将视频进行压缩，并提供一张缩略图
@version 0.0.0.0
'''

import subprocess
import os
import sys
from subprocess import DEVNULL  # Python 3.

# 检测输入的值是否符合要求
def checkInputValues(inputDir, outputDir, videoHeight, imageResolution):
    if inputDir is None or inputDir == '':
        print('要转换的视频文件夹地址不能为空!')
        sys.exit(0)
    if outputDir is None or inputDir == '':
        print('要输出的文件夹目录地址不能为空!')
        sys.exit(0)
    if videoHeight is None or inputDir == '':
        print('要输出的视频分辨率不能为空!')
        sys.exit(0)
    if imageResolution is None or inputDir == '':
        print('要输出的缩略图的分辨率不能为空!')
        sys.exit(0)

# 生成压缩的命令
# @param inputFile
# @param outputFile


def compressVideo(inputFile, outputFile, height):
    getResolution = "ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 {0}".format(
        inputFile)
    resolution = subprocess.check_output(getResolution, shell=True)
    resolution = str(resolution)[2:-5]
    width = int(
        (float(resolution.split('x')[0])/float(resolution.split('x')[1]))*float(height))
    scale = str(width)+':'+str(height)
    compressCommmand = 'ffmpeg -i {0} -vf scale={1}  {2}'.format(
        inputFile, scale, outputFile)
    return compressCommmand


# 获取缩略图命令
# @param {String} inputFile 输入文件名
# @param {String} imageName 图片名称
def getVideoThumbnail(inputFile, imageName, imageResolution):
    compressCommmand = 'ffmpeg -i {0} -ss 00:00:20 -t 1 -r 1 -q:v 2  -f image2 -vf scale={2} {1}.jpg'.format(
        inputFile, imageName, imageResolution)
    return compressCommmand


inputDir = input('输入要转换的视频文件夹地址:')
outputDir = input('输入要输出的文件夹目录地址:')
videoHeight = input('输入要输出的视频分辨率(示例：1080):')
imageResolution = input('输入要输出的缩略图的分辨率（格式：320:240）:')
checkInputValues(inputDir,outputDir,videoHeight,imageResolution)
print('开始压缩文件.....')
# inputDir = 'D:\\pensiveant\lab\\ffmpeg\\beibei'
# outputDir = 'D:\\pensiveant\lab\\ffmpeg\\beibei\\output'
# videoHeight = '1080'
# imageResolution = '320:240'

# 获取输入的文件路径下的文件path
pathList = []
videoFormat = ["wmv", "asf", "asx", "rm", "rmvn", "mp4",
               "3gp", "mov", "m4v", "avi", "dat", "mkv", "fiv", "vob"]
for root, dirs, files in os.walk(inputDir):
    for file in files:
        fileFomat = file.split('.')
        try:
            videoFormat.index(fileFomat[1].lower())
            pathList.append(os.path.join(root, file))
        except:
            continue


# 构造输出的路径
outputPathList = []
for path in pathList:
    outputPath = path.replace(inputDir, outputDir)
    outputPathList.append(outputPath)

# 创建输出路径的文件夹
for path in outputPathList:
    outPath = path.split('\\')
    outPath.pop()
    outputPath = '\\'.join(outPath)
    if not os.path.exists(outputPath):
        os.mkdir(outputPath)

# 压缩视频
for index, value in enumerate(pathList):
    print('压缩第{0}个文件'.format(index+1))
    print('生成缩略图')
    thumbnailName = outputPathList[index].split('.')[0]
    videoThumbnail = getVideoThumbnail(value, thumbnailName, imageResolution)
    p = subprocess.call(videoThumbnail, stdout=DEVNULL,
                        stderr=DEVNULL, shell=True)
    print('压缩视频')
    compressVideo1 = compressVideo(value, outputPathList[index], videoHeight)
    p = subprocess.call(compressVideo1, stdout=DEVNULL,
                        stderr=DEVNULL, shell=True)
print('压缩完成')
