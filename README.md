# Market-Rhythm

Market Rhythm is a way to create and backtest strategies with a ui to display strategy performance. This is not trading software as it's more to backtest market strategies to find an edge in the market. For now, i've only added support for the crypto market such as BTC and ETH as those are the most liquid markets.

# How to get started
Clone project, then cd into folder

Creating a virtual environemnt
```bash
python3 -m venv env
```
Activating the environemnt
```bash
source env/bin/activate
```
 
Installing requirements.txt
```bash
pip install -r requirements.txt
```

With the libraries installed needed to run, we are set up. 
Will update the rest, as I need to implement more to make it more. For right now, you can download crypto data, create strategies, and backtest them by running in app.py (python3 app.py) 

# Future implementations
- Add implementation for AI models
- More exchcange data for different pairs
- Strategy deployment into x exchange written in c++
