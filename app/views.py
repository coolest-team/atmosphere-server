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
def getTotalPolluted(request):
    province = request.GET.get("province")
    city = request.GET.get("city")
    arrnew = []
    # temp_dict = json.loads("/city_daily_data/"+changeFileName(province, city))
    with open("./city_daily_data/"+changeFileName(province=province, city=city), 'r') as city_file:
        city_data = json.load(city_file)
        # print(city_data)
        for key in range(len(city_data)):
            arrnew.append(city_data[key]['PM2.5'])
            # print(city_data[key]['PM2.5'])
    # return HttpResponse(arrnew)
    return JsonResponse({'code': 0, 'data': arrnew, 'message': '提交成功'})

# for平行坐标图
# 获取某日某个省内所有市的污染程度
def getCityPolluted(request):
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
                    # print(city_data[key]['date'])
                    if date == city_data[key]['date']:
                        # print(file)
                        arrnew.append(city_data[key])
    return JsonResponse({'code': 0, 'data': arrnew, 'message': '提交成功'})

# for平行坐标图
# 获取某日所有省的污染程度（还没写）
def getProvincePolluted(request):
    date = request.GET.get("date")
    path = "./province_daily_data"
    files = os.listdir(path)
    arrnew = []
    for file in files:
        with open(path+file, 'r') as province_file:
            province_data = json.load(province_file)
            for key in range(len(province_data)):
                if date == province_data[key]['date']:
                    arrnew.append(province_data[key])
    return JsonResponse({'code': 0, 'data': '', 'message': '提交成功'})

# for时间轴面板
# 获取全年各省的污染等级（还没写）
def getProvinceLevelByYear(request):
    year = request.GET.get("year")
    path = "./province_daily_data"
    files = os.listdir(path)
    arrnew = []
    for file in files:
        with open(path + file, 'r') as province_file:
            province_data = json.load(province_file)
            for key in range(len(province_data)):
                if year in province_data[key]['date']:
                    # print(file)
                    arrnew.append(province_data[key])
    return JsonResponse({'code': 0, 'data': '', 'message': '提交成功'})



