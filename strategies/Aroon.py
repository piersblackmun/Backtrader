import math
import backtrader as bt

class Aroon(bt.Strategy):

    params = (('upperband', 99), ('lowerband', -99), ('order_percentage', 0.95))

    def __init__(self):
        self.Aroon = bt.indicators.AroonOscillator(self.data, period=14)

    
    def next(self):
        if not self.position and self.Aroon < self.params.lowerband: 
           amount_to_invest = (self.params.order_percentage * self.broker.cash)
           self.size = math.floor(amount_to_invest / self.data.close)

           print("Buy {} shares  at {}".format(self.size, self.data.close[0]))
           self.buy(size=self.size)

        if self.position and self.Aroon > self.params.upperband:
                print("Sell {} shares  at {}".format(self.size, self.data.close[0]))
                self.close()
