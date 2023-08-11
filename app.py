import json, sys
import numpy as np
from strategies import *
from sqldatabase import SqlDatabase
from settings import user_config
from websettings import Settings
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'random-password20' 

LENGTH = 28
NUM = 100

# start = "2019-09-18 17:00:00"
# end = "2020-06-16 05:00:00"

# strategy = "rsi_strategy"
symbol = user_config.SYMBOL
# timeframe = user_config.TIMEFRAME

# start, end = get_range("2019-09-18 17:00:00", "2020-06-16 05:00:00")

def get_data(start="", end="", timeframe="1h"):
	""" Returns raw data from database based on range and timeframe given """
	candles = SqlDatabase(symbol, timeframe, autoUpdate=False)

	price_data = np.array(candles.ohlcv_range("close", start, end)['close'].tolist())
	timestamp_data = candles.ohlcv_range("timestamp", start, end)['timestamp'].tolist()

	return price_data, timestamp_data


def get_first_last(start="", end="", timeframe="1h"):
	""" Returns raw data from database based on range and timeframe given """
	candles = SqlDatabase(symbol, timeframe, autoUpdate=False)

	price_data = np.array(candles.ohlcv_range("close", start, end)['close'].tolist())

	return price_data, timestamp_data


def str_to_class(classname):
	""" Converts name object to a class and returns it """
	return getattr(sys.modules[__name__], classname)

# rsi_data = backtest.rsi_data(length=28)[-NUM:]
# timestamp_data = backtest.timestamp_data()[-NUM:]


@app.route('/', methods=["GET", "POST"])
def main():
	"""
	Default page, shows both longs/shorts combined data.
	And a breakdown of longs/shorts for more detail.
	"""

	with open('./data/data.json', 'r') as f:
		data = json.load(f)

	start = data["backtest"]["start"]
	end = data["backtest"]["end"]
	timeframe = data["backtest"]["timeframe"]

	# Creates object of strategy inputted
	backtest = str_to_class(data["backtest"]["strategy"])
	# init object after created
	backtest = backtest(symbol, timeframe)

	# collects close data and timestamp
	close, timestamp = get_data(start=start, end=end, timeframe=timeframe)
	# calls strategy function inside the strategies class
	backtest_strat = backtest.strategy(close, timestamp)

	# print(backtest.get_symbol())
	# print(backtest.get_timeframe())
	# print("")
	# print(backtest.get_long_prices())
	# print(backtest.get_short_prices())


	strat = backtest.get_name()


	# longs data
	long_data = backtest.long_data()
	long_percentgains=long_data[4]
	long_tradesn=long_data[3]
	long_avgtrade=long_data[5]

	long_labels = backtest.long_time() #timestamps
	long_labels.insert(0,0) # Make chart begin from 0

	long_trades = long_data[0] # Trades
	long_trades.insert(0,0) # Make chart begin from 0

	long_pnl = long_data[1] # PNL overtime
	long_pnl.insert(0,0) # Make chart begin from 0


	# shorts data
	short_data = backtest.short_data()
	short_percentgains=short_data[4]
	short_tradesn=short_data[3]
	short_avgtrade=short_data[5]
	
	short_labels = backtest.short_time()
	short_labels.insert(0,0)

	short_trades = short_data[0] # Trades
	short_trades.insert(0,0)

	short_pnl = short_data[1] # PNL overtime
	short_pnl.insert(0,0)


	# long/short data
	trades = long_tradesn + short_tradesn
	gains = long_percentgains + short_percentgains
	try:
		avgtrade = gains/trades
	except ZeroDivisionError:
		avgtrade = 0

	# total_labels = combined_data[0]
	combined_data = backtest.combined_data()
	total_labels = combined_data[3]
	total_labels.insert(0,0)

	total_trades = combined_data[1]
	total_trades.insert(0,0)

	total_pnl = combined_data[2]
	total_pnl.insert(0,0)


	return render_template('index.html',
		title="Strategy Backtest",
		start=start,
		end=end,
		strat=strat,
		trades=trades,
		gains=gains,
		avgtrade=avgtrade,

		long_gains=long_percentgains,
		long_num_trades=long_tradesn,
		long_avgtrade=long_avgtrade,

		short_gains=short_percentgains,
		short_num_trades=short_tradesn,
		short_avgtrade=short_avgtrade,

		total_labels=total_labels,
		total_trades=total_trades,
		total_pnl=total_pnl,

		long_labels=long_labels,
		long_trades=long_trades,
		long_pnl=long_pnl,

		short_labels=short_labels,
		short_trades=short_trades,
		short_pnl=short_pnl
	)

@app.route('/settings', methods=["GET", "POST"])
def settings_panel():
	""" 
	Settings page to modify start, end, strategy, and timeframe. 
	Saved in data.json file
	"""
	form = Settings()

	if request.method == 'POST':

		# start = fist index in sql database (oldest)
		# end  = last index in sql database (newest)
		start = "2019-09-18 17:00:00"
		end = "2020-06-16 05:00:00"

		if request.form['start'] != "":
			start = request.form['start']

		if request.form['end'] != "":
			end = request.form['end']

		strategy = request.form['strategy']
		timeframe = request.form['timeframe']

		data = {}

		data['backtest'] = {'start': start,
							'end': end,
							'strategy': strategy,
							'timeframe': timeframe
							}

		with open('./data/data.json', 'w') as f:
			json.dump(data, f)

		return redirect(url_for('main'))

	return render_template('settings.html', form=form)

# @app.route('/longs', methods=["GET", "POST"])
# def longs():
# 	# longs data
# 	trades = long_total_trades
# 	gains = long_total_gains
# 	avgtrade = long_avg_gain

# 	long_labels = long_timestamps
# 	long_trades = long_tradegains
# 	long_pnl = long_gains

# 	winloss = longs_winloss

# 	return render_template('longs.html',
# 		title="Longs Backtest",
# 		trades=trades,
# 		gains=gains,
# 		avgtrade=avgtrade,

# 		long_labels=long_labels,
# 		long_trades=long_trades,
# 		long_pnl=long_pnl,
# 		winloss=winloss
# 	)


# @app.route('/shorts', methods=["GET", "POST"])
# def shorts():
# 	# shorts data
# 	trades = short_total_trades
# 	gains = short_total_gains
# 	avgtrade = short_avg_gain

# 	short_labels = short_timestamps
# 	short_trades = short_tradegains
# 	short_pnl = short_gains

# 	winloss = shorts_winloss

# 	return render_template('shorts.html',
# 		title="Shorts Backtest",
# 		trades=trades,
# 		gains=gains,
# 		avgtrade=avgtrade,

# 		short_labels=short_labels,
# 		short_trades=short_trades,
# 		short_pnl=short_pnl,
# 		winloss=winloss
# 	)


if __name__ == "__main__":
    app.run(debug=True)

