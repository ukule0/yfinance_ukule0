import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


def main():
    history_start_year = 1980
    ticker = get_ticker()
    ret = yf.Ticker(ticker).history(start=str(history_start_year) + '-04-01')
    stock_data = ret['Close']
    dividends_data = ret['Dividends']
    splits_data = ret['Stock Splits']

    calendar_year = 2023

    '[配当]配当金/年'
    year_dividends = get_dividends(calendar_year, dividends_data)
    '[株価]株価(Fiscal Year 3月末)'
    benchmark_price = get_benchmark_price(stock_data, calendar_year + 1)
    '[配当割合]配当金/株価(%)'
    dividends_per = year_dividends / benchmark_price * 100

    print("bench_price[" + str(calendar_year + 1) + "]:" + str(benchmark_price))
    print("dividend[" + str(calendar_year) + "]:" + str(dividends_per))


#    plt.figure()
#    year_dividends.plot()
#    plt.show()

def get_dividends(calendar_year, dividends_data):
    year_start = pd.to_datetime(str(calendar_year) + '-04-01', utc=True).tz_convert('Asia/Tokyo')
    year_end = pd.to_datetime(str(calendar_year + 1) + '-04-01', utc=True).tz_convert('Asia/Tokyo')
    each_dividends = dividends_data[(dividends_data.index >= year_start) & (dividends_data.index < year_end)]
    ret = each_dividends.sum()
    return ret


def get_benchmark_price(stock_data, calendar_year):
    year_start = pd.to_datetime(str(calendar_year) + '-03-24T00:00:00', utc=True).tz_convert('Asia/Tokyo')
    year_end = pd.to_datetime(str(calendar_year) + '-04-01T00:00:00', utc=True).tz_convert('Asia/Tokyo')
    yearend_stock = stock_data[(stock_data.index >= year_start) & (stock_data.index < year_end)].tail(1).iat[0]
    return yearend_stock


def get_ticker():
    #ticker = "^N225"
    #ticker = "2267.T" #ヤクルト
    ticker = "9434.T"  #ソフトバンク
    return ticker


if __name__ == "__main__":
    main()
