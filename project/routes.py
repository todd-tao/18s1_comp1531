from flask import render_template, request, redirect, url_for, abort
from flask_login import current_user, login_required, login_user, logout_user
from server import app, system
from datetime import datetime
from src.Event import Course, Seminar
from src.Event import Event
from utils import admin_required
from src.Session import Session
from src.User import Guest
from src.Exception import MessageError, RegisterError

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=["GET", "POST"])
def login():
	msg = ""
	if request.method == 'POST':
		if 'register' in request.form:
			return redirect(url_for('guest_register'))
		email = request.form["email"]
		password = request.form["password"]
		user = system.validate_login(email, password)
		if user is not None:
			login_user(user)
			return redirect(url_for('index'))
		else:
			msg = "Wrong user id or password! Please try again!"
	return render_template('login.html', message =msg)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404
    
@app.route('/new_event', methods=["GET", "POST"])
@login_required
@admin_required
def new():
	if request.method == 'POST':
		event_name = request.form['name']

		date_format = "%Y-%m-%d"
		start_time = request.form['start_time']
		end_time = request.form['end_time']
		early_time = request.form['early_time']
		fee = request.form['fee']
		location = request.form['location']
		description = request.form['description']
		max_num = request.form['max_numbers']


		type_event = request.form['type']
		user = system.get_user_by_id(current_user.get_id())
		event = system.add_event(event_name, early_time, start_time, end_time, max_num, location, user, fee, description, type_event)


		if not isinstance(event,Event):
			return render_template('new.html', message = event)

		user.add_event_posted(event)
		return render_template('event_create_confirm.html', event= event)
	return render_template('new.html')

@app.route('/event/<eid>', methods=["GET", "POST"])
@login_required
def event(eid):
	event = system.get_event_by_id(eid)
	user = system.get_user_by_id(current_user.get_id())
	if not event.is_course():
		sessions = event.get_sessions()
	fee = None
	if current_user.what_type() == 'Guest':
		if event.is_discount():
			fee = int(event.fee) * 0.5
		else:
			fee = event.fee

	if request.method == 'POST':
		if 'register' in request.form:

			mark = []
			if not event.is_course():	
				for c in sessions:
					checked = request.form.get(c.name)
					if checked:
						mark.append(c.name)
				message = system.register_event(eid, user, mark)

				if not isinstance(message, Event):
					return render_template('events.html',event = event, confirmation = False, fee = fee, error = message)
				return render_template('event_de_re_confirm.html', event = event, info = 'registered',fee = fee)
			else:
				message = system.register_event(eid, user, mark)

				if not isinstance(message, Event):
						return render_template('events.html',event = event, confirmation = False, fee = fee, error = message)
				return render_template('event_de_re_confirm.html', event = event, info = 'registered',fee = fee)


		if 'deregister' in request.form and event.can_cancell() and event.check_attendee(user):
			event.del_attendee(user)
			user.del_event_registered(event)
			if not event.is_course():
				for c in sessions:
					for f in c.get_attendee():
						if f.email == user.email:
							c.del_attendee(user)

			return render_template('event_de_re_confirm.html', event = event, info = 'de-registered')

		if 'cancel' in request.form and user.email == event.convenor.email:
			event.status = "cancelled"
			user.add_event_cancelled(event)
			user.del_event_posted(event)

			for c in event.get_attendee():
				c.add_event_closed(event)
				c.del_event_registered(event)
			return render_template('event_de_re_confirm.html', event = event, info = 'cancelled')

		if 'add_session' in request.form:
			if user.email == event.convenor.email:
				return render_template('events.html',event = event, confirmation = True)
			return render_template('events.html',event = event, error = 'Only convenor have the right to add sessions.')

		if 'submit' in request.form:
			session_name = request.form['name']
			location = request.form['location']
			start_time = request.form['start_time']
			end_time = request.form['end_time']
			capacity = request.form['capacity']

			message = event.add_sessions(session_name, capacity, location, start_time, end_time)
			if not isinstance(message, Session):
				return render_template('events.html',event = event, confirmation = True, fee = fee, error = message)

			return render_template('events.html',event = event, confirmation = False, error = 'New session created successfully')

	return render_template('events.html',event = event, confirmation = False, fee = fee)

@app.route('/index')
@login_required
def index():
	events_c = []
	events_s = []
	events = system.status_check("open")
	for c in events:
		if c.is_course():
			events_c.append(c)
		elif c.is_course() is False:
			events_s.append(c)
	return render_template('index.html', events_c = events_c, events_s = events_s)



@app.route('/dashboard')
@login_required
def dashboard():
	r_events = []
	p_events = []
	c_events = []
	user = system.get_user_by_id(current_user.get_id())

	r_events = user.get_event_registered()
	if user.what_type() == 'Staff':
		p_events = user.get_event_posted()
		c_events = user.get_event_cancelled()
	return render_template('dashboard.html', user = user)

@app.route('/guest_register', methods=["GET", "POST"])
def guest_register():
	if request.method == "POST":
		try:
			guest_email = request.form['email']
			guest_username = request.form['username']
			guest_password = request.form['password']
			

			if len(guest_email) == 0:
				raise MessageError('Please enter a valid email address')
			for c in system.get_user():
				if (c.email == guest_email):
					raise MessageError('This email is already registered')
			if len(guest_username) ==0:
				raise MessageError('Please enter a valid username')
			for c in system.get_user():
				if (c.username == guest_username):
					raise MessageError('This username is already used')
			if len(guest_password) == 0:
				raise MessageError('Please let password at least 1 digital')
		except MessageError as error:
			return render_template('g_r.html', message = error)
			
		guest = Guest(guest_email, guest_username, guest_password)
		system.add_user(guest)

		return render_template('g_r_confirm.html', guest = guest)
	return render_template('g_r.html')

@app.route('/event/<eid>/session/<sid>', methods=["GET", "POST"])
@login_required
def session(eid, sid):
	event = system.get_event_by_id(eid)
	session = event.get_session_by_id(sid)
	user = system.get_user_by_id(current_user.get_id())
	if request.method == "POST":
		if 'be_speaker' in request.form and current_user.what_type() != "Student" and not event.check_attendee(user):
			session.speaker = user
	return render_template('sessions.html', session = session)


