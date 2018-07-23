from flask_login import UserMixin
from abc import ABC, abstractmethod


class User(UserMixin, ABC):
    __id = -1

    def __init__(self, zid, email, username, password):
        self._id = self._generate_id()
        self._zid = zid
        self._email = email
        self._username = username
        self._password = password
        self._event_registered = []
        self._event_closed = []

    @property
    def zid(self):
        return self._zid

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        """Required by Flask-login"""
        return str(self._id)

    def _generate_id(self):
        User.__id += 1
        return User.__id

    def validate_password(self, password):
        return self._password == password
        
    @property
    def email(self):
        return self._email

    @abstractmethod
    def what_type(self):
        pass

    def get_event_registered(self):
        return self._event_registered

    def add_event_registered(self, event):
        self._event_registered.append(event)

    def del_event_registered(self, event):
        self._event_registered.remove(event)

    def get_event_closed(self):
        return self._event_closed

    def add_event_closed(self, event):
        self._event_closed.append(event)

class Student(User):

    def __init__(self, zid, email, username, password,):
        super().__init__(zid, email, username, password)

    def __str__(self):
        return self._username

    def what_type(self):
        return 'Student'


class Staff(User):

    def __init__(self, zid, email, username, password,):
        super().__init__(zid, email, username, password)
        self._event_posted = []
        self._event_cancelled = []

    def add_event_posted(self, event):
        self._event_posted.append(event)

    def del_event_posted(self, event):
        self._event_posted.remove(event)

    def get_event_posted(self):
        return self._event_posted

    def add_event_cancelled(self, event):
        self._event_cancelled.append(event)

    def del_event_cancelled(self, event):
        self._event_cancelled.remove(event)

    def get_event_cancelled(self):
        return self._event_cancelled

    def what_type(self):
        return 'Staff'

    def __str__(self):
        return self._username

class Guest(User):
    def __init__(self, email, username, password):
        super().__init__('0',email, username, password)

    def __str__(self):
        return self._username

    def what_type(self):
        return 'Guest'
