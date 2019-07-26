from google.appengine.ext import ndb

class User(ndb.Model):
	fullname = ndb.StringProperty(required=True)
	username = ndb.StringProperty(required=True)
	email = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)

class Objective(ndb.Model):
	name = ndb.StringProperty(required=True)
	objective_complete = ndb.BooleanProperty(required=False)
	user = ndb.StringProperty(required=True)
	date = ndb.StringProperty(required=True)
class Event(ndb.Model):
	name = ndb.StringProperty(required=True)
	user = ndb.StringProperty(required=True)
	date = ndb.StringProperty(required=True)


