import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs

class Admin(base_page.BaseHandler):
	def get(self):
		self.render('admin.html')
		
	def post(self):
		action = self.request.get('action')
		if action == 'add_channel':
			k = ndb.Key(db_defs.Channel, self.app.config.get('default-group'))
			chan = db_defs.Channel(parent=k)
			chan.name = self.request.get('channel-name')
			chan.active = True
			chan.put()
			self.render('admin.html', {'message' : 'Added ' + chan.name + ' to the database.'})
		else:
			self.render('admin.html', {'message' : 'Action ' + action + ' is unknown.'})
			
			