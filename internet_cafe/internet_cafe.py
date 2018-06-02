# -*- coding: utf-8 -*-
"""
Created on Sat Jun 02 10:12:16 2018

@author: Thinkpad
"""

import os
import csv
import sys


read_path= "E:\\SJTU_courses\\Computer Science\\Data Visualization\\project\\code\\data-pre\\test_data\\input_log"
write_path="E:\\SJTU_courses\\Computer Science\\Data Visualization\\project\\code\\data-pre\\test_data"
internet_path= "E:\\SJTU_courses\\Computer Science\\Data Visualization\\project\\code\\data-pre\\test_data\\internet_cafe"
portrait_path=write_path + '\\portrait'


file_Header = ["PERSONID","SITEID","XB","CUSTOMERNAME","ONLINEYEAR","ONLINEMONTH","ONLINEDAY","ONLINEHOUR","ONLINEMINUTE","ONLINESECOND","OFFLINEYEAR","OFFLINEMONTH","OFFLINEDAY","OFFLINEHOUR","OFFLINEMINUTE","OFFLINESECOND","AREAID","BIRTHYEAR","BIRTHMONTH","BIRTHDAY","ISTEENAGER","DATABROKEN"]

def clean_or_make_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    else:
        files = os.listdir(folder.decode('utf-8'))
        for file in files:
            os.remove(folder + '\\' + file)
            
            
def create_empty_files(file_name,header,default,times):
    if not os.path.isfile(file_name):
        #print 'File does not exist'
        tempCsvFile = open(file_name, "wb")
        writer = csv.writer(tempCsvFile)
        writer.writerow(header)
        for i in range(times):
            writer.writerow(default)
        tempCsvFile.close()




def read_in_files(input_folder,dataset):
    input_files = os.listdir(input_folder.decode('utf-8'))
    for file in input_files:
        temp_file = input_folder + '\\' + file
        csvFile = open(temp_file,'r')
        reader = csv.reader(csvFile)
        for item in reader:
            if reader.line_num == 1:
                continue

            d = []
            d.append(item[0])
            d.append(item[1])

    
            #性别
            if item[2]=='男':
                d.append(1)
            else:
                d.append(0)
    
            d.append(item[3])
    
    
            #Online
            temp = item[4]
            temp_year = int(temp[0:4])
            temp_month = int(temp[4:6])
            temp_day = int(temp[6:8])
            temp_hour = int(temp[8:10])
            temp_minute = int(temp[10:12])
            temp_second = int(temp[12:14])
    
            d.append(temp_year)
            d.append(temp_month)
            d.append(temp_day)
            d.append(temp_hour)
            d.append(temp_minute)
            d.append(temp_second)
    
            #Offline
            temp = item[5]
            temp_year = int(temp[0:4])
            temp_month = int(temp[4:6])
            temp_day = int(temp[6:8])
            temp_hour = int(temp[8:10])
            temp_minute = int(temp[10:12])
            temp_second = int(temp[12:14])
    
            d.append(temp_year)
            d.append(temp_month)
            d.append(temp_day)
            d.append(temp_hour)
            d.append(temp_minute)
            d.append(temp_second)
        
    
            d.append(item[6])
    
    
            #Birth
            temp = item[7]
            temp_year = int(temp[0:4])
            temp_month = int(temp[4:6])
            temp_day = int(temp[6:8])
            
            d.append(temp_year)
            d.append(temp_month)
            d.append(temp_day)
            
            #此处默认不是未成年人，数据也没有损坏
            d.append(False)
            d.append(False)
            
            dataset.append(d)
        csvFile.close()
        
def read_in_cafe(input_folder,dataset):
    input_files = os.listdir(input_folder.decode('utf-8'))
    for file in input_files:
        temp_file = input_folder + '\\' + file
        csvFile = open(temp_file,'r')
        reader = csv.reader(csvFile)
        for item in reader:
            if reader.line_num == 1:
                continue
            d = []
            d = item
            del d[4]
            d.append(0)
            d.append(0)
            dataset.append(d)
        csvFile.close()
    
def find_cafe_by_id(id,dataset):
    for index,item in enumerate(dataset):
        if item[0] == id:
            return index
            break
    return -1



def count_people(internet_cafe,input_dataset):
    for item in input_dataset:
        index = find_cafe_by_id(item[1],internet_cafe)
        internet_cafe[index][4] += 1
    
def count_teenager(internet_cafe,input_dataset):
    for item in input_dataset:
        if item[20] == True:
            index = find_cafe_by_id(item[1],internet_cafe)
            if index != -1:
                internet_cafe[index][5] += 1
                
def count_teenager2(internet_cafe,path):
    files = os.listdir(path.decode('utf-8'))
    for file in files:
        temp_file = path + '\\' + file
        #print temp_file
        with open(temp_file,'rb') as csvFile:
            reader = csv.DictReader(csvFile)
            for item in reader:
                #print item['ISTEENAGER']
                if item['ISTEENAGER']:
                    #print 'hi'
                    index = find_cafe_by_id(item['SITEID'],internet_cafe)
                    if index != -1:
                        internet_cafe[index][5] += 1
                        #print internet_cafe[index][5]

             
def append_to_portrait(file_name,item):
    csvFile = open(file_name,'ab')
    writer = csv.writer(csvFile)
    writer.writerow(item)
    csvFile.close()
    
                
                
def draw_one_portrait(item):   
    portrait_Header = file_Header   
    portrait_time = 0
    portrait_default = []
    
    file_name = portrait_path + '\\' + item[0] + '.csv'
    #print file_name
    create_empty_files(file_name,portrait_Header,portrait_default,portrait_time)
    append_to_portrait(file_name,item)
    

def draw_portraits(input_dataset):
    clean_or_make_folder(portrait_path)
    for item in input_dataset:
        #print item
        draw_one_portrait(item)
    
def analyze_portraits(path):
    files = os.listdir(path.decode('utf-8'))
    
    for file in files:
        temp_file = portrait_path + '\\' + file
        black_list = False
        with open(temp_file,'rb') as csvFile:
            reader = csv.DictReader(csvFile)
            for item in reader:
                if reader.line_num == 1:
                    continue
            
                #analyze teenager
                age = int(item['ONLINEYEAR'])-int(item['BIRTHYEAR'])
                #18岁，直接判断
                if age < 18:
                    item['ISTEENAGER'] = True
                    
                
                online_time = int(item['OFFLINEYEAR']) - int(item['ONLINEYEAR'])
                online_time %= 24
                #上网时长过长
                if online_time >= 14:
                    item['ISTEENAGER'] = True
                    black_list = True
                    break
                    
                #同时或者在3h内出现在两个网吧
                for item2 in reader:
                    month_interval = int(item['ONLINEMONTH']) - int(item2['OFFLINEMONTH'])
                    month_interval2 = int(item['OFFLINEMONTH']) - int(item2['ONLINEMONTH'])
                    day_interval = int(item['ONLINEDAY']) - int(item2['OFFLINEDAY']) + 30*month_interval
                    day_interval2 = int(item2['ONLINEDAY']) - int(item['OFFLINEDAY']) + 30*month_interval2
                    hour_interval = int(item['ONLINEHOUR']) - int(item2['OFFLINEHOUR']) + 24*day_interval
                    hour_interval2 = int(item2['ONLINEHOUR']) - int(item['OFFLINEHOUR']) + 24*day_interval2
                    if abs(hour_interval) <= 3 | abs(hour_interval2) <= 3:
                        black_list = True
                        break
                if black_list:
                    break
                
                #成年人多次在上班时间上网
                work_hour_record = 0
                if age >= 30 & age <=45:
                    if int(item['ONLINEHOUR']) >= 10 & int(item['ONLINEHOUR']) <= 14:
                        work_hour_record += 1
                                    
                if work_hour_record >= 3:
                    black_list = True               
                    break;
                    
                    
                
            if black_list:
                for item in reader:
                    item['ISTEENAGER'] = True
   

def write_overall_internet_cafe_file(path,dataset):
    cafe_path = path + '\\internet_cafe_write'
    overall_file = cafe_path + '\\overall.csv'
            
    clean_or_make_folder(cafe_path)
    
    internet_cafe_Header = ['SITEID','TITLE','lng','lat','NUM','TEENAGER_NUM']
    internet_cafe_time = 0
    internet_cafe_default = ['0' for i in range(len(internet_cafe_Header))]
    
    create_empty_files(overall_file,internet_cafe_Header,internet_cafe_default,internet_cafe_time)
    

    with open(overall_file,'ab') as tempCsvFile:
        writer = csv.writer(tempCsvFile)
        for item in dataset:
            writer.writerow(item)
   
def write_internet_cafe_files(path,internet_cafe,portrait_path,input_dataset):
    cafe_path = path + '\\internet_cafe_write'
    internet_cafe_Header = ['SITEID','TITLE','lng','lat','NUM','TEENAGER_NUM']
    internet_cafe_time = 0
    internet_cafe_default = ['0' for i in range(len(internet_cafe_Header))]
    
    #创建空文件夹
    for item in input_dataset:
        temp_file = cafe_path + '\\' + str(item[4]) + '-' + str(item[5]) + '-' + str(item[6]) + '.csv'
        create_empty_files(temp_file,internet_cafe_Header,internet_cafe_default,internet_cafe_time)
    
    target_files = os.listdir(cafe_path.decode('utf-8'))
    for file in target_files:
        if file == 'overall.csv': 
            continue
        
        temp_time_origin = file.split('.')
        temp_time = temp_time_origin[0].split('-')
        temp_time[0] = int(temp_time[0])
        temp_time[1] = int(temp_time[1])
        temp_time[2] = int(temp_time[2])
        #print temp_time
        
        read_in_cafe(internet_path,internet_cafe)
        
        
        portrait_path = path + '\\portrait'
        portrait_files = os.listdir(portrait_path.decode('utf-8'))
        for file2 in portrait_files:
            temp_file = portrait_path + '\\' + file2
            with open(temp_file,'rb') as readFile:
                reader = csv.DictReader(readFile)
                for item in reader:
                    #print int(item['ONLINEYEAR']) == temp_time[0] and int(item['ONLINEMONTH']) == temp_time[1] and int(item['ONLINEDAY']) == temp_time[2]
                    if int(item['ONLINEYEAR']) == temp_time[0] and int(item['ONLINEMONTH']) == temp_time[1] and int(item['ONLINEDAY']) == temp_time[2]:
                        index = find_cafe_by_id(item['SITEID'],internet_cafe)
                        if not index == -1:
                            internet_cafe[index][4] += 1
                            if item['ISTEENAGER']:
                                internet_cafe[index][5] += 1
                            print file
                
        
        
        #print internet_cafe
        write_file = cafe_path + '\\' + file
        #print write_file
        with open(write_file,'wb') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(internet_cafe_Header)
            for item in internet_cafe:
                writer.writerow(item)
    
    
    '''
    portrait_path = path + '\\portrait'    
    files = os.listdir(portrait_path.decode('utf-8'))
    for file in files:
        temp_file = portrait_path + '\\' + file
        #print temp_file
        with open(temp_file,'rb') as csvFile:
            reader = csv.reader(csvFile)
            for item in reader:
                print item
                
                write_file = cafe_path + '\\' + str(item[4]) + '-' + str(item[5]) + '-' + str(item[6]) + '.csv'
                with open(write_file,'ab') as writeFile:
                    writer = csv.writer(writeFile)
                    writer.writerow(item)
    '''            
                


def handle_main():
    input_dataset = []
    read_in_files(read_path,input_dataset)
    
    internet_cafe = []
    read_in_cafe(internet_path,internet_cafe)
    
    
    draw_portraits(input_dataset)
    analyze_portraits(portrait_path)
    
    count_people(internet_cafe,input_dataset)
    count_teenager2(internet_cafe,portrait_path)
    
    #print input_dataset
    #print internet_cafe
    #print find_cafe_by_id('50011810000032',internet_cafe)
    
    write_overall_internet_cafe_file(write_path,internet_cafe)
    write_internet_cafe_files(write_path,internet_cafe,portrait_path,input_dataset)
    

    


def main(argv):
    handle_main()
    
    
if __name__ == "__main__":
    main(sys.argv)
