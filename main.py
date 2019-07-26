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



users_query = User.query().fetch()

class MainHandler(webapp2.RequestHandler):
	def get(self):  # for a get request
		home_template = the_jinja_env.get_template('templates/home.html')
		self.response.write(home_template.render())

class LoggedInHome(BaseHandler):
	def get(self):
		logged_home_template = the_jinja_env.get_template('templates/logged_home.html')
		self.response.write(logged_home_template.render())

class AboutHandler(webapp2.RequestHandler):
	def get(self):
	   about_template = the_jinja_env.get_template('templates/about.html')
	   self.response.write(about_template.render())

class LoginHandler(BaseHandler):
	def get(self):
		login_template = the_jinja_env.get_template('templates/login.html')
		self.response.write(login_template.render())

	def post(self):
		planner_template = the_jinja_env.get_template('templates/planner.html')
		login_template = the_jinja_env.get_template('templates/login.html')

		username_input = self.request.get('username')
		password_input = self.request.get('password')



		for user in users_query:
			if (username_input==user.username) and (password_input==user.password):
				login(self, user.username)
	    		current_user = getCurrentUser(self)
	    		variable_dict = {
	    			'username':current_user
	    		}
	    		self.response.write(planner_template.render(variable_dict))
			continue
		if isLoggedIn(self)==False:
			variable_dict={
				"message":"We could not find your account, please try again."
			}
			self.response.write(login_template.render(variable_dict))


class SignUp(BaseHandler):
	def get(self):  # for a get request
		sign_template = the_jinja_env.get_template('templates/sign.html')
		self.response.write(sign_template.render())
	def post(self):
		fullname = self.request.get('fullname')
		email = self.request.get('email')
		username = self.request.get('username')
		password = self.request.get('password')

		user = User(fullname=fullname,username=username,email=email,password=
			password)

		user_id=user.put()

		login_template = the_jinja_env.get_template('templates/login.html')
		self.response.write(login_template.render())




class LogOut(BaseHandler):
	def get(self):
		home_template = the_jinja_env.get_template('templates/home.html')
		current_user = getCurrentUser(self)
		if current_user is not None:
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

	def post(self):
		day_template = the_jinja_env.get_template("templates/day.html")

		current_user = getCurrentUser(self)
		current_date = self.request.get('current_date')
	
		objectiveQuery=Objective.query().filter(Objective.user==current_user,Objective.date==current_date).fetch()
		variable_dict = {
			'date':current_date,
			'objectives':objectiveQuery
			#'events': Event.query().filter(Event.date==current_date).fetch()
		}

		self.response.write(day_template.render(variable_dict))

class AccountHandler(BaseHandler):
	def get(self):
		account_template = the_jinja_env.get_template('templates/account.html')
		self.response.write(account_template.render())

#class DayHandler(BaseHandler):
	


		
class DailyObjectives(BaseHandler):
	def post(self):
		day_template = the_jinja_env.get_template('templates/day.html')

		current_user = getCurrentUser(self);
		current_date = self.request.get('current_date')

		objective = self.request.get('objective')
		add_objective = Objective(name=objective,user=current_user,date=current_date)
		add_objective.put()

		variable_dict = {
			'date':current_date,
			'objectives':Objective.query().filter(Objective.user==current_user,Objective.date==current_date).fetch()
		}
		self.response.write(day_template.render(variable_dict))


config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'your-super-secret-key',
}

# the app configuration section	
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', MainHandler),
  ('/logged_home',LoggedInHome),
  ('/login', LoginHandler),
  ('/about', AboutHandler),
  ('/signup', SignUp),
  ('/planner',Planner),
  ('/account',AccountHandler),
  ('/logout',LogOut),
  #('/day',DayHandler),
  ('/objectives',DailyObjectives)
  ], debug=True, config=config)
