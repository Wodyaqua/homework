import requests
import decimal
import datetime


currency = input('Введите код валюты: ').upper()


def currency_rates(currency):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if currency in response:
        val = response[
              response.find('<Value>', response.find(currency)) + 7:response.find('</Value>', response.find(currency))]
        date = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
        datetime.datetime(day=int(date[0]), month=int(date[1]), year=int(date[2]))
        return f"{currency}/RUB {decimal.Decimal(val.replace(',', '.'))} " \
               f"{datetime.datetime(day=int(date[0]), month=int(date[1]), year=int(date[2]))}"
    else:
        return None


print(currency_rates(currency))
