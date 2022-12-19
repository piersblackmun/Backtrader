import math
import backtrader as bt

class RSI(bt.Strategy):
    
    params = (('upperband', 85), ('lowerband', 25), ('order_percentage', 0.95))

    def __init__(self):
        self.rsi = bt.indicators.RSI(self.data, period=14)

    def next(self):
        if not self.position and self.rsi < self.params.lowerband: 
           amount_to_invest = (self.params.order_percentage * self.broker.cash)
           self.size = math.floor(amount_to_invest / self.data.close)

           print("Buy {} shares at {}".format(self.size,self.data.close[0]))
           self.buy(size=self.size)

        if self.position and self.rsi > self.params.upperband:
                print("Sell {} shares at {}".format(self.size, self.data.close[0]))
                self.close()
