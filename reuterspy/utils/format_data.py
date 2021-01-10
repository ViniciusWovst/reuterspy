from datetime import date, datetime

def format_data(ticker, report_name, metric, ticker_values, yearly):
        list_values = []
        today = date.today()
        for periodo in ticker_values:
            date_periodo = datetime.strptime(periodo['date'], '%Y-%m-%d').date()
            year = date_periodo.year
            valor = periodo['value']

            ticker_values = {
                'dataAtual':str(today),
                'nomeAcao':ticker,
                'relatorioFinanceiro': report_name,
                'fonte':'reuters',
                'ano':year,
                'metrica':metric,
                'valor':valor
                }
            if not(yearly):
                trimestre = {'trimestre': (date_periodo.month-1)//3+1}
                ticker_values.update(trimestre)
            list_values.append(ticker_values)
        return list_values