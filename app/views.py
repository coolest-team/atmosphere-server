import json
import os
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from app.utils import *


# Create your views here.

def index(request):
    return HttpResponse("欢迎使用")

# for热力图
# 获取某市全年的空气污染程度
def getCityPollutedHeat(request):
    year = request.GET.get("year")
    province = request.GET.get("province")
    city = request.GET.get("city")
    arrnew = []
    ori_month = 1
    with open("./city_daily_data/"+changeFileName(province=province, city=city), 'r') as city_file:
        city_data = json.load(city_file)
        temp_list = []
        for key in range(len(city_data)):
            if year in city_data[key]["date"]:
                month = int(city_data[key]["date"][5:7])
                level = int(city_data[key]['AQI'] // 50)  # 污染等级
                if month == ori_month:
                    temp_list.append(level)
                else:
                    ori_month += 1
                    arrnew.append(temp_list)
                    temp_list = [level]
    return JsonResponse({'code': 0, 'data': arrnew, 'message': '提交成功'})

# for热力图
# 获取某省全年的空气污染程度
def getProvincePollutedHeat(request):
    year = request.GET.get("year")
    province = request.GET.get("province")
    arrnew = []
    ori_month = 1
    with open("./province_daily_data/"+changeFileName(province=province), 'r') as province_file:
        province_data = json.load(province_file)
        temp_list = []
        for key in range(len(province_data)):
            if year in province_data[key]["date"]:
                month = int(province_data[key]["date"][5:7])
                level = int(province_data[key]['AQI'] // 50)  # 污染等级
                if month == ori_month:
                    temp_list.append(level)
                else:
                    ori_month += 1
                    arrnew.append(temp_list)
                    temp_list = [level]
    return JsonResponse({'code': 0, 'data': arrnew, 'message': '提交成功'})

# for平行坐标图
# 获取某日某个省内所有市的污染程度
def getCityPollutedParallel(request):
    date = request.GET.get("date")
    province = request.GET.get("province")
    file_list = []
    path = "./city_daily_data/"
    find_prefix_of_path(path=path, file_list=file_list, word=province)
    print(file_list)
    files = os.listdir(path)
    arrnew = []
    for file in files:
        if path+file in file_list:
            with open(path+file, 'r') as city_file:
                city_data = json.load(city_file)
                for key in range(len(city_data)):
                    if date == city_data[key]['date']:
                        AQI = city_data[key]["AQI"]
                        pm2p5 = city_data[key]["PM2.5"]
                        pm10 = city_data[key]["PM10"]
                        so2 = city_data[key]["SO2"]
                        no2 = city_data[key]["NO2"]
                        co = city_data[key]["CO"]
                        o3 = city_data[key]["O3"]
                        level = int(AQI//50)
                        if level == 0:
                            evaluate = "优"
                        elif level == 1:
                            evaluate = "良"
                        elif level == 2:
                            evaluate = "轻度污染"
                        elif level == 3:
                            evaluate = "中度污染"
                        elif level == 4:
                            evaluate = "重度污染"
                        else:
                            evaluate = "严重污染"
                        arrnew.append([AQI, pm2p5, pm10, so2, no2, co, o3, evaluate])
    return JsonResponse({'code': 0, 'data': arrnew, 'message': '提交成功'})

# for平行坐标图
# 获取某日全国所有省的污染程度
def getProvincePollutedParallel(request):
    date = request.GET.get("date")
    path = "./province_daily_data/"
    files = os.listdir(path)
    arrnew = []
    for file in files:
        with open(path+file, 'r') as province_file:
            province_data = json.load(province_file)
            for key in range(len(province_data)):
                if date == province_data[key]['date']:
                    AQI = province_data[key]["AQI"]
                    pm2p5 = province_data[key]["PM2.5"]
                    pm10 = province_data[key]["PM10"]
                    so2 = province_data[key]["SO2"]
                    no2 = province_data[key]["NO2"]
                    co = province_data[key]["CO"]
                    o3 = province_data[key]["O3"]
                    level = int(AQI // 50)
                    if level == 0:
                        evaluate = "优"
                    elif level == 1:
                        evaluate = "良"
                    elif level == 2:
                        evaluate = "轻度污染"
                    elif level == 3:
                        evaluate = "中度污染"
                    elif level == 4:
                        evaluate = "重度污染"
                    else:
                        evaluate = "严重污染"
                    arrnew.append([AQI, pm2p5, pm10, so2, no2, co, o3, evaluate])
    return JsonResponse({'code': 0, 'data': arrnew, 'message': '提交成功'})

# for时间轴面板
# 获取全年各省的污染等级
def getTimeline(request):
    year = request.GET.get("year")
    path = "./province_daily_data/"
    files = os.listdir(path)
    arrnew = []
    days = 365
    if year == "2016":
        days = 366
    good = [0 for n in range(days)]  # 优
    moderate = [0 for n in range(days)]  # 良
    little = [0 for n in range(days)]  # 轻度污染
    unhealthy = [0 for n in range(days)]  # 重度污染
    dangerous = [0 for n in range(days)]  # 重度污染
    hazardous = [0 for n in range(days)]  # 严重污染
    # print(good)
    for file in files:
        with open(path + file, 'r') as province_file:
            province_data = json.load(province_file)
            for key in range(len(province_data)):
                if year in province_data[key]['date']:
                    year_int = int(year)
                    month = int(province_data[key]["date"][5:7])
                    day = int(province_data[key]["date"][8:10])
                    AQI = province_data[key]["AQI"]
                    level = int(AQI // 50)
                    if level == 0:
                        good[date_to_sum(year_int, month, day) - 1] += 1
                    elif level == 1:
                        moderate[date_to_sum(year_int, month, day) - 1] += 1
                    elif level == 2:
                        little[date_to_sum(year_int, month, day) - 1] += 1
                    elif level == 3:
                        unhealthy[date_to_sum(year_int, month, day) - 1] += 1
                    elif level == 4:
                        dangerous[date_to_sum(year_int, month, day) - 1] += 1
                    else:
                        hazardous[date_to_sum(year_int, month, day) - 1] += 1
                    # arrnew.append(province_data[key])
    return JsonResponse({'code': 0, 'data': {"good": good, "moderate": moderate, "little": little, "unhealthy": unhealthy, "dangerous": dangerous, "hazardous": hazardous}, 'message': '提交成功'})