import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api import mail
from random import choice


class RFVHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(template.render('index.html', {}))

class URLShortnerHandler(webapp2.RequestHandler):
	def get(self, shortner):
		URL_table = {'Cs': 'https://coins.ph/invite/Hr12YA'}
		self.redirect(URL_table[shortner])

app = webapp2.WSGIApplication([
	webapp2.Route(r'/<shortner>', handler=URLShortnerHandler, name='URLShortner'),
	webapp2.Route(r'/', handler=RFVHandler, name='RFV')])

