import yfinance as yf
import pandas as pd


def read_csv():
    filename = 'nikkei.csv'
    df = pd.read_csv(filename, encoding='shift-jis')
    return df


def main():
    df_tickers = read_csv()
    df_tickers['コード'] =  df_tickers['コード'].astype(str) + '.T'

    for ticker in df_tickers['コード']:
        st_jp = yf.Ticker(ticker)
        price = st_jp.history('1d')
        print(price['Close'])

    for it_tuple in df_tickers.itertuples(name=None):
        str_ticker = it_tuple[1]
        st_jp = yf.Ticker(str_ticker)
        price = st_jp.history('1d')['Close'][0,1]
        it_tuple[3] = price
        print(it_tuple[1] + " " + str(it_tuple[3]))



if __name__ == "__main__":
    main()
