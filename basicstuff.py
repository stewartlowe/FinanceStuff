import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web

style.use('ggplot')

#st = dt.datetime.now() - dt.timedelta(days=5*365)
#ed = dt.datetime.now()

#df = web.DataReader('SCAM.L','yahoo',st,ed)

#df.to_csv('SCAM.csv')

df = pd.read_csv('EMHYY.csv',parse_dates=True,index_col=0)

print(df.head())
