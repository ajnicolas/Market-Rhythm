"""
Settings webpage 
What strategy to backtest
Time range (Year, Month, Day(optional), hour(optional))
What currency to backtest on (Download data if file not found)
What timeframe to choose to backtest

"""
import strategies
import inspect
from settings import user_config
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import Length

# app= Flask(__name__)
# app.config['SECRET_KEY'] = 'Nobody-will-guess12'

class Settings(FlaskForm):
	""" Creates form for settings page"""

	def get_classes():
		return [m[0] for m in inspect.getmembers(strategies, inspect.isclass) if m[1].__module__ == 'strategies']

	start = StringField('Start', validators=[Length(min=9, max=19)])
	end = StringField('End', validators=[Length(min=9, max=19)])

	strategy = SelectField('Strategy', choices=get_classes())
	timeframe = SelectField('Timeframe', choices=['1h', '1d'])

