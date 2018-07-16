
#!/usr/bin/env python3

import minidb
import model

class Downloads(minidb.Model, model.Model):
	url = str
	filename = str
	status = str
	size = int
	description = str
	def __init__(self):
		super(minidb.Model, self).__init__()
		super(model.Model, self).__init__()
