import pytest
from flask import Flask
from flask_login import LoginManager
from datetime import datetime
from flask import render_template, request, redirect, url_for, abort
from flask_login import current_user, login_required, login_user, logout_user
from src.Location import Location
from src.Car import Car, PremiumCar
from src.CarRentalSystem import CarRentalSystem
from src.Customer import Customer



# app = Flask(__name__)
# app.secret_key = 'very-secret-123'  # Used to add entropy
system = CarRentalSystem()

# # Login manager stuff
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'


# @login_manager.user_loader
# def load_user(user_id):
#     return system.get_user_by_id(user_id)

def test_1():


	user_name = "Matt"
	password = "pass"
	system.new_customer(Customer(user_name, password, 1531))
	user = system.validate_login(user_name, password)
	#login_user(user)
	assert user != None

	car_name = "Tesla"
	car_model = "model x"
	rego = 0
	system.add_car(PremiumCar(car_name, car_model, str(rego)))
	car = system.get_car(str(rego))
	assert car.get_name() == car_name
	assert car.get_model() == car_model


	location = Location("Sydney", "Mel")
	assert location

	date_format = "%Y-%m-%d"
	start_time = datetime.strptime("2018-11-11", date_format)
	end_time = datetime.strptime("2018-12-12", date_format)

	diff = end_time - start_time

	booking = system.make_booking(current_user, diff, car, location)
	assert booking._period == diff
	assert booking._car == car
	assert booking.location == location
	assert car.get_bookings()[0]
	assert system._bookings[0]
