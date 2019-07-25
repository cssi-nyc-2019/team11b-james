# the import section
import webapp2
import jinja2
import os
from models import User


# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# other functions should go above the handlers or in a separate file

current_user = ""
users_query = User.query().fetch()

class MainHandler(webapp2.RequestHandler):
  def get(self):  # for a get request
    home_template = the_jinja_env.get_template('templates/home.html')
    self.response.write(home_template.render())

class LoginHandler(webapp2.RequestHandler):
  def get(self):  # for a get request
    login_template = the_jinja_env.get_template('templates/login.html')
    self.response.write(login_template.render())

class SignHandler(webapp2.RequestHandler):
  def get(self):  # for a get request
    sign_template = the_jinja_env.get_template('templates/sign.html')
    self.response.write(sign_template.render())

class AboutHandler(webapp2.RequestHandler):
	def get(self):
	   about_template = the_jinja_env.get_template('templates/about.html')
	   self.response.write(about_template.render())

class SignUp(webapp2.RequestHandler):
    def post(self):
        username = self.request.get('username')
        email = self.request.get('email')
        password = self.request.get('password')
        fullname = self.request.get('fullname')

        user = User(fullname = fullname, username = username, email = email, password = password)
        query = User().query().filter(User.username).fetch()
        if not (user in query):
	        query.insert(0,user)
	        user.put()


class ValidateUser(webapp2.RequestHandler):
	def post(self):

		planner_template = the_jinja_env.get_template('templates/planner.html')
		username = self.request.get('username')
		password = self.request.get('password')
		# usernames = User.query().filter(User.username).fetch()
		# passwords =User.query().filter(User.password).fetch()

		# if (username in usernames) and (password in passwords):
		# 	user = User.query().filter(User.username==name).fetch()
		# 	user.islogged=True
		# 	variable_dict={
		# 		'username':user.username
		# 	}
		# 	self.response.write(planner_template.render(variable_dict))

		# else:
		# 	variable_dict={
		# 	'message': "Your account doesn't exist, please sign up."
		# 	}

class SignOut(webapp2.RequestHandler):
	def get(self):
		current_user=''
		home_template = the_jinja_env.get_template('templates/home.html')
		self.response.write(home_template.render())

		planner_template = the_jinja_env.get_template('templates/planner.html')
		self.response.write(planner_template.render(variable_dict))

class Planner(webapp2.RequestHandler):
	def get(self):
		day_template = the_jinja_env.get_template('templates/day.html')
		self.response.write(day_template.render())

	def post(self):
		event = self.request.get('event');
		objective = self.request.get('objective')
		new_event = Event(name=event)
		new_objective = Objective(name=objective)



		events_query = Event.query().fetch()
		objectives_query = Objective.query().fetch()

		events_query.insert(0,new_event)
		new_event.put()

		objectives_query.insert(0,new_objective)
		new_objective.put()

		variable_dict = {
			'objectives': objectives_query,
			'events': events_query
		}

		day_template = the_jinja_env.get_template('templates/day.html')
		self.response.write(day_template.render())

class DailyObjective(webapp2.RequestHandler):
	def post(self):
		objective = self.request.get('objective')
    theDate = self.request.get('name')
		new_objective = Objective(name=objective)

		objectives_query = Objective.query().fetch()


		objectives_query.insert(0,new_objective)
		new_objective.put()

		variable_dict = {
			'objectives':objectives_query
		}

		day_template = the_jinja_env.get_template('templates/day.html')
		self.response.write(day_template.render(variable_dict))

class DailyEvent(webapp2.RequestHandler):
	def post(self):
		event = self.request.get('event')
		new_event = Event(name=event)

		events_query = Event.query().fetch()


		events_query.insert(0,new_event)
		new_event.put()

		variable_dict = {
			'events':events_query
		}

		day_template = the_jinja_env.get_template('templates/day.html')
		self.response.write(day_template.render(variable_dict))
 



# the app configuration section
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', MainHandler),
  ('/login', LoginHandler),
  ('/sign', SignHandler),
  ('/about', AboutHandler),
  ('/uploadUser', SignUp),
  ('/validateUser',ValidateUser),
  ('/planner',Planner)
  ], debug=True)
