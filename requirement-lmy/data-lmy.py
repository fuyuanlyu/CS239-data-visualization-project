import csv
import os
import os.path
import sys


read_path = 'E:\\SJTU_courses\\Computer Science\\Data Visualization\\project\\code\\data-pre\\requirement-lmy\\data_input'
write_path = 'E:\\SJTU_courses\\Computer Science\\Data Visualization\\project\\code\\data-pre\\requirement-lmy'


def read_in_files(input_folder,dataset):
    input_files = os.listdir(input_folder.decode('utf-8'))
    for file in input_files:
        temp_file = input_folder + '\\' + file
        csvFile = open(temp_file,'r')
        reader = csv.reader(csvFile)
        for item in reader:
            if reader.line_num == 1:
                continue
            dataset.append(item)
        csvFile.close()


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
        
        
def fill_dd_format(file_name,item):
    try:
        tempCsvFile = open(file_name, "rb")
        reader = csv.reader(tempCsvFile)
    
        tempDataset = []
    
        for row in tempCsvFile:
            row2 = row.strip()
            row3 = row2.split(',')       
            tempDataset.append(row3)
    
        age = int(item[5][0:4]) - int(item[7][0:4])
    
        start_time = int(item[4][8:10])
        end_time = int(item[5][8:10])

        if age<18:
            t = 0
        elif age < 40:
            t = 1
        elif age < 60:
            t = 2
        else:
            t = 3
        
        for i in range(start_time+1,end_time+1):
            temp = int(tempDataset[i][t])
            temp += 1
            tempDataset[i][t] = str(temp)      
    
    finally:
        tempCsvFile.close()
        
    try:
        tempCsvFile = open(file_name, "wb")
        writer = csv.writer(tempCsvFile)
        for row in tempDataset:
            writer.writerow(row)
    finally:
        tempCsvFile.close()  
    


def handle_dd():
    input_dataset = []
    read_in_files(read_path,input_dataset)

    #输出文件夹
    output_folder = write_path + '\\dd_output'
    overall_output_folder = output_folder + '\\overall'
    clean_or_make_folder(overall_output_folder)

    for item in input_dataset:
        time_output_folder = output_folder + '\\' + item[4][0:4] + '-' + item[4][4:6] + '-' + item[4][6:8]
        clean_or_make_folder(time_output_folder)

    #抬头
    dd_Header = ["<18","18-40","40-60",">60"]
    dd_default = [0,0,0,0]
    dd_time = 24

    #处理数据
    for item in input_dataset:    
        #若需要修改的文件不存在，则创建一个空文件
        overall_file_name = overall_output_folder + '\\' + item[1] + '.csv'
        time_file_name = output_folder + '\\' + item[4][0:4] + '-' + item[4][4:6] + '-' + item[4][6:8] + '\\' + item[1] + '.csv'

        create_empty_files(overall_file_name,dd_Header,dd_default,dd_time)
        create_empty_files(time_file_name,dd_Header,dd_default,dd_time)

        fill_dd_format(overall_file_name,item)
        fill_dd_format(time_file_name,item)
   
    
    
    

def fill_po_format(file_name,item):
    try:
        tempCsvFile = open(file_name, "rb")
        reader = csv.reader(tempCsvFile)
    
        tempDataset = []
    
        for row in tempCsvFile:
            row2 = row.strip()
            row3 = row2.split(',')
       
            tempDataset.append(row3)

        age = int(item[5][0:4]) - int(item[7][0:4])
    
        if age<18:
            t = 0
        elif age < 40:
            t = 1
        elif age < 60:
            t = 2
        else:
            t = 3
        

        temp = int(tempDataset[1][t])
        temp += 1
        tempDataset[1][t] = str(temp)
    
        #print tempDataset
        
    
    finally:
        tempCsvFile.close()
        
    try:
        tempCsvFile = open(file_name, "wb")
        writer = csv.writer(tempCsvFile)
        for row in tempDataset:
            writer.writerow(row)
    finally:
        tempCsvFile.close() 
    

    
def handle_po():
    input_dataset = []
    read_in_files(read_path,input_dataset) 
    
    #输出文件夹
    output_folder = write_path + '\\po_output'
    overall_output_folder = output_folder + '\\overall'
    clean_or_make_folder(overall_output_folder)

    for item in input_dataset:
        time_output_folder = output_folder + '\\' + item[4][0:4] + '-' + item[4][4:6] + '-' + item[4][6:8]
        clean_or_make_folder(time_output_folder)
        
    #抬头
    po_Header = ["<18","18-40","40-60",">60"]
    po_default = [0,0,0,0]
    po_time = 1
    
     #处理数据
    for item in input_dataset:    
        #若需要修改的文件不存在，则创建一个空文件
        overall_file_name = overall_output_folder + '\\' + item[1] + '.csv'
        time_file_name = output_folder + '\\' + item[4][0:4] + '-' + item[4][4:6] + '-' + item[4][6:8] + '\\' + item[1] + '.csv'

        create_empty_files(overall_file_name,po_Header,po_default,po_time)
        create_empty_files(time_file_name,po_Header,po_default,po_time)
        
        fill_po_format(overall_file_name,item)
        fill_po_format(time_file_name,item)


def fill_pi_format(file_name,item):
    try:
        tempCsvFile = open(file_name, "rb")
        reader = csv.reader(tempCsvFile)
    
        tempDataset = []
    
        for row in tempCsvFile:
            row2 = row.strip()
            row3 = row2.split(',')
            tempDataset.append(row3)

        location = item[1][0:2]
        
        if location == '50':
            t = 0
        else:
            t = 1
        
        temp = int(tempDataset[1][t])
        temp += 1
        tempDataset[1][t] = str(temp)
    
        #print tempDataset
        
    
    finally:
        tempCsvFile.close()
        
    try:
        tempCsvFile = open(file_name, "wb")
        writer = csv.writer(tempCsvFile)
        for row in tempDataset:
            writer.writerow(row)
    finally:
        tempCsvFile.close() 



def handle_pi():
    input_dataset = []
    read_in_files(read_path,input_dataset) 
    
    #输出文件夹
    output_folder = write_path + '\\pi_output'
    overall_output_folder = output_folder + '\\overall'
    clean_or_make_folder(overall_output_folder)

    for item in input_dataset:
        time_output_folder = output_folder + '\\' + item[4][0:4] + '-' + item[4][4:6] + '-' + item[4][6:8]
        clean_or_make_folder(time_output_folder)
        
    #抬头
    pi_Header = ["citizen","other"]
    pi_default = [0,0]
    pi_time = 1
    
    for item in input_dataset:    
        #若需要修改的文件不存在，则创建一个空文件
        overall_file_name = overall_output_folder + '\\' + item[1] + '.csv'
        time_file_name = output_folder + '\\' + item[4][0:4] + '-' + item[4][4:6] + '-' + item[4][6:8] + '\\' + item[1] + '.csv'

        create_empty_files(overall_file_name,pi_Header,pi_default,pi_time)
        create_empty_files(time_file_name,pi_Header,pi_default,pi_time)
        
        fill_pi_format(overall_file_name,item)
        fill_pi_format(time_file_name,item)


def prepare_cal_header(input_dataset,cal_header):
    for item in input_dataset:
        date = item[4][0:8]
        cal_header.add(date)



def fill_cal_format(file_name,item):
    try:
        tempCsvFile = open(file_name, "rb")
        reader = csv.reader(tempCsvFile)
    
        tempDataset = []
    
        for row in tempCsvFile:
            row2 = row.strip()
            row3 = row2.split(',')
            tempDataset.append(row3)

        time = item[4][0:8]
        
        #print reader
        
        for t in range(len(item)):
            if tempDataset[0][t] == time:
                break
        
        
        temp = int(tempDataset[1][t])
        temp += 1
        tempDataset[1][t] = str(temp)
        
        #print tempDataset
        
    
    finally:
        tempCsvFile.close()
        
    try:
        tempCsvFile = open(file_name, "wb")
        writer = csv.writer(tempCsvFile)
        for row in tempDataset:
            writer.writerow(row)
    finally:
        tempCsvFile.close()

def handle_cal():
    input_dataset = []
    read_in_files(read_path,input_dataset) 
    
    #输出文件夹
    output_folder = write_path + '\\cal_output'
    overall_output_folder = output_folder + '\\overall'
    clean_or_make_folder(overall_output_folder)
    
    cal_header = set()
    prepare_cal_header(input_dataset,cal_header)
    cal_header = list(cal_header)
    cal_default = ['0' for i in range(len(cal_header))]
    cal_time = 1

    for item in input_dataset:    
        #若需要修改的文件不存在，则创建一个空文件
        overall_file_name = overall_output_folder + '\\' + item[1] + '.csv'

        create_empty_files(overall_file_name,cal_header,cal_default,cal_time)
    
        fill_cal_format(overall_file_name,item)


    

        
    
    
    
def main(argv):
    for arg in argv[1:]:
        if arg == 'dd':
            handle_dd()
        elif arg == 'po':
            handle_po()
        elif arg == 'pi':
            handle_pi()
        elif arg == 'cal':
            handle_cal()
    
    
if __name__ == "__main__":
    main(sys.argv)

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''
    try:
        tempCsvFile = open(file_name, "rb")
        reader = csv.reader(tempCsvFile)
    
        tempDataset = []
    
        for row in tempCsvFile:
            #next(reader,None)
            #if reader.line_num == 1:
                #continue
                #print row
            row2 = row.strip()
            row3 = row2.split(',')
       
            tempDataset.append(row3)
       
        #print tempDataset
    
        age = int(item[5][0:4]) - int(item[7][0:4])
    
        start_time = int(item[4][8:10])
        end_time = int(item[5][8:10])
        #print age
    
        if age<18:
            t = 0
        elif age < 40:
            t = 1
        elif age < 60:
            t = 2
        else:
            t = 3
        
        for i in range(start_time+1,end_time+1):
            temp = int(tempDataset[i][t])
            temp += 1
            tempDataset[i][t] = str(temp)
    
        #print tempDataset
        
    
    finally:
        tempCsvFile.close()
        
    try:
        tempCsvFile = open(file_name, "wb")
        writer = csv.writer(tempCsvFile)
        for row in tempDataset:
            writer.writerow(row)
    finally:
        tempCsvFile.close()    
    '''










'''
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

'''




