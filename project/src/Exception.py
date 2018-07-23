class MessageError(Exception):
	def __init__(self, message):
		self._message = message

	@property
	def message(self):
		return self._message
	
	def __str__(self):
		return self._message


class RegisterError(Exception):
	"""docstring for RegisterRoor"""
	def __init__(self, name, message):
		self._name = name
		self._message = message

	def __str__(self):
		return "There is error exit, it is at {}, {}".format(self._name, self._message)
		