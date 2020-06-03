#coding=utf-8
'''
批量切片工具
@author:pensiveant
@email:1429055703@qq.com
@description:输入切片路径，
@version 0.0.0.0
'''

import argparse
from PIL import Image
import os
import sys
import math
import ast
from distutils.spawn import find_executable
import subprocess


# Find external programs
try:
    nona = find_executable('nona')
except KeyError:
    # Handle case of PATH not being set
    nona = None

parser=argparse.ArgumentParser()
parser.add_argument('-i','--inputpath',dest='path',help='需要切片影像根目录')
parser.add_argument('-o','--outpath',dest='outpath',help='输出路径')


parser.add_argument('-C', '--cylindrical', action='store_true',
                    help='input projection is cylindrical (default is equirectangular)')
parser.add_argument('-H', '--haov', dest='haov', default=-1, type=float,
                    help='horizontal angle of view (defaults to 360.0 for full panorama)')
parser.add_argument('-F', '--hfov', dest='hfov', default=100.0, type=float,
                    help='starting horizontal field of view (defaults to 100.0)')
parser.add_argument('-V', '--vaov', dest='vaov', default=-1, type=float,
                    help='vertical angle of view (defaults to 180.0 for full panorama)') 
parser.add_argument('-O', '--voffset', dest='vOffset', default=0.0, type=float,
                    help='starting pitch position (defaults to 0.0)')
parser.add_argument('-e', '--horizon', dest='horizon', default=0.0, type=int,
                    help='offset of the horizon in pixels (negative if above middle, defaults to 0)')
parser.add_argument('-s', '--tilesize', dest='tileSize', default=512, type=int,
                    help='tile size in pixels')
parser.add_argument('-f', '--fallbacksize', dest='fallbackSize', default=1024, type=int,
                    help='fallback tile size in pixels (defaults to 1024)')
parser.add_argument('-c', '--cubesize', dest='cubeSize', default=0, type=int,
                    help='cube size in pixels, or 0 to retain all details')
parser.add_argument('-b', '--backgroundcolor', dest='backgroundColor', default="[0.0, 0.0, 0.0]", type=str,
                    help='RGB triple of values [0, 1] defining background color shown past the edges of a partial panorama (defaults to "[0.0, 0.0, 0.0]")')
parser.add_argument('-B', '--avoidbackground', action='store_true',
                    help='viewer should limit view to avoid showing background, so using --backgroundcolor is not needed')
parser.add_argument('-a', '--autoload', action='store_true',
                    help='automatically load panorama in viewer')
parser.add_argument('-q', '--quality', dest='quality', default=75, type=int,
                    help='output JPEG quality 0-100')
parser.add_argument('--png', action='store_true',
                    help='output PNG tiles instead of JPEG tiles')
parser.add_argument('-n', '--nona', default=nona, required=nona is None,
                    metavar='EXECUTABLE',
                    help='location of the nona executable to use')
parser.add_argument('-G', '--gpu', action='store_true',
                    help='perform image remapping by nona on the GPU')
parser.add_argument('-d', '--debug', action='store_true',
                    help='debug mode (print status info and keep intermediate files)')
args = parser.parse_args()


# 获取输入路径下，图片的路径
imagePathList = []
imageFormat = ["png","jpg","jpeg"]
for root, dirs, files in os.walk(args.path):
    for file in files:
        fileFomat = file.split('.')
        try:
            imageFormat.index(fileFomat[1].lower())
            path=os.path.join(root,file)
            imagePathList.append(path.replace('\\','/'))
        except:
            continue

# 构造输出的路径
def generateOutDir(imagePath):
    if args.outpath:
        outputPath = path.replace(args.path, args.outpath)
    else:
        outputPath = path.replace(args.path, args.path+'/output')
    return outputPath.split('.')[0]

   

# 生成切片方法
def generateTile(inputFile,outDir):
    # Create output directory
    if os.path.exists(outDir):
        print('Output directory "' + outDir + '" already exists')
        if not args.debug:
            sys.exit(1)
    else:
        os.makedirs(outDir)

    # Process input image information
    print('Processing input image information...')
    origWidth, origHeight = Image.open(inputFile).size
    haov = args.haov
    if haov == -1:
        if args.cylindrical or float(origWidth) / origHeight == 2:
            print('Assuming --haov 360.0')
            haov = 360.0
        else:
            print('Unless given the --haov option, equirectangular input image must be a full (not partial) panorama!')
            sys.exit(1)
    vaov = args.vaov
    if vaov == -1:
        if args.cylindrical or float(origWidth) / origHeight == 2:
            print('Assuming --vaov 180.0')
            vaov = 180.0
        else:
            print('Unless given the --vaov option, equirectangular input image must be a full (not partial) panorama!')
            sys.exit(1)
    if args.cubeSize != 0:
        cubeSize = args.cubeSize
    else:
        cubeSize = 8 * int((360 / haov) * origWidth / math.pi / 8)
    tileSize = min(args.tileSize, cubeSize)
    levels = int(math.ceil(math.log(float(cubeSize) / tileSize, 2))) + 1
    if round(cubeSize / 2**(levels - 2)) == tileSize:
        levels -= 1  # Handle edge case
    origHeight = str(origHeight)
    origWidth = str(origWidth)
    origFilename = os.path.join(os.getcwd(), inputFile)
    extension = '.jpg'
    if args.png:
        extension = '.png'
    partialPano = True if args.haov != -1 and args.vaov != -1 else False
    colorList = ast.literal_eval(args.backgroundColor)
    colorTuple = (int(colorList[0]*255), int(colorList[1]*255), int(colorList[2]*255))

    if args.debug:
        print('maxLevel: '+ str(levels))
        print('tileResolution: '+ str(tileSize))
        print('cubeResolution: '+ str(cubeSize))

    # Generate PTO file for nona to generate cube faces
    # Face order: front, back, up, down, left, right
    faceLetters = ['f', 'b', 'u', 'd', 'l', 'r']
    projection = "f1" if args.cylindrical else "f4"
    pitch = 0
    text = []
    facestr = 'i a0 b0 c0 d0 e'+ str(args.horizon) +' '+ projection + ' h' + origHeight +' w'+ origWidth +' n"'+ origFilename +'" r0 v' + str(haov)
    text.append('p E0 R0 f0 h' + str(cubeSize) + ' w' + str(cubeSize) + ' n"TIFF_m" u0 v90')
    text.append('m g1 i0 m2 p0.00784314')
    text.append(facestr +' p' + str(pitch+ 0) +' y0'  )
    text.append(facestr +' p' + str(pitch+ 0) +' y180')
    text.append(facestr +' p' + str(pitch-90) +' y0'  )
    text.append(facestr +' p' + str(pitch+90) +' y0'  )
    text.append(facestr +' p' + str(pitch+ 0) +' y90' )
    text.append(facestr +' p' + str(pitch+ 0) +' y-90')
    text.append('v')
    text.append('*')
    text = '\n'.join(text)
    with open(os.path.join(outDir, 'cubic.pto'), 'w') as f:
        f.write(text)

    # Create cube faces
    print('Generating cube faces...')
    subprocess.check_call([args.nona, ('-g' if args.gpu else '-d') , '-o', os.path.join(outDir, 'face'), os.path.join(outDir, 'cubic.pto')])
    faces = ['face0000.tif', 'face0001.tif', 'face0002.tif', 'face0003.tif', 'face0004.tif', 'face0005.tif']

    # Generate tiles
    print('Generating tiles...')
    for f in range(0, 6):
        size = cubeSize
        faceExists = os.path.exists(os.path.join(outDir, faces[f]))
        if faceExists:
            face = Image.open(os.path.join(outDir, faces[f]))
            for level in range(levels, 0, -1):
                if not os.path.exists(os.path.join(outDir, str(level))):
                    os.makedirs(os.path.join(outDir, str(level)))
                tiles = int(math.ceil(float(size) / tileSize))
                if (level < levels):
                    face = face.resize([size, size], Image.ANTIALIAS)
                for i in range(0, tiles):
                    for j in range(0, tiles):
                        left = j * tileSize
                        upper = i * tileSize
                        right = min(j * args.tileSize + args.tileSize, size) # min(...) not really needed
                        lower = min(i * args.tileSize + args.tileSize, size) # min(...) not really needed
                        tile = face.crop([left, upper, right, lower])
                        if args.debug:
                            print('level: '+ str(level) + ' tiles: '+ str(tiles) + ' tileSize: ' + str(tileSize) + ' size: '+ str(size))
                            print('left: '+ str(left) + ' upper: '+ str(upper) + ' right: '+ str(right) + ' lower: '+ str(lower))
                        colors = tile.getcolors(1)
                        if not partialPano or colors == None or colors[0][1] != colorTuple:
                            # More than just one color (the background), i.e., non-empty tile
                            if tile.mode in ('RGBA', 'LA'):
                                background = Image.new(tile.mode[:-1], tile.size, colorTuple)
                                background.paste(tile, tile.split()[-1])
                                tile = background
                            tile.save(os.path.join(outDir, str(level), faceLetters[f] + str(i) + '_' + str(j) + extension), quality=args.quality)
                size = int(size / 2)

    # Generate fallback tiles
    print('Generating fallback tiles...')
    for f in range(0, 6):
        if not os.path.exists(os.path.join(outDir, 'fallback')):
            os.makedirs(os.path.join(outDir, 'fallback'))
        if os.path.exists(os.path.join(outDir, faces[f])):
            face = Image.open(os.path.join(outDir, faces[f]))
            if face.mode in ('RGBA', 'LA'):
                background = Image.new(face.mode[:-1], face.size, colorTuple)
                background.paste(face, face.split()[-1])
                face = background
            face = face.resize([args.fallbackSize, args.fallbackSize], Image.ANTIALIAS)
            face.save(os.path.join(outDir, 'fallback', faceLetters[f] + extension), quality = args.quality)

    # Clean up temporary files
    if not args.debug:
        os.remove(os.path.join(outDir, 'cubic.pto'))
        for face in faces:
            if os.path.exists(os.path.join(outDir, face)):
                os.remove(os.path.join(outDir, face))

    # Generate config file
    text = []
    text.append('{')
    text.append('    "hfov": ' + str(args.hfov)+ ',')
    if haov < 360:
        text.append('    "haov": ' + str(haov)+ ',')
        text.append('    "minYaw": ' + str(-haov/2+0)+ ',')
        text.append('       "yaw": ' + str(-haov/2+args.hfov/2)+ ',')
        text.append('    "maxYaw": ' + str(+haov/2+0)+ ',')
    if vaov < 180:
        text.append('    "vaov": '    + str(vaov)+ ',')
        text.append('    "vOffset": ' + str(args.vOffset)+ ',')
        text.append('    "minPitch": ' + str(-vaov/2+args.vOffset)+ ',')
        text.append('       "pitch": ' + str(        args.vOffset)+ ',')
        text.append('    "maxPitch": ' + str(+vaov/2+args.vOffset)+ ',')
    if colorTuple != (0, 0, 0):
        text.append('    "backgroundColor": "' + args.backgroundColor+ '",')
    if args.avoidbackground and (haov < 360 or vaov < 180):
        text.append('    "avoidShowingBackground": true,')
    if args.autoload:
        text.append('    "autoLoad": true,')
    text.append('    "type": "multires",')
    text.append('    "multiRes": {')
    text.append('        "path": "/%l/%s%y_%x",')
    text.append('        "fallbackPath": "/fallback/%s",')
    text.append('        "extension": "' + extension[1:] + '",')
    text.append('        "tileResolution": ' + str(tileSize) + ',')
    text.append('        "maxLevel": ' + str(levels) + ',')
    text.append('        "cubeResolution": ' + str(cubeSize))
    text.append('    }')
    text.append('}')
    text = '\n'.join(text)
    with open(os.path.join(outDir, 'config.json'), 'w') as f:
        f.write(text)

# 循环调用方法生成切片
for index, path in enumerate(imagePathList):
    print('第{0}张图片开始切片：'.format(index+1))
    outDir=generateOutDir(path)
    generateTile(path,outDir)

print('切片完成.')