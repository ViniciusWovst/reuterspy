# Copyright 2020-2021 Vinicius Wovst, viniciuswovst @ GitHub
# See LICENSE for details.

import requests
from datetime import datetime

BASE_URL = 'https://www.reuters.com/companies/api'

def get_data(ticker, report_name, yearly=True):
    """
    This function gets company's financial reports from reuters api (https://www.reuters.com/companies/api/getFetchCompanyFinancials/[ticker]),
    these informations are `income statement, cash flow and balance sheet`.
    
    Args:
        ticker (:obj: `str`): symbol of the stock to retrieve its company's profile. 
        report_name (:obj: `str`):name of the financial report, can be: <income, cash_flow, balance_sheet>
        yearly (:obj: `bool`, optional [default True]: if True returns yearly report or False returns quarterly report.

    Returns:
        :obj:`json` - data:
            This function returns a :obj:`json`  containing recent data of the specific stock informed in `ticker` parameter.
    """
    url = '%s/getFetchCompanyFinancials/%s' % (BASE_URL, ticker)
    request = requests.get(url)
    result = {}
    if request.status_code == 200:
        content = request.json()
        market_data = content['market_data']
        market_data = market_data['financial_statements']
        income = market_data[report_name]
        if (yearly):
            result = income['annual']
        else:
            result = income['interim']

    return result
  
def get_fields_date(ticker):
    """
    This function gets value of date fields `Pricing date, 52 Week High Date and 52 Week Low Date` from reuters api (https://www.reuters.com/companies/api/getFetchCompanyKeyMetrics/[ticker]).    
    Args:
        ticker (:obj:`str`): symbol of the stock to retrieve its company's profile. 

    Returns:
        :obj:`json` - data:
            This function returns a :obj:`json` containing dates `Pricing date, 52 Week High Date and 52 Week Low Date`, the output will be::
            
            {
            Pricing date: yyyy-mm-ddTHH:MM:SS,
            52 Week High Date: yyyy-mm-ddTHH:MM:SS,
            52 Week Low Date: yyyy-mm-ddTHH:MM:SS
            }
    """
    fields_date = {}
    url = '%s/getFetchCompanyKeyMetrics/%s' % (BASE_URL, ticker)
    request = requests.get(url)
    DATE_MASK = '%Y-%m-%dT%H:%M:%S'
    if request.status_code == 200:
        content = request.json()['market_data']
        fields_date = {
            'Pricing date':datetime.strptime(content['price_date'], DATE_MASK).date(),
            '52 Week High Date':datetime.strptime(content['fiftytwo_week_high_date'], DATE_MASK).date(),
            '52 Week Low Date':datetime.strptime(content['fiftytwo_week_low_date'], DATE_MASK).date()
        }
    return fields_date