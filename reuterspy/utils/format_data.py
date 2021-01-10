# Copyright 2020-2021 Vinicius Wovst, viniciuswovst @ GitHub
# See LICENSE for details.

from datetime import datetime

def format_data(ticker, report_name, metric, ticker_values, yearly):
    """
    This function format data for defined format
    
    Args:
        ticker (:obj: `str`): symbol of the stock to retrieve its company profile. 
        report_name (:obj: `str`): name of the financial report, can be: <income_statement, cash_flow, balance_sheet>.
        metric (:obj: `str`): metric description  of the financial report.
        yearly (:obj: `bool`): if True return yearly report, if False return quarterly report.

    Returns:
        :obj:`json` - data:
            This function returns a :obj:`json`  containing formatted data, the output will be::
            
            {
            ticker: x,
            financialReport: x,
            year: yyyy,
            metric: x,
            value: x
            }
    """
    list_values = []
    for period in ticker_values:
        date_period = datetime.strptime(period['date'], '%Y-%m-%d').date()
        year = date_period.year
        value = period['value']
        ticker_value = {
            'ticker':ticker,
            'financialReport': report_name,
            'year':year,
            'metric':metric,
            'value':value
            }
        if not(yearly):
            quarter = {'quarter': (date_period.month-1)//3+1}
            ticker_value.update(quarter)
        
        list_values.append(ticker_value)
    return list_values