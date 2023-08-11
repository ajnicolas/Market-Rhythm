import numpy as np
import talib

class Indicators():
	"""
	Either use indicators provided by talib 
	or create your own 
	"""

	def __init__(self):
		pass

	def rsi(self, close_values, length=14):
		# Plug into rsi reversed to calc from old to new

		rsi_ar = talib.RSI(close_values, length)
		return np.around(rsi_ar, decimals=2)

	def ema(self,close_values, period=20):

		ema_ar = talib.EMA(close_values, timeperiod=period)
		return np.around(ema_ar, decimals=2)

	def macd(self,close_values, num=2, fp=12, sp=26, sigp=9):

		macd_arr = talib.MACD(close_values, fastperiod=fp, slowperiod=sp, signalperiod=sigp)
		return np.around(macd_arr[num], decimals=2)

	def bbandsUpper(self,close_values, num):

		bb_arr = talib.BBANDS(close_values, matype=MA_Type.T3)
		return np.around(bb_arr[num], decimals=2)