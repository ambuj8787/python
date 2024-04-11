# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:21:05 2023

@author: user
"""
import qrcode

qr=qrcode.QRCode(
    version=1,
   # error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    
)


data="https://th.bing.com/th/id/OIP._EsEEB685g5-J3rLTwz3ngHaEo?pid=ImgDet&rs=1"

data2="https://www.youtube.com/watch?v=qvLMl6YP190"
qr.add_data(data)
qr.make(fit=True)


img=qr.make_image(fill_color="black",back_color="white")

img.save("my_qrcode.png")