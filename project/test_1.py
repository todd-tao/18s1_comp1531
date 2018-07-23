import pytest
from datetime import datetime
from src.Event import Course, Seminar
from src.Event import Event
from src.Session import Session
from src.User import Guest, Student, Staff
from src.EventSystem import EventSystem
from src.Exception import MessageError
system = EventSystem()

event_name = 'COMP1531'
early_time = '2018-9-10'
start_time = '2018-10-10'
end_time = '2018-11-10'
max_num = 20
location = 'UNSW'
user1 = Staff('4119991','z4119991@unsw.net','name4119991','pass29938')
fee = 30
description = "Join us"
type_event = 'Seminar'
user2 = Student('6119988','z6119988@unsw.net','name6119988','pass6890')
user3 = Guest('1','1','1')

session_name = 'Fake'
s_time = '2018-10-11'
e_time = '2018-10-20'
capacity = 10
session_location = 'Mel'
mark = ['Fake']

def test_create():

	event = system.add_event(event_name, early_time, start_time, end_time, max_num, location, user1, fee, description, type_event)
	assert isinstance(event, Event)

def test_create_no_event_name():

	event = system.add_event('', early_time, start_time, end_time, max_num, location, user1, fee, description, type_event)
	assert event.message == 'Please enter a valid name of this event.'

def test_create_no_early_time():

	event = system.add_event(event_name, '', start_time, end_time, max_num, location, user1, fee, description, type_event)
	assert event == "Enter time in Y-m-d format"

def test_create_no_start_time():

	event = system.add_event(event_name, early_time, '', end_time, max_num, location, user1, fee, description, type_event)
	assert event == "Enter time in Y-m-d format"

def test_create_no_end_time():

	event = system.add_event(event_name, early_time, start_time, '', max_num, location, user1, fee, description, type_event)
	assert event == "Enter time in Y-m-d format"

def test_create_not_int_max_num():

	event = system.add_event(event_name, early_time, start_time, end_time, 'abc', location, user1, fee, description, type_event)
	assert event == "Enter an integer at max_num and fee"

def test_create_negative_max_num():

	event = system.add_event(event_name, early_time, start_time, end_time, '-1', location, user1, fee, description, type_event)
	assert event.message == 'let max_num greater than 1'

def test_create_no_location():

	event = system.add_event(event_name, early_time, start_time, end_time, max_num, '', user1, fee, description, type_event)
	assert event.message == 'Please enter a valid location name.'

def test_create_not_int_fee():

	event = system.add_event(event_name, early_time, start_time, end_time, max_num, location, user1, 'abc', description, type_event)
	assert event == "Enter an integer at max_num and fee"

def test_create_negative_fee():

	event = system.add_event(event_name, early_time, start_time, end_time, max_num, location, user1, '-1', description, type_event)
	assert event.message == 'Please give a positive fee'

def test_create_no_description():

	event = system.add_event(event_name, early_time, start_time, end_time, max_num, location, user1, fee, '', type_event)
	assert event.message == 'Please enter some description of this event.'

def test_create_start_before_early():

	event = system.add_event(event_name, '2018-11-1', start_time, end_time, max_num, location, user1, fee, description, type_event)
	assert event.message == 'Please enter early_time, start_time, end_time in days order'

def test_create_early_time_before_today():

	event = system.add_event(event_name, '2018-5-10', start_time, end_time, max_num, location, user1, fee, description, type_event)
	assert event.message == 'Make early_time later than today'

def test_create_end_before_start():

	event = system.add_event(event_name, early_time, start_time, '2018-10-1', max_num, location, user1, fee, description, type_event)
	assert event.message == 'Please enter early_time, start_time, end_time in days order'



event = system.add_event(event_name, early_time, start_time, end_time, max_num, location, user1, fee, description, type_event)
assert isinstance(event, Event)
session = event.add_sessions(session_name, capacity, session_location, s_time, e_time)
assert isinstance(session, Session)
eid = event.get_id()


def test_create_session():
	session = event.add_sessions(session_name, capacity, session_location, s_time, e_time)
	assert isinstance(session, Session)

def test_create_session_no_name():
	session = event.add_sessions('', capacity, session_location, s_time, e_time)
	assert session.message == 'Please enter a valid name of this session.'

def test_create_session_not_int_cap():
	session = event.add_sessions(session_name, 'abc', session_location, s_time, e_time)
	assert session =="Enter an integer at capacity"

def test_create_session_negative_cap():
	session = event.add_sessions(session_name, '-1', session_location, s_time, e_time)
	assert session.message == 'let capacity greater than 1'

def test_create_session_no_location():
	session = event.add_sessions(session_name, capacity, '', s_time, e_time)
	assert session.message == 'Please enter a valid location name.'

def test_create_session_start_before_today():
	session = event.add_sessions(session_name, capacity, session_location, '2018-5-10', e_time)
	assert session.message == 'Make start_time later than today'

def test_create_session_end_before_start():
	session = event.add_sessions(session_name, capacity, session_location, e_time, s_time)
	assert session.message == 'Please enter start_time, end_time in days order'

def test_register():
	message = system.register_event(str(eid), user2, mark)
	assert isinstance(message, Event)


def test_register_already_attendee():
	message = system.register_event(str(eid), user2,mark)
	assert message.message == 'You are already an attendee of this event'

def test_register_no_session():
	message = system.register_event(str(eid), user3,[])
	assert message.message == 'You have to choose at least one seesion'

def test_register_be_speaker():
	session.speaker = user3
	assert not isinstance(session.speaker, str)

def test_register_already_speaker():
	message = system.register_event(str(eid), user3, mark)
	assert message.message == 'You can not register session which you are a speaker'


def test_register_event_full():
	event = system.add_event(event_name, early_time, start_time, end_time, '1', location, user1, fee, description, type_event)
	session = event.add_sessions(session_name, capacity, session_location, s_time, e_time)
	assert isinstance(session, Session)
	session.speaker = user1
	eid = event.get_id()
	message = system.register_event(str(eid), user2,mark)
	assert isinstance(message, Event)
	message = system.register_event(str(eid), user3,mark)
	assert message.message == 'This event is full now'


