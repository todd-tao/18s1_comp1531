from abc import ABC
class Session(ABC):
	__id = -1
	def __init__(self, name, capacity, location, start_time, end_time):
		self._id = self._generate_id()
		self._name = name
		self._speaker = 'empty'
		self._attendee = []
		self._capacity = capacity
		self._location = location
		self._start_time = start_time
		self._end_time = end_time
		self._num = 0

	def _generate_id(self):
		Session.__id += 1
		return Session.__id

	def get_id(self):
		return self._id

	@property
	def speaker(self):
		return self._speaker

	@speaker.setter
	def speaker(self, user):
		self._speaker = user 

	@property
	def name(self):
		return self._name

	@property
	def location(self):
		return self._location
	
	@property
	def num(self):
		return self._num

	@property
	def start_time(self):
		return self._start_time

	@property
	def end_time(self):
		return self._end_time
	
	@property
	def capacity(self):
		return self._capacity
	
	
	def add_attendee(self, user):
		self._attendee.append(user)
		self._num += 1

	def del_attendee(self, user):
		self._attendee.remove(user)
		self._num -= 1

	def get_attendee(self):
		return self._attendee

	def __str__(self):
		return "{} is speaked by {}".format(self._name, self._speaker)
