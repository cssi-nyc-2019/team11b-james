# the import section
import webapp2
import jinja2
import os
from webapp2_extras import sessions
from models import User, Event, Objective


# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# other functions should go above the handlers or in a separate file
def getCurrentUser(self):
	#will return None if user does not exist
	return self.session.get('user')

def login(self, id):
	self.session['user'] = id

def logout(self):
	self.session['user'] = None

def isLoggedIn(self):
	if self.session['user'] is not None:
		return True
	else:
		return False

users_query = User.query().fetch()

class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)
    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()





class MainHandler(webapp2.RequestHandler):
	def get(self):  # for a get request
		home_template = the_jinja_env.get_template('templates/home.html')
		self.response.write(home_template.render())

class LoginHandler(BaseHandler):
	def get(self):
		login_template = the_jinja_env.get_template('templates/login.html')
		self.response.write(login_template.render())

	def post(self):
		planner_template = the_jinja_env.get_template('templates/planner.html')
		login_template = the_jinja_env.get_template('templates/login.html')
		username_input = self.request.get('username')
		password_input = self.request.get('password')



		variable_dict={}
		for user in users_query:
			if (username_input==user.username) and (password_input==user.password):
				login(self, username_input)
	    		user = getCurrentUser(self)
	    		variable_dict = {
	    			'username':user
	    		}
	    		self.response.write(planner_template.render(variable_dict))
			continue
		if variable_dict=={}:
			variable_dict={
				"message":"We could not find your account, please try again."
			}
			self.response.write(login_template.render(variable_dict))




  

class AboutHandler(webapp2.RequestHandler):
	def get(self):
	   about_template = the_jinja_env.get_template('templates/about.html')
	   self.response.write(about_template.render())


class SignUp(BaseHandler):
	def get(self):  # for a get request
		sign_template = the_jinja_env.get_template('templates/sign.html')
		self.response.write(sign_template.render())
	def post(self):
		email = self.request.get('email')
		username = self.request.get('username')
		password = self.request.get('password')

		user = User(username=username,password=password,email=email)
		query=User.query().fetch()
		query.insert(0,user)
		user_id=user.put()

		login_template = the_jinja_env.get_template('templates/login.html')
		self.response.write(login_template.render())




class LogOut(BaseHandler):
	def get(self):
		home_template = the_jinja_env.get_template('templates/home.html')
		user = getCurrentUser(self)
		if user is not None:
				logout(self)
				self.response.write(home_template.render())
		else:
				self.redirect('/')

class Planner(BaseHandler):
	def get(self):
		planner_template = the_jinja_env.get_template('templates/planner.html')
		user = getCurrentUser(self)
		if user is not None:
			user_info = User.query().filter(User.username == getCurrentUser(self)).fetch()
			variable_dict = {"username": user_info[0].username}
			self.response.write(planner_template.render(variable_dict))
		else:
			self.redirect('/')

class DayHandler(BaseHandler):
	def get(self):
		day_template = the_jinja_env.get_template("templates/day.html")
		user = getCurrentUser(self)
       userDate = self.request.get('date')
		if user is not None:
			user_info = User.query().filter(User.username == getCurrentUser(self)).fetch()



		self.response.write(day_template.render())

       variable_dict = {
         'fullDate': userDate
       }
		   self.response.write(day_template.render(variable_dict))



class DailyObjective(BaseHandler):
	def post(self):
		user = getCurrentUser(self)
		objective = self.request.get('objective')


		new_objective = Objective(name=objective,user=user)

		new_objective = Objective(name=objective,user=user)

		new_objective = Objective(name=objective)
		events_query = Event.query().fetch()


		objectives_query = Objective.query().fetch()


		objectives_query.insert(0,new_objective)
		new_objective.put()

		variable_dict = { 
			'objectives': objectives_query,
		}

		day_template = the_jinja_env.get_template('templates/day.html')
		self.response.write(day_template.render(variable_dict))

class DailyEvent(webapp2.RequestHandler):
	def post(self):

    user = getCurrentUser(self)
		event = self.request.get('event')
		new_event = Event(name=event, user = user)

		user = getCurrentUser(self)
		event = self.request.get('event')
		new_event = Event(name=event,user=user)


		events_query = Event.query().fetch()


		events_query.insert(0,new_event)
		new_event.put()

		variable_dict = { 
			'events':events_query
		}

		day_template = the_jinja_env.get_template('templates/day.html')
		self.response.write(day_template.render(variable_dict))


config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'your-super-secret-key',
}

# the app configuration section	
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', MainHandler),
  ('/login', LoginHandler),
  ('/about', AboutHandler),
  ('/signup', SignUp),
  ('/planner',Planner),
  ('/daily_objective',DailyObjective),
  ('/daily_event', DailyEvent),
  ('/logout',LogOut),
  ('/day',DayHandler)
  ], debug=True, config=config)
