from PIL import Image

###镜像变换
# girlimg = Image.open(r"C:\Users\Administrator\Desktop\girl_book.jpg")
# girlimg.transpose(Image.FLIP_LEFT_RIGHT).save(r'C:\Users\Administrator\Desktop\girl_book_transpose.jpg')

# girlimg = Image.open(r"C:\Users\Administrator\Desktop\boy.jpg")
# girlimg.transpose(Image.FLIP_LEFT_RIGHT).save(r'C:\Users\Administrator\Desktop\boy_transpose.jpg')

###裁剪图片
# crop_girl =  Image.open(r"C:\Users\Administrator\Desktop\girl_book_transpose.jpg")
# crop_girl.crop((0,0,196,230)).save(r'C:\Users\Administrator\Desktop\girl_bokk_crop.jpg')

window_img = Image.open(r"C:\Users\Administrator\Desktop\windows.jpg")
window_img.transpose(Image.FLIP_LEFT_RIGHT).save(r'C:\Users\Administrator\Desktop\window_transpose.jpg')
paste_girl =  Image.open(r"C:\Users\Administrator\Desktop\girl_bokk_crop.jpg")
window_paste_img = Image.open(r"C:\Users\Administrator\Desktop\window_transpose.jpg")
window_paste_img.paste(paste_girl,(620,235))
window_paste_img.save(r'C:\Users\Administrator\Desktop\merge.jpg')