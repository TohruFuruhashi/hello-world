import pandas_datareader.data as pdr
import mplfinance as mpf

def getStockPrice(code):
  df = pdr.DataReader("{}.JP".format(code), "stooq").sort_index()
  return df

df = getStockPrice(8604).tail(100)
mpf.plot(df, type='candle', volume=True, savefig='8604_JP.png')
