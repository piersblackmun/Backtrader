import math
import backtrader as bt

class BuyHold(bt.Strategy):

    def next(self):
        if self.position.size == 0:
            amount_to_invest = 0.95 * self.broker.getcash()
            size = math.floor(amount_to_invest / self.data)
            print("Buy {} shares at {}".format(size, self.data.close[0]))
            self.buy(size=size)
