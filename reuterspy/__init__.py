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
    """
    This class is used to get recent data of informed stocks from reuters.com.
    """
    def get_income_statement(self, ticker_list, yearly=True):
        """
        This function gets income statement report

        Args:
            ticker_list (`list`): symbol's list of the stocks to retrieve its company profile.
            yearly (`bool`): if True return yearly report, if False return quarterly report.

        Returns:
            :obj:`pandas.DataFrame`:
                This function returns a :obj:`pandas.DataFrame` , 
                if yearly The dataset contains the ticker, financialReport, year, metric and value.
                if quarterly The dataset contains the ticker, financialReport, year, metric, value and quarter.
                
                if yearly the output will be::

                    ticker || financialReport | year | metric | value 
                    -------||-----------------|------|--------|-------
                    xxxxxx || xxxxxxxxxxxxxxx | xxxx | xxxxxx | xxxxx

                but if quarterly, then the output will be::

                    ticker || financialReport | year | metric | value | quarter 
                    -------||-----------------|------|--------|-------|---------
                    xxxxxx || xxxxxxxxxxxxxxx | xxxx | xxxxxx | xxxxx | xxxxxxx
        """
        list_values = []
        for ticker in ticker_list:
            income = get_data(ticker, 'income', yearly)
            metrics = income.keys()

            for item in metrics:
                metric = item
                periods = income[item]
                list_values = list_values+format_data(ticker, 'income_statement', metric, periods, yearly)
        df = pd.DataFrame (list_values)
        return df

    def get_cash_flow(self, ticker_list, yearly=True):
        """
        This function gets cash flow report

        Args:
            ticker_list (`list`): symbol's list of the stocks to retrieve its company profile.
            yearly (`bool`): if True return yearly report, if False return quarterly report.

        Returns:
            :obj:`pandas.DataFrame`:
                This function returns a :obj:`pandas.DataFrame` , 
                if yearly The dataset contains the ticker, financialReport, year, metric and value.
                if quarterly The dataset contains the ticker, financialReport, year, metric, value and quarter.
                
                if yearly the output will be::

                    ticker || financialReport | year | metric | value 
                    -------||-----------------|------|--------|-------
                    xxxxxx || xxxxxxxxxxxxxxx | xxxx | xxxxxx | xxxxx

                but if quarterly, then the output will be::

                    ticker || financialReport | year | metric | value | quarter 
                    -------||-----------------|------|--------|-------|---------
                    xxxxxx || xxxxxxxxxxxxxxx | xxxx | xxxxxx | xxxxx | xxxxxxx
        """
        list_values = []
        for ticker in ticker_list:
            cash_flow = get_data(ticker, 'cash_flow', yearly)
            metrics = cash_flow.keys()

            for item in metrics:
                metric = item
                periods = cash_flow[item]
                list_values = list_values+format_data(ticker, 'cash_flow', metric, periods, yearly)
        df = pd.DataFrame (list_values)
        return df

    def get_balance_sheet(self, ticker_list, yearly=True):
        """
        This function gets balance sheet report

        Args:
            ticker_list (`list`): symbol's list of the stocks to retrieve its company profile.
            yearly (`bool`): if True return yearly report, if False return quarterly report.

        Returns:
            :obj:`pandas.DataFrame`:
                This function returns a :obj:`pandas.DataFrame` , 
                if yearly The dataset contains the ticker, financialReport, year, metric and value.
                if quarterly The dataset contains the ticker, financialReport, year, metric, value and quarter.
                
                if yearly the output will be::

                    ticker || financialReport | year | metric | value 
                    -------||-----------------|------|--------|-------
                    xxxxxx || xxxxxxxxxxxxxxx | xxxx | xxxxxx | xxxxx

                but if quarterly, then the output will be::

                    ticker || financialReport | year | metric | value | quarter 
                    -------||-----------------|------|--------|-------|---------
                    xxxxxx || xxxxxxxxxxxxxxx | xxxx | xxxxxx | xxxxx | xxxxxxx
        """
        list_values = []
        for ticker in ticker_list:
            income = get_data(ticker, 'balance_sheet', yearly)
            metrics = income.keys()

            for item in metrics:
                metric = item
                periods = income[item]
                list_values = list_values+format_data(ticker, 'balance_sheet', metric, periods, yearly)
        df = pd.DataFrame (list_values)
        return df

    def get_key_metrics(self, ticker_list):
        """
        This function gets key metrics report

        Args:
            ticker_list (`list`): symbol's list of the stocks to retrieve its company profile.
            yearly (`bool`): if True return yearly report, if False return quarterly report.

        Returns:
            :obj:`pandas.DataFrame`:
                This function returns a :obj:`pandas.DataFrame` , 
                if yearly The dataset contains the ticker, financialReport, year, metric and value.
                if quarterly The dataset contains the ticker, financialReport, year, metric, value and quarter.
                
                if yearly the output will be::
                    
                    ticker || financialReport | year | metric | value 
                    -------||-----------------|------|--------|-------
                    xxxxxx || xxxxxxxxxxxxxxx | xxxx | xxxxxx | xxxxx

                but if quarterly, then the output will be::

                    ticker || financialReport | year | metric | value | quarter 
                    -------||-----------------|------|--------|-------|---------
                    xxxxxx || xxxxxxxxxxxxxxx | xxxx | xxxxxx | xxxxx | xxxxxxx
        """
        today = date.today()
        list_values = []
        for ticker in ticker_list:
            req = requests.get('https://www.reuters.com/companies/%s/key-metrics'% ticker)

            if req.status_code == 200:
                fields_date = get_fields_date(ticker)
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
                            'ticker':ticker,
                            'metric':metric,
                            'value':value,
                            'financialReport':report_name
                            }
                        list_values.append(ticker_values)

        df = pd.DataFrame (list_values)
        return df        
