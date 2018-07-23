class BookingError(Exception):
	def __init__(self, name, message):
		self._name = name
		self._message = message

	def __str__(self):
		return "The error happen at {}, {}". format(self._name, self._message)