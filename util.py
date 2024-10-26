import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


def main():
    ticker = "^N225"
    ticker = "2267.T" #ヤクルト
    ticker = "9434.T" #ソフトバンク
    ret = yf.Ticker(ticker).history(start="1980-01-01")
    stock_data = ret['Close']
    dividends_data = ret['Dividends']
#    Splits_data = ret['Stock Splits']

    year_start = pd.to_datetime('2023-01-01',utc=True).tz_convert('Asia/Tokyo')
    year_end = pd.to_datetime('2024-01-01',utc=True).tz_convert('Asia/Tokyo')
    year_dividends = dividends_data[(dividends_data.index >= year_start) & (dividends_data.index < year_end)]
    yearend_stock = stock_data[(stock_data.index >= year_start) & (stock_data.index < year_end)].tail(1).iat[0]

    #plt.figure()
    dividends_per = year_dividends.sum() / yearend_stock * 100
    print(dividends_per)
    year_dividends.plot()
    plt.show()


if __name__ == "__main__":
    main()

