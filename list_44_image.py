# 试试模块函数
# from PIL import ImageColor

# print('Red: {}'.format(ImageColor.getcolor('red', 'RGBA')))

from PIL import Image
girlIm = Image.open('girl.jpg')
# print('size: {}'.format(girlIm))
# width, height = girlIm.size
# print('width is {}, height is {}'.format(width, height))

im = Image.new('RGBA', (100, 200), 'red')
im.save('red.png')
# 裁剪功能
croppedIm = girlIm.crop((0, 100, 600, 800))
croppedIm.save('girl_crop.png')

# girlCopyIm = girlIm.copy()
girlCopyIm = Image.open('girl_crop.png')

reindeerIm = Image.open(r'D:\Download\qq_girl.png').convert('RGBA')
# 将格式转换为“RGBA”后，可以规避bad transparency mask这个错误，成功将透明背景图的背景换成其他图片
girlCopyIm.paste(reindeerIm, (30, 30), reindeerIm)

girlCopyIm.save('merge.png')

# 重复图像马赛克
beautygirl = Image.open(r'D:\用户目录\我的图片\美莉\156649_201611091239530717147982.jpg')
beautygirl_w, beautygirl_h = beautygirl.size

beautygirl_crop = beautygirl.crop((238,92,610,384))
###crop中的四个参数需要用元组形式(x,x,x,x)表示
beautygirl_crop_w, beautygirl_crop_h = beautygirl_crop.size
for left in range(0, beautygirl_w, beautygirl_crop_w):
    for top in range(0, beautygirl_h, beautygirl_crop_h):
        beautygirl.paste(beautygirl_crop, (left,top))

beautygirl.save('masaike.png')

###resize函数重新设定图片尺寸（宽高参数是个元组），rotate(需要旋转的角度)，expand参数可以使图片旋转时避免被截。transpose做镜像。

