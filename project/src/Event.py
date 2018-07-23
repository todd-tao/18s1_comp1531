from abc import ABC, abstractmethod
from src.Session import Session
from src.Exception import MessageError

from datetime import datetime, timedelta

class Event(ABC):
	__id = -1

	def __init__(self, name, early_time, start_time, end_time, max_num, location, convenor, fee, description):
		self._id = self._generate_id()
		self._num = 0
		self._name = name
		self._start_time = start_time
		self._end_time = end_time
		self._max = max_num
		self._attendee = []
		self._location = location
		self._status = "open"
		self._description = description
		self._convenor = convenor
		self._fee = fee
		self._early_time = early_time


	def get_id(self):
		return self._id

	def _generate_id(self):
		Event.__id += 1
		return Event.__id

	def get_num(self):
		return self._num

	@property
	def status(self):
		return self._status

	@property
	def early_time(self):
		return self._early_time
	@early_time.setter
	def early_time(self, time):
		self._early_time = time

	def is_discount(self):
		now = datetime.now()
		delta = self._early_time - now
		if delta.days > 0:
			return True
		else:
			return False

	#the status only have open, closed, cancelled
	@status.setter
	def status(self, new):
		self._status = new

	@property
	def fee(self):
		return self._fee
	
	@property
	def name(self):
		return self._name

	@property
	def start_time(self):
		return self._start_time

	@start_time.setter
	def start_time(self, start_time):
		self._start_time = start_time

	@property
	def end_time(self):
		return self._end_time

	@property
	def max(self):
		return self._max

	@property
	def location(self):
		return self._location

	@location.setter
	def location(self, location):
		self._location = location

	def capacity(self):
		if self._num >= self._max:
			return 'full'
		elif self._num <self._max:
			return self._num + '/'+ self._max

	def add_attendee(self, user):
		self._attendee.append(user)
		self._num += 1
		if self._num == self._max:
			self.status = "closed"

	def del_attendee(self, user):
		self._attendee.remove(user)
		self._num -= 1

	def get_attendee(self):
		return self._attendee

	def check_attendee(self, user):
		for c in self._attendee:
			if c.email == user.email:
				return True
		return False
	def check_convenor(self, user):
		if self._convenor.email == user.email:
			return True
		return False

	def can_cancell(self):
		now = datetime.now()
		delta = self._start_time - now
		if delta.days > 1:
			return True
		else:
			return False

	def __str__(self):
		return "Event {} posting: {} start from {} and end_time is {}, the fee of it is {}, this event have max number {} and the location is {}".format(self._id, self._name , self._start_time, self._end_time, self._fee, self._max, self._location)

	@property
	def description(self):
		return self._description

	@description.setter
	def description(self, description):
		self._description = description

	@abstractmethod
	def is_course(self):
		pass

	@property
	def convenor(self):
		return self._convenor

class Course(Event):
	def __init__(self, name, early_time, start_time, end_time, max_num, location, convenor, fee, description):
		super().__init__(name, early_time, start_time, end_time, max_num, location, convenor, fee, description)

	def is_course(self):
		return True


class Seminar(Event):
	def __init__(self, name, early_time, start_time, end_time, max_num, location, convenor, fee, description):
		super().__init__(name, early_time, start_time, end_time, max_num, location, convenor, fee, description)
		self._sessions = []

	def add_sessions(self, name, capacity, location, start_time, end_time):
		try:
			if len(name) == 0:
				raise MessageError('Please enter a valid name of this session.')

			date_format = "%Y-%m-%d"
			start_time = datetime.strptime(start_time, date_format)
			end_time = datetime.strptime(end_time, date_format)
			now = datetime.now()

			
			if not now < start_time:
				raise MessageError('Make start_time later than today')
			if not now < start_time or not start_time < end_time:
				raise MessageError('Please enter start_time, end_time in days order')
			if len(location) == 0:
				raise MessageError('Please enter a valid location name.')
		
		except ValueError as error:
			return "Enter time in Y-m-d format"
		except MessageError as error:
			return error

		try:
			capacity = int(capacity)

			if capacity< 1:
				raise MessageError('let capacity greater than 1')

		except ValueError as error:
			return "Enter an integer at capacity"
		except MessageError as error:
			return error
		session = Session(name, capacity, location, start_time, end_time)
		self._sessions.append(session)
		return session

	def get_sessions(self):
		return self._sessions

	def is_course(self):
		return False

	def get_session_by_id(self, session_id):
		for c in self._sessions:
			if str(c.get_id()) == session_id:
				return c
		return None
