import yfinance as yf
import pandas as pd


def read_csv():
    filename = 'nikkei.csv'
    df = pd.read_csv(filename, encoding='shift-jis')
    return df


def main():
    print("USDJPY:" + str(get_close_value("USDJPY=X")))

    'CSVの企業の株価を取得'
    df = read_csv()
    df_tickers = to_jp_ticker_name(df)
    for it_tuple in df_tickers.itertuples(name=None):
        print(it_tuple[3] + " " + str(get_close_value(it_tuple[2])))


def to_jp_ticker_name(df):
    filter = df["Market"] != "Tokyo"
    df_temp = df['コード'].where(filter, df['コード'].astype(str) + '.T')
    df['コード'] = df_temp
    # ハマリポイント : filterのTrue/Falseは感覚と逆
    # ハマリポイント df.whereで取得された結果df_tickers['コード']は一旦別の変数df2に格納する
    return df


def get_close_value(ticker):
    ret = yf.Ticker(ticker).history(period="1d")
    ret = ret.iloc[0].at["Close"]     # ハマりポイント：DF/Seriesの要素アクセス　行(iloc):連番 , 列(at):列名
    ret = round(ret, 2)
    return ret


if __name__ == "__main__":
    main()
