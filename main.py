import datetime
import backtrader as bt
from strategies.BuyAndHold import BuyHold
from strategies.GoldenCross import GoldenCross
from strategies.BollingerBands import BollingerBands
from strategies.RSI import RSI
from strategies.SMA import SMA
from strategies.EMA import EMA
from strategies.MACD import MACD
from strategies.Aroon import Aroon
from strategies.Ichimoku import Ichimoku
from strategies.RMI import RMI

# Initiate instance
cerebro = bt.Cerebro()

# Set account margin
cerebro.broker.setcash(1000)
print (f'Starting Account Balance: {cerebro.broker.getvalue()}')

# Define and configure dataset 
data = bt.feeds.YahooFinanceCSVData(
           dataname='data/AAPL.csv',
           fromdate=datetime.datetime(2015, 1, 1),
           todate=datetime.datetime(2022, 1, 1)
           )


# Add data, strategy and trade analyzer
cerebro.adddata(data)
cerebro.addstrategy(RSI)
cerebro.addanalyzer(bt.analyzers.TradeAnalyzer,_name="Basic_stats")

#Run application
strats = cerebro.run()
strat = strats[0]

# Generate GUI and plot trades 
cerebro.plot()
print (f'Ending Account Balance: {cerebro.broker.getvalue()}')

# Print analysis of the trades 
for e in strat.analyzers:
    e.print()
