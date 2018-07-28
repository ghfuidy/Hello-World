from PIL import Image
from pathlib import Path

# logoimg = Image.open(r'D:\Download\qq_girl.png')
# logoimg_re = logoimg.resize((20,25))

PATH = 'D:/Download/'
PATH_meili = 'D:/用户目录/我的图片/美莉/'
LOGOFILENAME = 'qq_girl.png'
###设定logo尺寸，并存储在logo文件夹中
def resizeLogo(p):
    originLogoIm = Image.open(str(p))
    w, h = originLogoIm.size
    ratio = w/h
    nWidth, nHeight = int(300*ratio), 300
    nFilename = str(imagePath.joinpath('withlogo').joinpath('LOGO.png'))

    originLogoIm.resize((nWidth, nHeight)).save(nFilename)
    return nWidth, nHeight, nFilename  

imagePath = Path(PATH_meili)
LogoPATH = Path(PATH)

imageWithlogo = imagePath.joinpath('withlogo')
imageWithlogo.mkdir(777,exist_ok=True,)

logo_w, logo_h, logo = resizeLogo(LogoPATH.joinpath(LOGOFILENAME))

logoIm = Image.open(logo).convert('RGBA')
###添加LOGO循环
for fname in [x for x in imagePath.iterdir()]:
    filename = fname.name
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGOFILENAME:
        continue ###skip non-image files
    
    imageLocation = PATH_meili + filename
    im = Image.open(imageLocation)
    width, height = im.size

    print('Adding log to {}...'.format(filename))
    im.paste(logoIm, (width-logo_w, height-logo_h), logoIm)

    im.save(str(imagePath.joinpath('withlogo').joinpath(filename)))

Path(logo).unlink()
    