import math
import backtrader as bt

class MACD(bt.Strategy):

    params = (('ema_12', 12), ('ema_26', 26), ('order_percentage', 0.95))

    def __init__(self):     
        self.fast_ema_12 = bt.indicators.EMA(
            self.data.close, period = self.params.ema_12, plotname = '12 day EMA'
        )

        self.slow_ema_26 = bt.indicators.EMA(
            self.data.close, period = self.params.ema_26, plotname = '26 day EMA'
        )

        self.macd = bt.indicators.MACDHistogram(self.fast_ema_12, self.slow_ema_26)

    def next (self):
        if not self.position and self.macd > 0:
            amount_to_invest = (self.params.order_percentage * self.broker.cash)
            self.size = math.floor(amount_to_invest / self.data.close)

            print("Buy {} shares at {}".format(self.size, self.data.close[0]))
            self.buy(size=self.size)

        if self.position and self.macd < 0:
             print("Sell {} shares at {}".format(self.size, self.data.close[0]))
             self.close()
