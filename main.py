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

<<<<<<< HEAD
current_user = "madaf"
=======
<<<<<<< HEAD
=======
current_user = ""
>>>>>>> 0b7fb9d8c693fdcba204b0213f09546600b8f457
users_query = User.query().fetch()
>>>>>>> 8cb886eccf268b4c6ecbd47c5f29980a66e540b0

class MainHandler(webapp2.RequestHandler):
  def get(self):  # for a get request
    home_template = the_jinja_env.get_template('templates/home.html')
    self.response.write(home_template.render())

class LoginHandler(webapp2.RequestHandler):
  def get(self):  # for a get request
    login_template = the_jinja_env.get_template('templates/login.html')
    self.response.write(login_template.render())

<<<<<<< HEAD
class SignHandler(webapp2.RequestHandler):
=======
  def post(self):
		planner_template = the_jinja_env.get_template('templates/planner.html')
		login_template = the_jinja_env.get_template('templates/login.html')
		username_input = self.request.get('username')
		password_input = self.request.get('password')



		variable_dict={}
		for user in users_query:
			if (username_input==user.username) and (password_input==user.password):
				current_user = username_input
				variable_dict={
					'username':current_user
				}
				
				self.response.write(planner_template.render(variable_dict))
			continue
		if variable_dict=={}:
			variable_dict={
				"message":"We could not find your account, please try again."
			}
			self.response.write(login_template.render(variable_dict))
class SignUpHandler(webapp2.RequestHandler):
>>>>>>> 8cb886eccf268b4c6ecbd47c5f29980a66e540b0
  def get(self):  # for a get request
    sign_template = the_jinja_env.get_template('templates/sign.html')
    self.response.write(sign_template.render())

class AboutHandler(webapp2.RequestHandler):
	def get(self):
	   about_template = the_jinja_env.get_template('templates/about.html')
	   self.response.write(about_template.render())

<<<<<<< HEAD
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
			
		# 	self.response.write(planner_template.render(variable_dict))

=======
class SignOut(webapp2.RequestHandler):
	def get(self):
		current_user=''
		home_template = the_jinja_env.get_template('templates/home.html')
		self.response.write(home_template.render())

class PlannerHandler(webapp2.RequestHandler):
	def get(self):
		variable_dict = {
		'username':current_user
		}
>>>>>>> 8cb886eccf268b4c6ecbd47c5f29980a66e540b0
		planner_template = the_jinja_env.get_template('templates/planner.html')
		self.response.write(planner_template.render(variable_dict))

class Planner(webapp2.RequestHandler):
	def get(self):
<<<<<<< HEAD
		planner_template = the_jinja_env.get_template('templates/planner.html')
		self.response.write(planner_template.render())
=======

		day_template = the_jinja_env.get_template('templates/day.html')
		self.response.write(day_template.render())

class DailyObjective(webapp2.RequestHandler):
	def post(self):
		objective = self.request.get('objective')
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
>>>>>>> 8cb886eccf268b4c6ecbd47c5f29980a66e540b0



# the app configuration section	
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', MainHandler),
  ('/login', LoginHandler),
  ('/sign', SignHandler),
  ('/about', AboutHandler),
<<<<<<< HEAD
  ('/uploadUser', SignUp),
  ('/validateUser',ValidateUser),
  ('/planner',Planner)
=======
  ('/planner',PlannerHandler),
  ('/daily_objective',DailyObjective),
  ('/daily_event', DailyEvent),
  ('/signout',SignOut),
  ('/day',DayLayoutHandler)
>>>>>>> 8cb886eccf268b4c6ecbd47c5f29980a66e540b0
  ], debug=True)
