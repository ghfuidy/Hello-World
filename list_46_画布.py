# from PIL import Image

# im = Image.new('RGBA', (100, 100))
# print('transparent background: {}'.format(im.getpixel((0, 0))))

# for x in range(100):
#     for y in range(50):
#         im.putpixel((x,y), (20, 165, 210))

# from PIL import ImageColor

# for x in range(100):
#     for y in range(50,100):
#         im.putpixel((x,y), ImageColor.getcolor('violet', 'RGBA'))

# print('upper part: {}, lower part: {}'.format(im.getpixel((0,0)), im.getpixel((0,50))))

# im.save('RGBA.png')

# from PIL import Image, ImageDraw

# im = Image.new('RGBA', (200, 200), 'white')
# draw = ImageDraw.Draw(im)

# draw.line([(0,0), (199,0), (199,199), (0,199), (0,0)], fill='pink', width=10)
# draw.rectangle((20,30,60,60), fill='blue')
# draw.ellipse((120,30,160,60), fill='red')
# draw.polygon(((57,87),(79,62),(94,85),(120,90),(103,113)), fill='brown',outline='green')

# for i in range(100,200,10):
#     draw.line([(i,0),(200,i-100)], fill='purple')
# im.save('drawimg.png')

from PIL import ImageFont, Image, ImageDraw

im = Image.new('RGBA', (200,200), 'white')
draw = ImageDraw.Draw(im)

draw.text((20,100), 'Hello,this is \na image  of photo', fill='purple')

fontFolder = 'C:\Windows\Fonts'
BRADHITCFont = ImageFont.truetype('BRADHITC.TTF', 32)

draw.text((100,150), 'pitterZhu', fill='gray', font=BRADHITCFont)
im.save('text.png')