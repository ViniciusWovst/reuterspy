# Copyright 2020-2021 Vinicius Wovst, viniciuswovst @ GitHub
# See LICENSE for details.

import requests
from datetime import datetime

BASE_URL = 'https://www.reuters.com/companies/api'

def get_data(ticker, report_name, yearly=True):
    url = '%s/getFetchCompanyFinancials/%s' % (BASE_URL, ticker)
    req = requests.get(url)
    result = {}
    if req.status_code == 200:
        content = req.json()
        market_data = content['market_data']
        market_data = market_data['financial_statements']
        income = market_data[report_name]
        if (yearly):
            result = income['annual']
        else:
            result = income['interim']

    return result
  
def get_fields_date(ticker):
        fields_date = {}
        url = '%s/getFetchCompanyKeyMetrics/%s' % (BASE_URL, ticker)
        req_ws = requests.get(url)
        DATE_MASK = '%Y-%m-%dT%H:%M:%S'
        if req_ws.status_code == 200:
            content_ws = req_ws.json()['market_data']
            fields_date = {
                'Pricing date':datetime.strptime(content_ws['price_date'], DATE_MASK).date(),
                '52 Week High Date':datetime.strptime(content_ws['fiftytwo_week_high_date'], DATE_MASK).date(),
                '52 Week Low Date':datetime.strptime(content_ws['fiftytwo_week_low_date'], DATE_MASK).date()
            }
        return fields_date