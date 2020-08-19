# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 12:07:26 2020

@author: Madhan Kumar
"""

import io
import re
import csv
import configuration

def date_time(string, pattern):
    try:
        return re.findall(pattern, string)[0]
    except:
        return ""
    
def chat_generator(WAfile, filename):
    chat_list = []  
    unique_names = set()
    name_dict = {}
    check_date = None
#    text_convert = open(configuration.file_name,"r", encoding='utf-8')
    file = WAfile.decode("utf-8") 
    text_convert = io.StringIO(file)
    content = text_convert.readlines()
#    print(content)
    if filename == "statistics":
        with open(configuration.csv_file_path, 'w+', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Date", "Time", "Chat"])
    for each_chat in content:
        try:
            name_result = re.findall(configuration.name_addon_pattern, re.findall(configuration.name_pattern, each_chat)[0])[0]
            unique_names.add(name_result)            
        except:
            pass
    len_unique_names = len(unique_names)
    
        
    for index, name in enumerate(unique_names):
        name_dict[name] = index        
    for each_chat in content:    
        date_result = date_time(each_chat, configuration.date_pattern)
        time_result = date_time(each_chat, configuration.time_pattern)        
        try:
            chat_result = re.findall(configuration.chat_pattern, each_chat)[0].replace(": ", "")
        except:
            chat_result = ""           
        try:
            name_result = re.findall(configuration.name_addon_pattern, re.findall(configuration.name_pattern, each_chat)[0])[0]                        
        except:
            name_result = "" 
        name_result_copy = name_result
        try:
            attachment_result = re.findall(configuration.attachment_pattern, each_chat)[0]
            chat_result = " "
        except:
            attachment_result = ""    
        if(filename != "statistics"):
            if (date_result != check_date):
                check_date = date_result
            else:
                date_result = ""        
        try:
            name_result = name_dict[name_result]
        except:
            name_result = ""            
        if (chat_result != "") & (filename != "statistics") :
            list_data = [date_result, time_result, name_result, chat_result, attachment_result, name_result_copy]
            chat_list.append(list_data) 
        elif(chat_result != "") & (filename == "statistics"):
            list_data = [name_result_copy, date_result, time_result, chat_result]
            with open(configuration.csv_file_path, 'a+', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(list_data)
            
        date_result = time_result = name_result = chat_result = attachment_result = ""
        if filename != "statistics":
            if len_unique_names==2:
                for chat_name in unique_names:
                    pass
            else:
                chat_name = re.findall(configuration.group_name_pattern, filename)[0].replace("with ","").replace(".txt","")
    
    if filename != "statistics":
        return chat_name, chat_list, len_unique_names
    elif filename == "statistics":
        return "success"
        
#print(chat_generator(1,1))

