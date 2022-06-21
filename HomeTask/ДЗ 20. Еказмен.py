# City Info
# Максимальний бал: 95
# Реалізувати отримання інформації про місто за допомогою Python.
#
# User story: При запуску файлу користувач вводить назву міста,
# система повертає назву міста, країни, валюти та кількості населення
#
# Технічні вимоги: Ввод реалізувати за допомогою інтерфейсу командного рядку.
# Звідки отримувати інформацію - на вибір розробника.
# Формат вводу - за допомогою аргументів запуску (як у прикладі).

import requests
import json
import argparse


class Cmd_argparse():

    def __init__(self):
        self.id = 0

    def run_argparse(self):
        """
        description
        :return:
        """
        parser = argparse.ArgumentParser(description='Process get info area')
        parser.add_argument(
            'id',  # імʼя аргументу
            type=int,  # очікуваний тип
            nargs=1,  # кількість аргументів
            help='id area, 0 - get all areas',  # текст підказки для користувача
        )

        args = parser.parse_args()

        return args


class Areas:
    def __init__(self, url=""):
        if url == "":
            url = "https://decentralization.gov.ua/graphql"
        self.url = url

    def __requests_get_all_areas(self):

        str_query = "?query={areas{title, id}}"
        URL_ALL_AREAS = f'{self.url}{str_query}'

        response = requests.post(URL_ALL_AREAS)

        return response

    def __requests_get_areas_by_id(self, id):
        str_col = "{title, id, square, population, " \
                  "local_community_count, percent_communities_from_area,sum_communities_square}"

        str_id = f'area(id: "{id}")'

        str_query = "{" + f'{str_id}{str_col}' + "}"

        URL_BY_ID = f"{self.url}?query={str_query}"

        response = requests.post(URL_BY_ID)

        return response

    def get_all_areas(self):

        NEW_DICT = {}

        resp_json = self.__requests_get_all_areas()

        if resp_json.status_code == 200:

            json_text = resp_json.text

            json_dict = json.loads(json_text)

            list_areas = json_dict["data"]["areas"]

            for ls in list_areas:
                NEW_DICT[ls["id"]] = ls["title"]

            return NEW_DICT

        else:
            return f'error {resp_json}, {resp_json.text}'

    def get_area_by_id(self, id):

        NEW_DICT = {}

        resp_json = self.__requests_get_areas_by_id(id)

        if resp_json.status_code == 200:

            json_text = resp_json.text

            json_dict = json.loads(json_text)

            dict_info = json_dict["data"]["area"]

            NEW_DICT["Найменування області:"] = dict_info["title"]
            NEW_DICT["Площа:"] = dict_info["square"]
            NEW_DICT["Населення:"] = dict_info["population"]

            return NEW_DICT

        else:
            return f'error {resp_json}, {resp_json.text}'


# areas = Areas()
# list_areas = areas.get_all_areas()
# print(list_areas)

# info_area = areas.get_area_by_id(10)
# print(info_area)
#
if __name__ == '__main__':
    cmd_args = Cmd_argparse()

    args = cmd_args.run_argparse()

    list_id = args.id
    print(list_id)

    id = list_id[0]

    areas = Areas()

    if id == 0:
        list_areas = areas.get_all_areas()
        print(list_areas)
    else:
        info_area = areas.get_area_by_id(id)
        print(info_area)


