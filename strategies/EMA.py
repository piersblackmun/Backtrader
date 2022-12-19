import math
import backtrader as bt

class EMA(bt.Strategy):

    def __init__(self):
        self.ema = bt.indicators.EMA()

    def next(self):
        if not self.position and self.data > self.ema.lines.ema: 
           amount_to_invest = (0.95 * self.broker.cash)
           self.size = math.floor(amount_to_invest / self.data.close)

           print("Buy {} shares at {}".format(self.size, self.data.close[0]))
           self.buy(size=self.size)

        if self.position and self.data < self.ema.lines.ema:
                print("Sell {} shares at {}".format(self.size, self.data.close[0]))
                self.close()
