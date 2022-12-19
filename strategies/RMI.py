import math
import backtrader as bt

class RMI(bt.Strategy):
    
    params = (('upperband', 70.0), ('lowerband', 30.0), ('order_percentage', 0.95))

    def __init__(self):
        self.rmi = bt.indicators.RMI(self.data, period=20)

    def next(self):
        if not self.position and self.rmi < self.params.lowerband: 
           amount_to_invest = (self.params.order_percentage * self.broker.cash)
           self.size = math.floor(amount_to_invest / self.data.close)

           print("Buy {} shares at {}".format(self.size, self.data.close[0]))
           self.buy(size=self.size)

        if self.position and self.rmi > self.params.upperband:
                print("Sell {} shares at {}".format(self.size, self.data.close[0]))
                self.close()
