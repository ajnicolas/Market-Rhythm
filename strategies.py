from indicators import Indicators
from backtest import BackTest
from tradebitmex import TradeBitmex

# simple strategies to test backtesting engine 

class rsi_strategy(BackTest):
	"""
	Simple rsi strategy to test backtesting
	"""

	def __init__(self, symbol, timeframe):
		BackTest.__init__(self, symbol=symbol, timeframe=timeframe)

		# init indicators to be able to use all indicators if using them
		self.indicators = Indicators()


	def strategy(self, close, timestamp):
		"""
		Rsi strategy meant for 1h timeframe
		If rsi < 30 then open long
		If rsi > 70 Then open short
		"""

		# Set name for strategy
		self.set_name("rsi strategy")

		# Convert close data to rsi data
		rsi_data = self.indicators.rsi(close_values=close, length=28).tolist()
		print("Total candles loaded:", len(close)) # See how many candles are loading


		# For loop to backtest strategy 
		for i in range(len(close)):

			if rsi_data[i] < 30:
				self.long_entry(close[i], timestamp[i])

			elif rsi_data[i] > 70:
				self.short_entry(close[i], timestamp[i])

			else:
				continue



class EMA_strategy(BackTest):

	def __init__(self, symbol, timeframe):
		BackTest.__init__(self, symbol=symbol, timeframe=timeframe)

		self.indicators = Indicators()


	def strategy(self, close, timestamp):

		self.set_name("EMA")

		ema_12 = self.indicators.ema(close_values=close, period=12).tolist()
		ema_26 = self.indicators.ema(close_values=close, period=26).tolist()
		print("Total candles loaded:", len(close))

		for i in range(len(close)):

			if ema_12[i] > ema_26[i]:
				self.long_entry(close[i], timestamp[i])
			elif ema_12[i] < ema_26[i]:
				self.short_entry(close[i], timestamp[i])
			else:
				continue



