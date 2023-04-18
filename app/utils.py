import os


# 省市名->文件名
def changeFileName(province, city=None):
    if city:
        return province + '-' + city + '.json'
    else:
        return province + '.json'


def find_prefix_of_path(path, file_list, word):
    # path = "./city_daily_data/"
    files = os.listdir(path)
    for file_name in files:
        file_path = os.path.join(path, file_name)

        if os.path.isdir(file_path):
            find_prefix_of_path(file_path, file_list)
        elif os.path.isfile(file_path) and word in file_name:
            # elif os.path.isfile(file_path) and u'项目' in file_name:
            file_list.append(file_path)


# 日期->一年内的第几天
def date_to_sum(year, month, day):
    sum = 0
    months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    for i in range(month - 1):
        sum += months[i]
    sum += day
    leap = 0
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        leap = 1
    if leap == 1 and month > 2:
        sum += 1
    # print("It is the {} day".format(sum))
    return sum
