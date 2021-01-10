__author__ = 'Vinicius wovst @ viniciuswovst in GitHub'
__version__ = '1.0'

# Copyright 2020-2021 Vinicius Wovst, viniciuswovst @ GitHub
# See LICENSE for details.

from bs4 import BeautifulSoup

import requests
import pandas as pd
from datetime import date

from .utils.api import get_data, get_fields_date
from .utils.format_data import format_data

class Reuters:    
    def get_income_statement(self, ticker_list, yearly=True):
        list_values = []
        for ticker in ticker_list:
            income = get_data(ticker, 'income', yearly)
            metricas = income.keys()

            for item in metricas:
                metrica = item
                periodos = income[item]
                list_values = list_values+format_data(ticker, 'income_statement', metrica, periodos, yearly)
        df = pd.DataFrame (list_values)
        return df

    
    def get_cash_flow(self, ticker_list, yearly=True):
        list_values = []
        for ticker in ticker_list:
            income = self.get_data(ticker, 'cash_flow', yearly)
            metricas = income.keys()

            for item in metricas:
                metrica = item
                periodos = income[item]
                list_values = list_values+format_data(ticker, 'cash_flow', metrica, periodos, yearly)
        df = pd.DataFrame (list_values)
        return df

    def get_balance_sheet(self, ticker_list, yearly=True):
        list_values = []
        for ticker in ticker_list:
            income = get_data(ticker, 'balance_sheet', yearly)
            metricas = income.keys()

            for item in metricas:
                metrica = item
                periodos = income[item]
                list_values = list_values+format_data(ticker, 'balance_sheet', metrica, periodos, yearly)
        df = pd.DataFrame (list_values)
        return df

    def get_key_metrics(self, ticker_list):
        today = date.today()
        list_values = []
        for ticker in ticker_list:
            req = requests.get('https://www.reuters.com/companies/%s/key-metrics'% ticker)

            fields_date = get_fields_date(ticker)

            if req.status_code == 200:
                content = req.content
                soup = BeautifulSoup(content, 'lxml')
                div_table = soup.find_all(name='div', attrs={'class':'KeyMetrics-table-container-3wVZN'})
                for div in div_table:
                    report_name = div.find_all(name='h3')[0].text
                    tr_list = div.find_all(name='tr')
                    for tr in tr_list:
                        metric = tr.find_all(name='th')[0].text
                        value = tr.find_all(name='td')[0].text

                        if len(value) == 0:
                            value = fields_date[metric]

                        ticker_values = {
                            'dataAtual':str(today),
                            'nomeAcao':ticker,
                            'fonte':'reuters',
                            'metrica':metric,
                            'valor':value,
                            'relatorio_financeiro':report_name
                            }
                        list_values.append(ticker_values)

        df = pd.DataFrame (list_values)
        return df        
