
"""Скрипт який конвертує існуючий файл у форматі json у формат csv.
Також фільтрує записи. Файл у форматі JSON додано до завдання.

Допомагаємо HR департаменту.

Зчитати данні з файлу "people_db.json"
Відфільтрувати та залишити лише записи в яких:
Немає компанії (У 'company_name' пусто)
Також є номер телефону (У 'phone' не пусто)
Також є слово software у назві посади ('job_title')
Відфільтровані данні записати у файл в форматі CSV


P.s. Результатом вашого домашнього завдання,
як завжди, має бути код скрипту на GitHub, а не результуючий CSV файл.
"""

import pandas as pd


def read_json(file_json):
    """
        use pandas for read json file
        Parameters:
            file_json(string): path file .json
        Returns:
            dataframe: convert json to dataframe
    """

    data_frame = pd.read_json(file_json)

    return data_frame


def df_query(data_frame, query_str):

    """
    Parameters:
        data_frame(dataframe): dataframe pandas
        query_str(string): query string:
    Returns:
         dataframe: result query
    """

    result = data_frame.query(query_str)

    return result


def save_to_csv_result(result, file_csv):

    """ save result to file csv"""

    result.to_csv(file_csv, index=None)


def help_hr():

    """def help hr main def"""

    file_json = "people_db.json"

    data_frame = read_json(file_json)

    query_str = "(company_name == '') and (phone != '') and (job_title.str.contains ('software'))"

    result = df_query(data_frame, query_str)

    file_json = "new_people_db.csv"

    save_to_csv_result(result, file_json)


help_hr()
