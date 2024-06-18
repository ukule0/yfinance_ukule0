import yfinance as yf
import pandas as pd


def read_csv():
    filename = 'nikkei.csv'
    df = pd.read_csv(filename, encoding='shift-jis')
    return df


def main():
    df = read_csv()
    df_tickers = to_jp_ticker_name(df)

    for it_tuple in df_tickers.itertuples(name=None):
        stock = yf.Ticker(it_tuple[2])
        price = stock.history('1d')
        print(it_tuple[3] + " " + str(round(price.iloc[0].at["Close"],2)))  #ハマりポイント：DF/Seriesの要素アクセス　行(iloc):連番 , 列(at):列名


def to_jp_ticker_name(df):
    filter = df["Market"] != "Tokyo"
    df_temp = df['コード'].where(filter, df['コード'].astype(str) + '.T')
    df['コード'] = df_temp
    # ハマリポイント : filterのTrue/Falseは感覚と逆
    # ハマリポイント df.whereで取得された結果df_tickers['コード']は一旦別の変数df2に格納する

    return df


if __name__ == "__main__":
    main()
