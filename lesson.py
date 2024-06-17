import yfinance as yf
import pandas as pd


def read_csv():
    filename = 'nikkei.csv'
    df = pd.read_csv(filename, encoding='shift-jis')
    return df


def main():
    df_tickers = read_csv()
    df_tickers['コード'] =  df_tickers['コード'].astype(str) + '.T'

    for it_tuple in df_tickers.itertuples(name=None):
        stock = yf.Ticker(it_tuple[1])
        price = stock.history('1d')
        print(it_tuple[2] + " " +  str(price.iloc[0].at["Close"]))   #ハマりポイント：DF/Seriesの要素アクセス　行(iloc):連番 , 列(at):列名


if __name__ == "__main__":
    main()
