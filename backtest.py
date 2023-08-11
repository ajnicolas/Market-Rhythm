import numpy as np
from utils import dhm, percentage_decrease, percentage_increase, Merge

class BackTest():
	"""
	Backtest strategies 
	"""

	def __init__(self, symbol, timeframe):

		self.symbol = symbol

		self.timeframe = timeframe

		self.long_prices = []
		self.short_prices = []

		self.long_timestamps = []
		self.short_timestamps = []

		# Strategy uses this to see if positions are open
		self.long_pos = False
		self.short_pos = False

		self.strategy_name = ""


	def get_symbol(self):
		""" Returns symbol eg. XBTUSD, ETHUSD """
		return self.symbol

	def get_timeframe(self):
		""" Returns timeframe backtesting """
		return self.timeframe


	def get_long_prices(self):
		""" Returns a list of prices where it opened/closed a long """
		return self.long_prices

	def get_long_ts(self):
		""" Returns a list of timestamps where it opened/closed a long """
		return self.long_timestamps


	def get_short_prices(self):
		""" Returns a list of prices where it opened/closed a short """
		return self.short_prices

	def get_short_ts(self):
		""" Returns a list of timestamps where it opened/closed a short """
		return self.short_timestamps


	def set_name(self, name):
		""" Sets a name for the strategy """
		self.strategy_name = name

	def get_name(self):
		""" Returns the name set of the strategy """
		return self.strategy_name



	def long_entry(self, close, timestamp):
		""" 
		Opens a long position if it's not already in a long position. 
		Closes any open short position to be able to open a long position.
		"""

		if self.long_pos != True:
			if self.short_pos == True:
				# Closes short if open
				self.short_pos = False
				self.short_prices.append(close)
				self.short_timestamps.append(timestamp)

			# Opens long
			self.long_pos = True
			self.long_prices.append(close)
			self.long_timestamps.append(timestamp)
		else:
			return


	def short_entry(self, close, timestamp):
		""" 
		Opens a short position if it's not already in a short position. 
		Closes any open long position to be able to open a short position.
		"""

		if self.short_pos != True:
			if self.long_pos == True:
				# Closes long if open
				self.long_pos = False
				self.long_prices.append(close)
				self.long_timestamps.append(timestamp)

			# Opens short
			self.short_pos = True
			self.short_prices.append(close)
			self.short_timestamps.append(timestamp)
		else:
			return


	def short_data(self):
		"""
		Calculates gain of a trade (list)(float)
		Calculates pnl overtime (list)(float)
		Calculates winloss ratio (list)(int)
		Calculates total totaltrades (int)
		Calculates total gain (float)
		Calculates average gain(float)
		"""
		gains = []
		won = []
		loss = []
		winloss = []

		temp = 0
		pnl = []

		total_trades = 0
		total_gains = 0
		avg_gain = 0

		try:
			for i in range(0,len(self.short_prices), 2):
				gain = percentage_decrease(self.short_prices[i], self.short_prices[i+1])
				gains.append(gain)
				temp += gain
				pnl.append(temp)
				# total += gain
				# total_trades += 1
		except IndexError:
			pass

		for i in gains:
			if i > 0:
				won.append(i)
			else:
				loss.append(i)

		winloss.append(len(won))
		winloss.append(len(loss))

		total_trades = sum(winloss)
		total_gains = round(sum(gains),3)
		try:
			avg_gain = round(total_gains / total_trades, 3)
		except ZeroDivisionError:
			avg_gain = 0

		return gains, pnl, winloss, total_trades, total_gains, avg_gain


	def long_data(self):
		"""
		Calculates gain of a trade (list)(float)
		Calculates pnl overtime i-1 (list)(float)
		Calculates winloss ratio (list)(int)
		Calculates total totaltrades (int)
		Calculates total gain (float)
		Calculates average gain(float)
		"""
		gains = []
		won = []
		loss = []
		winloss = []

		temp = 0
		pnl = []

		total_trades = 0
		total_gains = 0
		avg_gain = 0

		try:
			for i in range(0,len(self.long_prices), 2):
				gain = percentage_increase(self.long_prices[i], self.long_prices[i+1])
				gains.append(gain)
				temp += gain
				pnl.append(temp)
		except IndexError:
			pass

		for i in gains:
			if i > 0:
				won.append(i)
			else:
				loss.append(i)

		winloss.append(len(won))
		winloss.append(len(loss))

		total_trades = sum(winloss)
		total_gains = round(sum(gains),3)

		try:
			avg_gain = round(total_gains / total_trades, 3)
		except ZeroDivisionError:
			avg_gain = 0


		return gains, pnl, winloss, total_trades, total_gains, avg_gain


	def short_time(self):
		""" grabs timestamp when trade ended, grabs by odd index """

		return self.short_timestamps[1::2]


	def long_time(self):
		""" grabs timestamp when trade ended, grabs by odd index """

		return self.long_timestamps[1::2]



	def combined_data(self):
		"""
		Returns combined data in order from timestamps
		combined_timestamp (list)(timestamp datatype)
		combined_trades (list)(float)
		combined_pnl (list)(float)
		"""
		long_timestamp = self.long_time()
		long_gains = self.long_data()[0]

		short_timestamp = self.short_time()
		short_gains = self.short_data()[0]

		combined_timestamp = []
		combined_trades = []

		long_dic = dict(zip(long_timestamp, long_gains))
		short_dic = dict(zip(short_timestamp, short_gains))
		combined_data = Merge(long_dic, short_dic) # Merge both dictinaries

		for key in sorted(combined_data.keys()):
			combined_timestamp.append(key)
			combined_trades.append(combined_data[key])

		temp = 0
		combined_pnl = []

		for i in combined_trades:
			temp += i
			combined_pnl.append(temp)

		trades_list = []
		for i in range(len(combined_timestamp)):
			trades_list.append(i+1)

		return combined_timestamp, combined_trades, combined_pnl, trades_list




# backtest = BackTest("XBTUSD", "1h")
# print(backtest.rsi_strategy())
