import os


# 省市名->文件名
def changeFileName(province, city):
    return province + '-' + city + '.json'


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
