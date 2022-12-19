import math
import backtrader as bt

class BollingerBands(bt.Strategy):

    def __init__(self):
 
        self.bollinger_bands = bt.indicators.BollingerBands();
    
    def next(self):

        if not self.position and self.data < self.bollinger_bands.lines.bot: 
            amount_to_invest = (0.95 * self.broker.cash)
            self.size = math.floor(amount_to_invest / self.data.close)

            print("Buy {} shares at {}".format(self.size, self.data.close[0]))
            self.buy(size=self.size)

        if self.position and self.data > self.bollinger_bands.lines.top:
            print("Sell {} shares at {}".format(self.size, self.data.close[0]))
            self.close()
