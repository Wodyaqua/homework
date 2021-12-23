import requests
import decimal

currency = input('Введите код валюты: ').upper()


def currency_rates(currency):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if currency in response:
        val = response[
              response.find('<Value>', response.find(currency)) + 7:response.find('</Value>', response.find(currency))]
        return f"{decimal.Decimal(val.replace(',', '.'))} {currency}/RUB"
    else:
        return None


print(currency_rates(currency))
