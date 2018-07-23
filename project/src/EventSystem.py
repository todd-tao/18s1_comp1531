from .Event import Event
from src.Exception import MessageError
from datetime import datetime
from src.Event import Course, Seminar
class EventSystem:
	def __init__(self):
		self._user = []
		self._event = []

	def add_event(self,event_name, early_time, start_time, end_time, max_num, location, user, fee, description, type_event):
		try:

			if len(event_name) == 0:
				raise MessageError('Please enter a valid name of this event.')
				
			date_format = "%Y-%m-%d"
			early_time = datetime.strptime(early_time, date_format)
			start_time = datetime.strptime(start_time, date_format)
			end_time = datetime.strptime(end_time, date_format)
			now = datetime.now()

			
			if not now < early_time:
				raise MessageError('Make early_time later than today')
			if not now < early_time or not early_time < start_time or not start_time < end_time:
				raise MessageError('Please enter early_time, start_time, end_time in days order')
			if len(location) == 0:
				raise MessageError('Please enter a valid location name.')
			if len(description) == 0:
				raise MessageError('Please enter some description of this event.')
		
		except ValueError as error:
			return "Enter time in Y-m-d format"
		except MessageError as error:
			return error

		try:
			max_num = int(max_num)
			fee = int(fee)

			if max_num < 1:
				raise MessageError('let max_num greater than 1')
			if fee < 0:
				raise MessageError('Please give a positive fee')

		except ValueError as error:
			return "Enter an integer at max_num and fee"
		except MessageError as error:
			return error


		if type_event == "Course":
			event = Course(event_name, early_time, start_time, end_time, max_num, location, user, fee, description)
		elif type_event == "Seminar":
			event = Seminar(event_name, early_time, start_time, end_time, max_num, location, user, fee, description)

		self._event.append(event)
		return event

	def register_event(self, eid, user, mark):
		event = self.get_event_by_id(eid)
		try:
			if not event.is_course():
				for c in event.get_sessions():
					if c.speaker != 'empty':
						if c.speaker.email == user.email:
							raise MessageError('You can not register session which you are a speaker')
			if event.check_attendee(user):
				raise MessageError('You are already an attendee of this event')
			if len(mark) == 0 and not event.is_course():
				raise MessageError('You have to choose at least one seesion')
			if event.get_num() >= event.max:
				raise MessageError('This event is full now')
			if event.check_convenor(user):
				raise MessageError('Do not regiser the event which posted by yourself.')


		except MessageError as error:
			return error

		if not event.is_course():
			for c in event.get_sessions():
				if c.name in mark:
					c.add_attendee(user)

		event.add_attendee(user)
		if event not in user.get_event_registered():
			user.add_event_registered(event)

		return event

	def add_user(self, user):
		self._user.append(user)

	# to find different status of event
	def status_check(self, sp_status):
		event = []
		for c in self._event:
			if c.status == sp_status:
				event.append(c)
		return event

	# to find course event
	def event_course(self):
		event = []
		for c in self._event:
			if c.get_event().is_course():
				event.append(c)
		return event

	# to find seminar event
	def event_seminar(self):
		event = []
		for c in self._event:
			if c.get_event().is_course() == False:
				event.append(c)
		return event

	def validate_login(self, email, password):
		for c in self._user:
			if c.email == email and c.validate_password(password):
				return c
		return None

	def get_user_by_id(self, user_id):
		for c in self._user:
			if c.get_id() == user_id:
				return c
		return None

	def get_event_by_id(self, event_id):
		for c in self._event:
			if str(c.get_id()) == event_id:
				return c
		return None

	def get_user(self):
		return self._user