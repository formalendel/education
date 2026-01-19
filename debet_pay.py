import pandas as pd
from datetime import date, timedelta, datetime
import argparse
from operator import itemgetter
time_difference = 'Срок до погашения (дней)'
def pars_calculate_debet_payments(dataframe):
    dataframe=pd.read_excel('Debet_pay.xlsx')
    dataframe['долг'] = dataframe['Сумма договора'] - dataframe['Оплачено']
    filtered_df = dataframe[dataframe['долг'] > 0]
    today = pd.to_datetime(datetime.now())
    filtered_df[time_difference] = (filtered_df['Дата погашения'] - today).dt.days
    result = filtered_df[['Ф.И.О.', 'долг', time_difference]]
    return result
# print(pars_calculate_debet_payments('Debet_pay.xlsx'))


# parser = argparse.ArgumentParser(description='Сортировка по заданному полю')
# parser.add_argument('--sort_by', type=str, choices=['Ф.И.О.', 'долг', 'time_difference'], help='Поле для сортировки')
# args = parser.parse_args()
# result = pars_calculate_debet_payments('Debet_pay.xlsx').to_dict('records')
# sorted_result = sorted(result, key=itemgetter(args.sort_by))
# print(f"Отсортировано по {args.sort_by}:")
# for item in sorted_result:
#     print(item)