import configparser
import os

bools = ['True','False']
pairs = ["XBTUSD", "XBTJPY", "ADAM20", "BCHM20", "EOSM20", "ETHUSD", "LTCM20", "TRXM20", "XRPUSD", "XBTKRW"]
tf = ["1m", "5m", "1h", "1d"]

PROJECT_ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

# Parse configuration file

c = configparser.ConfigParser()
configFilePath = os.path.join(PROJECT_ROOT_DIR, 'config.cfg')

c.read(configFilePath)

class Config:

	# Check to see if testnet or live funds
	TEST_EXCHANGE = c.get('exchange', 'test_exchange')

	# See what timeframe we are trading / strat is using
	TIMEFRAME = c.get('exchange', 'timeframe')

	# Quatity we trading with(funds)
	QUANTITY = c.get('exchange', 'quantity')

	# Amount of leverage we are utilizing
	LEVERAGE = c.get('exchange', 'leverage')

	# What pair we are trading
	# CREATE A LIST OF ALL SYMBOLS AND CHECK IF VALID SYMBOL. IF NOT THEN ERROR
	SYMBOL = c.get('exchange', 'symbol')

	# API ID
	API_KEY = c.get('api_keys', 'api_key')

	# API Secret
	API_SECRET = c.get('api_keys', 'api_secret')

	def __init__(self):
		pass


	def validate_config(self):
		"""
		Check to validate user input from config file
		"""
		valid = True

		if self.TEST_EXCHANGE not in bools:
			print("Please enter True for testing in the testnet/exchange. False for real funds.")
			valid = False

		if self.TIMEFRAME not in tf:
			print("Please enter a correct timeframe [1m,5m,1h,1d]")
			valid = False

		# Could try float for now int
		try:
			value = int(self.QUANTITY)
		except ValueError:
			print("Please enter a integer(whole number)")
			valid = False # not a int

		if int(self.LEVERAGE) < 0:
			print("Please enter the leverage greater than or equal to 1")
			valid = False

		if self.SYMBOL not in pairs:
			print("Please enter a valid symbol pairing ex:XBTUSD")
			valid = False

		if not self.API_KEY:
			print("Please enter your api key to be able to use api")
			valid = False

		if not self.API_SECRET:
			print("Please enter your api secret to be able to use api")
			valid = False

		return valid


user_config = Config()


