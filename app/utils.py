import os
import calendar
import numpy as np
from scipy.interpolate import griddata


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


# 年份—>一年的所有日期 yyyy-mm-dd
def date_of_a_year(year):
    date_list = []
    for month in range(1, 13):
        for i in range(calendar.monthrange(year, month)[1] + 1)[1:]:
            str1 = str(year) + '-' + str("%02d" % month) + '-' + str("%02d" % i)
            date_list.append(str1)
    return date_list


def get_wind_of_that_day(year, month, day):
    filename = 'CN-Reanalysis-daily-' + year + month.zfill(2) + day.zfill(2) + '00.csv'
    path = "./csv_data/" + year + month.zfill(2) + '/'
    with open(path + filename, 'r') as daily_file:
        file = path + filename
        u = np.loadtxt(file, skiprows=1, dtype=np.float, delimiter=",", usecols=(6,), encoding='utf-8')
        v = np.loadtxt(file, skiprows=1, dtype=np.float, delimiter=",", usecols=(7,), encoding='utf-8')
        lat = np.loadtxt(file, skiprows=1, dtype=np.float, delimiter=",", usecols=(11,), encoding='utf-8')
        lon = np.loadtxt(file, skiprows=1, dtype=np.float, delimiter=",", usecols=(12,), encoding='utf-8')
        lats, lons = np.mgrid[18.33:53.61:0.2, 73.65:135.19:0.2]
        z = griddata((lon, lat), u, (lons, lats), method='linear')  # new
        z = np.nan_to_num(z)
        z2 = griddata((lon, lat), v, (lons, lats), method='linear')  # new
        z2 = np.nan_to_num(z2)
        np.savetxt('./csv_data/u.txt', z, fmt="%.2f", delimiter=',', newline=',')
        np.savetxt('./csv_data/v.txt', z2, fmt="%.2f", delimiter=',', newline=',')
