import yfinance as yf

msft = yf.Ticker("MSFT")

dv = msft.dividends

print(msft.dividends)

