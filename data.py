import csv
import os

readfile_name = 'hydata_swjl_0'
read_name = readfile_name + '.csv'
write_name = readfile_name + '_new.csv'

# 读取csv
csvFile = open(read_name, "r")
reader = csv.reader(csvFile)

# 写入csv
#csvFile2 = open(write_name, "wb")
#writer = csv.writer(csvFile2)

fileHeader = ["PERSONID","SITEID","XB","CUSTOMERNAME","ONLINEYEAR","ONLINEMONTH","ONLINEDAY","ONLINEHOUR","ONLINEMINUTE","ONLINESECOND","OFFLINEYEAR","OFFLINEMONTH","OFFLINEDAY","OFFLINEHOUR","OFFLINEMINUTE","OFFLINESECOND","AREAID","BIRTHYEAR","BIRTHMONTH","BIRTHDAY","ISTEENAGER","DATABROKEN"]
#writer.writerow(fileHeader)

data = []


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
    
    
    user_age = int(item[4][0:4]) - int(item[7][0:4])
    surfing_hour = int(item[5][8:10]) - int(item[4][8:10])
    surfing_hour %= 24
    is_working_time = int(item[4][0:4]) > 8 & int(item[4][0:4]) < 16
    
    #未成年人直接上网
    if user_age <= 18:
        d.append(1)
    #上网时间过长
    elif surfing_hour >= 16:
        d.append(1)
    # 成年人工作时间上网
    #elif user_age >= 25 & is_working_time:
    #    d.append(1)
    else:
        d.append(0)
        
    print d[20]

        
        
        
    #print(d)
    data.append(d)
    #writer.writerow(d)


csvFile.close()
#csvFile2.close()



#print data

# 按照时间创建目录并按照地点创建文件
if os.path.exists("data") == False:
    os.makedirs("data")

for item in data:
    time_path = 'data/' + str(item[4]) + '-' + str(item[5]) + '-' + str(item[6])
    if os.path.exists(time_path) == False:
        os.makedirs(time_path)
    file_path = time_path + '/' + item[1] + '.csv'
    if os.path.isfile(file_path):
        tempCsvFile = open(file_path, "ab")
        writer = csv.writer(tempCsvFile)
    else:
        tempCsvFile = open(file_path, "wb")
        writer = csv.writer(tempCsvFile)
        writer.writerow(fileHeader)
    writer.writerow(item)
    tempCsvFile.close()    






