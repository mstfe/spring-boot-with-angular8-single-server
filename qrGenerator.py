# import modules
import qrcode
from PIL import Image
import os
from PIL import ImageFont
from PIL import ImageDraw


def get_concat(im1, im2):
    back_im = im1.copy()
    newsize = (160, 160)
    im1 = im1.resize(newsize, Image.ANTIALIAS)
    area = (167, 180)
    back_im.paste(im2, area)
    return back_im

# taking image which user wants
# in the QR code center


def get_concat_array(area, im1, im2):
    back_im = im1.copy()
    newsize = (160, 160)
    im1 = im1.resize(newsize, Image.ANTIALIAS)
    back_im.paste(im2, area)
    return back_im


def generateImageArray(fileName, qrcodeTextArray, score):
    Logo_link = 'pk_logo.jpeg'
    Base_Image = 'result/'+fileName+'_result.png'
    img = Image.open('template.png')
    img.save(Base_Image)

    x = 0
    y = 0
    i = 0

    a = 157
    a1 = 160 + 85
    b = 167

    iX = [a, a+a1, a+a1*2, a+a1*3, a+a1*4, a+a1*5]
    iY = [b, b+a1, b+a1*2, b+a1*3, b+a1*4, b+a1*5, b+a1*6, b+a1*7]

    area = [(iX[0], iY[0]), (iX[1], iY[0]), (iX[2], iY[0]), (iX[3], iY[0]), (iX[4], iY[0]), (iX[5], iY[0]),
            (iX[0], iY[1]), (iX[1], iY[1]), (iX[2], iY[1]
                                             ), (iX[3], iY[1]), (iX[4], iY[1]), (iX[5], iY[1]),
            (iX[0], iY[2]), (iX[1], iY[2]), (iX[2], iY[2]
                                             ), (iX[3], iY[2]), (iX[4], iY[2]), (iX[5], iY[2]),
            (iX[0], iY[3]), (iX[1], iY[3]), (iX[2], iY[3]
                                             ), (iX[3], iY[3]), (iX[4], iY[3]), (iX[5], iY[3]),
            (iX[0], iY[4]), (iX[1], iY[4]), (iX[2], iY[4]
                                             ), (iX[3], iY[4]), (iX[4], iY[4]), (iX[5], iY[4]),
            (iX[0], iY[5]), (iX[1], iY[5]), (iX[2], iY[5]
                                             ), (iX[3], iY[5]), (iX[4], iY[5]), (iX[5], iY[5]),
            (iX[0], iY[6]), (iX[1], iY[6]), (iX[2], iY[6]
                                             ), (iX[3], iY[6]), (iX[4], iY[6]), (iX[5], iY[6]),
            (iX[0], iY[7]), (iX[1], iY[7]), (iX[2], iY[7]), (iX[3], iY[7]), (iX[4], iY[7]), (iX[5], iY[7]), ]

    for item in qrcodeTextArray:
        # area = (157+250*x, 180 + 260*y)
        # print(area)
        # if i == 5 or i == 11 or i == 17 or i == 23 or i == 29 or i == 35 or i == 41:
        #     y += 1
        #     x = 0
        # else:
        #     x += 1
        textToQrImageWithLogo(item[0], Logo_link, score, item[1]).save(
            'gfg_QR_.png')
        get_concat_array(area[i], Image.open(Base_Image), Image.open(
            'gfg_QR_.png')).save('result/'+fileName+'_result.png')
        i += 1
    # os.remove('result/gfg_QR_.png')


def generateImage(qrcodeText):

    Logo_link = 'pk_logo.jpeg'
    Base_Image = 'ismail_template-1.png'

    # save the QR code generated
    textToQrImageWithLogo(qrcodeText, Logo_link).save(
        'gfg_QR_'+qrcodeText+'.png')

    get_concat(Image.open(Base_Image), Image.open('gfg_QR_' +
                                                  qrcodeText+'.png')).save('result/'+qrcodeText+'.png')

    # print("{} QR code generated!".format(qrcodeText))

# generateImage('pk1-163b2b03-ecb2-4d6d-add8-d5ec962cf8d1')


def textToQrImageWithLogo(qrcodeText, logoLink, score, index):
    logo = Image.open(logoLink)

    # taking base width
    basewidth = 100

    # adjust image size
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    # taking url or text
    # url = 'pk1-163b2b03-ecb2-4d6d-add8-d5ec962cf8d1'

    # addingg URL or text to QRcode
    QRcode.add_data(qrcodeText)

    # generating QR code
    QRcode.make()

    # taking color name from user
    QRcolor = 'black'

    # adding color to QR code
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").convert('RGB')

    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
           (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    result = QRimg.resize((160, 160), Image.ANTIALIAS)
    draw = ImageDraw.Draw(result)
    font = ImageFont.truetype("times-ro.ttf", 20)
    draw.text((12, 152), str(index), (0, 0, 0), font=font)
    draw.text((135, 6), str(score), (0, 0, 0), font=font)

    return result
