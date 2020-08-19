# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 09:35:03 2020

@author: Madhan Kumar
"""

#file_name = r"E:\Coding\Interview\Whatsappbook\Solo\WhatsApp Chat with idiotzzz😘🥰.txt"
file_name = r"E:\Coding\Interview\Whatsappbook\Solo\WhatsApp Chat with Preethi Bhopal. Student.txt"

date_pattern = '\d\d\/\d\d\/\d\d\d\d'
time_pattern = '\d\d\:\d\d'
name_pattern = '- \w.*\S\)?: '
name_addon_pattern = "\w.*\w"
chat_pattern = ': .*'
attachment_pattern = "IMG\S*"
group_name_pattern = "with .*\.txt"
csv_file_path = "WAchat.csv"

color_code_dict = {2: "#D4CDB4",3: "#C4B4D4",4: "#D7846B",5: "#E0F588",6: "#94D785",7: "#71CFB4",8: "#729CB9",9: "#B5A7E6"}