import math
import backtrader as bt

class Ichimoku(bt.Strategy):

    def __init__(self):

        self.ichimoku = bt.indicators.Ichimoku()
   
    def next(self):

         if not self.position and self.ichimoku.lines.senkou_span_a > self.ichimoku.lines.senkou_span_b: 
            amount_to_invest = (0.95 * self.broker.cash)
            self.size = math.floor(amount_to_invest / self.data.close)

            print("Buy {} shares at {}".format(self.size, self.data.close[0]))
            self.buy(size=self.size)

         if self.position and self.ichimoku.lines.senkou_span_a < self.ichimoku.lines.senkou_span_b:
            print("Sell {} shares at {}".format(self.size, self.data.close[0]))
            self.close()
