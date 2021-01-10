from datetime import datetime

def format_data(ticker, report_name, metric, ticker_values, yearly):
        list_values = []
        for period in ticker_values:
            date_period = datetime.strptime(period['date'], '%Y-%m-%d').date()
            year = date_period.year
            value = period['value']
            ticker_values = {
                'ticker':ticker,
                'financialReport': report_name,
                'year':year,
                'metric':metric,
                'value':value
                }
            if not(yearly):
                quarter = {'quarter': (date_period.month-1)//3+1}
                ticker_values.update(quarter)
            
            list_values.append(ticker_values)
        return list_values