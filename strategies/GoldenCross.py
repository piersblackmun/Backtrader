import math
import backtrader as bt

class GoldenCross(bt.Strategy):
    params = (('sma_50', 50), ('sma_200', 200), ('order_percentage', 0.95))

    def __init__(self):
        # Create 50 SMA
        self.sma_moving_average_50 = bt.indicators.SMA(
            self.data.close, period=self.params.sma_50, plotname='50 day moving average'
        )

        # Create 200 SMA
        self.sma_moving_average_200 = bt.indicators.SMA(
            self.data.close, period=self.params.sma_200, plotname='200 day moving average'
        )

        # Create crossover using the SMA's
        self.crossover = bt.indicators.CrossOver(self.sma_moving_average_50, self.sma_moving_average_200)

    def next(self):

        # Open trade
        if self.position.size == 0:
            if self.crossover > 0:
                amount_to_invest = (self.params.order_percentage * self.broker.cash)
                self.size = math.floor(amount_to_invest / self.data.close)

                print("Buy {} shares at {}".format(self.size, self.data.close[0]))
                self.buy(size=self.size)
        
        # Close trade
        if self.position.size > 0:
            if self.crossover < 0:      
                print("Sell {} shares at {}".format(self.size, self.data.close[0]))
                self.close()
