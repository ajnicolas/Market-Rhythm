import bitmex
import time
import sys
import datetime
from dateutil.tz import tzutc

from settings import user_config
from utils import truncate
from backtest import BackTest


if __name__ == '__main__':

	print("Welcome to ? v1! \n")

	if user_config.validate_config() == False:
		print("Invalid configuration, check 'config.cfg'. Exiting...")
		sys.stdout.flush()
		sys.exit(1) # Exit script

	print("Passed config!")


	backtest = BackTest(user_config.SYMBOL, user_config.TIMEFRAME)
	backtest.backtest_data()


