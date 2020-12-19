# -*- coding: utf-8 -*-
# WhatsApp Bot

#import necessary libraries
from whatsapp_api import  WhatsApp
from time import sleep


# create the WhatsApp object
wp = WhatsApp()

#workaround to wait the user scanning the QR Code
input("Pressione Enter after scanning QR Code")

contact_names = ['Ge Bot', 'Diego Bot', 'Nedo Bot']

first_names = [n.split(' ')[0] for n in contact_names]

product_list = ['Lettuce', 'Beans', 'Carrots']

for first_name, full_name, product in zip (first_names, contact_names, product_list):
    #search contact
    wp.search_contact(full_name)
    sleep(3)
    
    #create message
    msg = "Hi, {first_name}. Thanks for buying {product}!"
    
    #send message
    wp.send_message(msg)


#wait 10 seconds befor closing Chrome
sleep(10)
wp.driver.close()


