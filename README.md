# reuterspy
[![reuterpy](https://img.shields.io/pypi/dm/reuterspy?color=blue&label=installs)](README.md)
<h2 align="center">Financial Data Extraction from Reuters.com with Python</h2>

reuterspy is a Python package to retrieve data from [reuters.com](https://www.reuters.com/), which provides **Balance sheet, Cash Flow, Income Statement and Key Metrics**.

reuterspy allows the user to download both recent and historical data from all the financial products indexed at reuters.com

reuterspy seeks simple Python packages when it comes to financial data extraction in order to stop relying on public/private APIs, since reuterspy is **FREE** and has **NO LIMITATIONS**. 

## Installation

In order to get this package working you will need to **install it via pip** (with a Python3.5 version or higher) on the terminal by typing:

``$ pip install reuterspy``

## Usage


<h2 align="center">Income Statement</h2>

 <h3>What is an Income Statement?</h3>
 
An income statement is one of the three important financial statements used for reporting a company's financial performance over a specific accounting period, with the other two key statements being the balance sheet and the statement of cash flows.

Also known as the profit and loss statement or the statement of revenue and expense, the income statement primarily focuses on the company’s revenues and expenses during a particular period.

In the example presented below, the yearly income statement of an stock is retrieved.

```python
from reuterspy import Reuters

reuters = Reuters()

ticker_list = ['NFLX.O']
df = reuters.get_income_statement(ticker_list)

print(df.head())
```
```{r, engine='python', count_lines}
ticker   financialReport  year   metric         value
NFLX.O  income_statement  2019  Revenue  20156.447000
NFLX.O  income_statement  2018  Revenue  15794.341000
NFLX.O  income_statement  2017  Revenue  11692.713000
NFLX.O  income_statement  2016  Revenue   8830.669000
NFLX.O  income_statement  2015  Revenue   6779.511000
```

<h2 align="center">Balance Sheet</h2>

 <h3>What Is a Balance Sheet?</h3>
 
A balance sheet is a financial statement that reports a company's assets, liabilities and shareholders' equity at a specific point in time, and provides a basis for computing rates of return and evaluating its capital structure. It is a financial statement that provides a snapshot of what a company owns and owes, as well as the amount invested by shareholders.

The balance sheet is used alongside other important financial statements such as the income statement and statement of cash flows in conducting fundamental analysis or calculating financial ratios.

In the example presented below, the yearly Balance Sheet of an stock is retrieved.

```python
from reuterspy import Reuters

reuters = Reuters()

ticker_list = ['NFLX.O']
df = reuters.get_balance_sheet(ticker_list)

print(df.head())
```
```{r, engine='python', count_lines}
ticker financialReport  year              metric        value
NFLX.O   balance_sheet  2019                Cash  3103.525000
NFLX.O   balance_sheet  2018                Cash  2572.685000
NFLX.O   balance_sheet  2016                Cash  1264.126000
NFLX.O   balance_sheet  2015                Cash  1706.592000
NFLX.O   balance_sheet  2019  Cash & Equivalents  1914.912000
```

<h2 align="center">Cash Flow</h2>

 <h3>What Is a Cash Flow?</h3>
 
Cash flow is the net amount of cash and cash-equivalents being transferred into and out of a business. At the most fundamental level, a company’s ability to create value for shareholders is determined by its ability to generate positive cash flows, or more specifically, maximize long-term free cash flow (FCF).

In the example presented below, the yearly Cash Flow of an stock is retrieved.


```python
from reuterspy import Reuters

reuters = Reuters()

ticker_list = ['NFLX.O']
df = reuters.get_cash_flow(ticker_list)

print(df.head())
```
```{r, engine='python', count_lines}
ticker financialReport  year                    metric        value
NFLX.O       cash_flow  2019  Net Income/Starting Line  1866.916000
NFLX.O       cash_flow  2018  Net Income/Starting Line  1211.242000
NFLX.O       cash_flow  2017  Net Income/Starting Line   558.929000
NFLX.O       cash_flow  2016  Net Income/Starting Line   186.678000
NFLX.O       cash_flow  2015  Net Income/Starting Line   122.641000
```

<h2 align="center">Key Metrics</h2>

In the example presented below, the key metrics of an stock is retrieved.

```python
from reuterspy import Reuters

reuters = Reuters()

ticker_list = ['NFLX.O']
df = reuters.get_key_metrics(ticker_list)

print(df.head())
```
```{r, engine='python', count_lines}
ticker                         metric       value   financialReport
NFLX.O      Price closing or last bid      510.40  Price and Volume
NFLX.O                   52 Week High      575.37  Price and Volume
NFLX.O                    52 Week Low      290.25  Price and Volume
NFLX.O                   Pricing date  2021-01-08  Price and Volume
NFLX.O  10 Day Average Trading Volume        3.49  Price and Volume
```

## Disclaimer
This Python package has been made for research purposes in order to fit the needs that reuters.com does not cover, so this package works like an Application Programming Interface (API) of reuters.com developed in an altruistic way.

Conclude that this package is not related in any way with reuters.com or any dependant company, the only requirement specified by reuters.com in order to develop this package was "mention the source where data is retrieved from".
