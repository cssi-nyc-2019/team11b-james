from google.appengine.ext import ndb

class User(ndb.Model):
	fullname = ndb.StringProperty(required=True)
	username = ndb.StringProperty(required=True)
	email = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)

class Objective(ndb.Model):
	name = ndb.StringProperty(required=True)
	objective_complete = ndb.BooleanProperty(required=False)
	user = ''
	date = ''
class Event(ndb.Model):
	name = ndb.StringProperty(required=True)
	user = ''
	date = ndb.StringProperty(required=True)
	# user = 

