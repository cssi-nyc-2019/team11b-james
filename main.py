# the import section
import webapp2
import jinja2
import os

# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# other functions should go above the handlers or in a separate file

# the handler section
class MainHandler(webapp2.RequestHandler):
  def get(self):  # for a get request
    home_template = the_jinja_env.get_template('templates/home.html')
    self.response.write(home_template.render())
class LoginHandler(webapp2.RequestHandler):
	def get(self):
		login_template = the_jinja_env.get_template('templates/login.html')
		self.response.write(login_template.render())
# the app configuration section	
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', MainHandler),
  ('/login', LoginHandler)
  ], debug=True)