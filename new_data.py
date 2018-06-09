# encoding: utf-8
import csv
import os

readfile_name = 'hydata_swjl_3'
read_name = readfile_name + '.csv'
write_name = readfile_name + '_new.csv'


def read_csv(read_name):
    # 读取csv
    csvFile = open(read_name, "r")
    reader = csv.reader(csvFile)

    # 写入csv
    # csvFile2 = open(write_name, "wb")
    # writer = csv.writer(csvFile2)

    fileHeader = ["PERSONID", "SITEID", "XB", "CUSTOMERNAME", "ONLINEYEAR", "ONLINEMONTH", "ONLINEDAY", "ONLINEHOUR",
                  "ONLINEMINUTE", "ONLINESECOND", "OFFLINEYEAR", "OFFLINEMONTH", "OFFLINEDAY", "OFFLINEHOUR",
                  "OFFLINEMINUTE", "OFFLINESECOND", "AREAID", "BIRTHYEAR", "BIRTHMONTH", "BIRTHDAY", "ISTEENAGER",
                  "DATABROKEN"]
    # writer.writerow(fileHeader)

    data = []

    for item in reader:
        if reader.line_num == 1:
            continue
        try:
            d = []
            d.append(item[0])
            d.append(item[1])
            # 性别
            if item[2] == '男':
                d.append(1)
            else:
                d.append(0)

            d.append(item[3])

            # Online
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

            # Offline
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

            # Birth
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

            # 未成年人直接上网
            if user_age <= 18:
                d.append(1)
            # 上网时间过长
            elif surfing_hour >= 16:
                d.append(1)
            # 成年人工作时间上网
            # elif user_age >= 25 & is_working_time:
            #    d.append(1)
            else:
                d.append(0)
        except:
            print item
            print 'error happen'
            continue
        # print d[20]
        data.append(d)
        # writer.writerow(d)
    print 'finished in first read'
    csvFile.close()
    print '数据项共:' + str(len(data))
    return data


# csvFile2.close()
# print data
def write_csv(data, file_name):
    path_dic = {}
    for item in data:
        time_path = 'data/' + str(item[4]) + '-' + str(item[5]) + '-' + str(item[6])
        if os.path.exists(time_path) == False:
            os.makedirs(time_path)
        file_path = time_path + '/' + item[1] + '.csv'
        if file_path not in path_dic:
            path_dic[file_path] = []
            path_dic[file_path].append(item)
            print 'add path: ' + file_path
        else:
            path_dic[file_path].append(item)
    print 'path_dic length:' + str(len(path_dic))
    # print path_dic['data/2016-11-15/50024210000041.csv']
    # print path_dic['data/2016-11-15/50024010000038.csv']
    # 按照时间创建目录并按照地点创建文件
    if os.path.exists("data") == False:
        os.makedirs("data")

    fileHeader = ["PERSONID", "SITEID", "XB", "CUSTOMERNAME", "ONLINEYEAR", "ONLINEMONTH", "ONLINEDAY", "ONLINEHOUR",
                  "ONLINEMINUTE", "ONLINESECOND", "OFFLINEYEAR", "OFFLINEMONTH", "OFFLINEDAY", "OFFLINEHOUR",
                  "OFFLINEMINUTE", "OFFLINESECOND", "AREAID", "BIRTHYEAR", "BIRTHMONTH", "BIRTHDAY", "ISTEENAGER",
                  "DATABROKEN"]
    count = 0
    path_dic_length = len(path_dic)
    for key in path_dic:
        if os.path.isfile(key):
            tempCsvFile = open(key, "ab")
            writer = csv.writer(tempCsvFile)
        else:
            tempCsvFile = open(key, "wb")
            writer = csv.writer(tempCsvFile)
            writer.writerow(fileHeader)
        for item in path_dic[key]:
            writer.writerow(item)
        tempCsvFile.close()
        print 'finish write file: ' + key
        count += 1
        print '已完成' + file_name + '  ' + str(count) + '/' + str(path_dic_length) + str(count / path_dic_length)


base_filename = 'hydata_swjl_'
for i in range(9, 17):
    # if i != 2 and i != 1:
    file_name = base_filename + str(i) + '.csv'
    print '正在处理:' + file_name
    data = read_csv(file_name)
    write_csv(data, file_name)
# data = read_csv(read_name=read_name)
# write_csv(data)







# length = len(data)
# count = 0
# print data[0]
# for item in data:
#     time_path = 'data/' + str(item[4]) + '-' + str(item[5]) + '-' + str(item[6])
#     if os.path.exists(time_path) == False:
#         os.makedirs(time_path)
#     file_path = time_path + '/' + item[1] + '.csv'
#     if os.path.isfile(file_path):
#         tempCsvFile = open(file_path, "ab")
#         writer = csv.writer(tempCsvFile)
#     else:
#         tempCsvFile = open(file_path, "wb")
#         writer = csv.writer(tempCsvFile)
#         writer.writerow(fileHeader)
#     writer.writerow(item)
#     tempCsvFile.close()
#     print 'finish write file' + file_path
#     count += 1
#     print '已完成' + str(count) + '/' + str(length) + str(count/length)
