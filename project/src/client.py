from .EventSystem import EventSystem
from .User import Student, Staff, Guest
from .Event import Course, Seminar
from datetime import datetime
from .Session import Session
import csv


def bootstrap_system():
	system = EventSystem()
	with open('user.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if row['role'] == 'trainee':
				system.add_user(Student(row['zID'], row['email'], row['name'], row['password']))
			if row['role'] == 'trainer':
				system.add_user(Staff(row['zID'], row['email'], row['name'], row['password']))

	date_format = "%Y-%m-%d"
	q = '2018-12-12'
	w = '2018-12-13'
	e = '2018-12-15'
	#event1 = Course('Comp1511', q,w,e, 2, 'UNSW', Staff('4119991','z4119991@unsw.net','name4119991','pass29938'), '20','Come on')
	event1 = system.add_event('Comp1511', q,w,e, 30, 'UNSW', Staff('4119991','z4119991@unsw.net','name4119991','pass29938'), '20','Come on','Course')

	#event2 = Seminar('Co', q,w,e, 2, 'UNSW', Staff('4119991','z4119991@unsw.net','name4119991','pass29938'), '20','Come on')
	event2 = system.add_event('Comp1521', q,w,e, 30, 'UNSW', Staff('4','4','4','4'), '20','Come on', 'Seminar')
	event2.add_sessions('Baby', 2, 'UNSW', q ,w)
	event2.add_sessions('Boom', 2, 'UNSW', q ,w)
	event2.add_sessions('Cat', 2, 'UNSW', q ,w)
	# event3 = Seminar('Game',q,w,e,2,'UNSW', Staff('4','4','4','4'),'20')
	# system.add_event(event3)
	# event3.add_sessions(Session('Baby', 1, 'UNSW', q ,w))
	system.add_user(Guest('1','1','1'))
	system.add_user(Guest('2','2','2'))
	system.add_user(Guest('3','3','3'))
	system.add_user(Staff('4','4','4','4'))
	user = Staff('4','4','4','4')
	# user.add_event_posted(event3)
	return system
