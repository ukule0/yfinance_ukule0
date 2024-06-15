import yfinance as yf
#import requests as req

#ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
#headers = {'User-Agent': ua}

#r=req.get("https://finance.yahoo.com/", headers=headers)
#r = req.get('https://blog.cosnomi.com', timeout=(60.0, 60.5), headers=headers)
#print(r.text)
msft = yf.Ticker("MSFT")

dv = msft.dividends

print(msft.dividends)
print(#test#)
