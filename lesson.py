import yfinance as yf
import pandas as pd


def read_csv():
    filename = 'nikkei.csv'
    df = pd.read_csv(filename, encoding='shift-jis')
    return df


def main():
    df_tickers = read_csv()

    filter = df_tickers["Market"] != "Tokyo"
    df2 = df_tickers['コード'].where(filter, df_tickers['コード'].astype(str) + '.T')
    df_tickers['コード'] = df2
# ハマリポイント : filterのTrue/Falseは感覚と逆
# ハマリポイント whereで取得された結果df_tickers['コード']は一旦別の変数df2に格納する
#    df_tickers['コード'] = df_tickers['コード'].where(df_tickers["Market"] == 'Nasdaq', df_tickers['コード'].astype(str) + '.T')
#    df_tickers['コード'] = df_tickers['コード'].astype(str) + '.T'

    for it_tuple in df_tickers.itertuples(name=None):
        stock = yf.Ticker(it_tuple[1])
        price = stock.history('7d')
        print(it_tuple[2] + " " +  str(price.iloc[0].at["Close"]))   #ハマりポイント：DF/Seriesの要素アクセス　行(iloc):連番 , 列(at):列名


if __name__ == "__main__":
    main()
